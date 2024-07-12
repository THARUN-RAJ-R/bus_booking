from fastapi import (
    FastAPI,
    Depends,
    Request,
    HTTPException,
    Form,
    status,
    Response,
    Query,
)
from . import schemas, models
from typing import Annotated
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from . import auth
import logging
from .auth import get_current_user

app = FastAPI()
app.include_router(auth.router)

app.mount("/static", StaticFiles(directory="booking/static"), name="static")

templates = Jinja2Templates(directory="booking/templates")

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@app.get("/bus/booking", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def homepage(request: Request):
    return templates.TemplateResponse("bookingpage.html", {"request": request})


@app.post("/bus/booking", status_code=201)
def bookings(
    route_id: int = Form(...),
    seat_number: int = Form(...),
    db: Session = Depends(get_db),
):
    logging.info(
        f"Received booking request: route_id={route_id}, seat_number={seat_number}"
    )
    try:
        if seat_number > 30:
            logging.error("Seat number greater than 30")
            raise HTTPException(status_code=400, detail="maximum number of seat is 30")

        route = db.query(models.Route).filter(models.Route.id == route_id).first()
        if not route:
            logging.error("Route not found")
            raise HTTPException(status_code=404, detail="Route not found")

        bus_id = route.bus_id
        existing_seat = (
            db.query(models.Seats)
            .filter(
                models.Seats.bus_id == bus_id, models.Seats.seat_number == seat_number
            )
            .first()
        )
        if existing_seat:
            logging.error("Seat already booked")
            raise HTTPException(status_code=400, detail="Seat already booked")

        booking = models.Booking(route_id=route_id, seat_number=seat_number)
        seat = models.Seats(bus_id=bus_id, seat_number=seat_number)

        db.add(booking)
        db.add(seat)
        db.commit()
        db.refresh(booking)

        logging.info(f"Booking successful: {booking}")
        return booking
    except Exception as e:
        logging.error(f"Error processing booking: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def get_login_page(request: Request):
    return templates.TemplateResponse("loginpage.html", {"request": request})


@app.get("/homepage", response_class=HTMLResponse, status_code=status.HTTP_200_OK)
def homepage(request: Request):
    return templates.TemplateResponse("Homepage.html", {"request": request})


@app.get("/search", response_class=HTMLResponse)
def search(
    request: Request, source: str, destination: str, db: Session = Depends(get_db)
):
    routes = (
        db.query(models.Route)
        .filter(
            models.Route.source == source and models.Route.destination == destination
        )
        .all()
    )
    return templates.TemplateResponse(
        "Homepage.html", {"request": request, "routes": routes}
    )


@app.get("/buses/", status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    try:
        buses = db.query(models.Bus).all()
        return buses
    except Exception as e:
        return {"error": str(e)}


@app.get("/routes/", status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    try:
        routes = db.query(models.Route).all()
        return routes
    except Exception as e:
        return {"error": str(e)}


# @app.delete("/bus/", status_code=204)
# def delete(db: Session = Depends(get_db)):
#     buses = db.query(models.Bus).all()
#     for bus in buses:
#         del_bus = db.query(models.Bus).filter(models.Bus.id == bus.id).first()
#         db.delete(del_bus)
#         db.commit()
#     return "deleted"


# @app.delete("/route/", status_code=204)
# def delete(db: Session = Depends(get_db)):
#     routes = db.query(models.Route).all()
#     for route in routes:
#         del_route = db.query(models.Route).filter(models.Route.id == route.id).first()
#         db.delete(del_route)
#         db.commit()
#     return "deleted"


# @app.delete("/booking/", status_code=204)
# def delete(db: Session = Depends(get_db)):
#     bookings = db.query(models.Booking).all()
#     for booking in bookings:
#         del_booking = (
#             db.query(models.Booking).filter(models.Booking.id == booking.id).first()
#         )
#         db.delete(del_booking)
#         db.commit()
#     return "deleted"
