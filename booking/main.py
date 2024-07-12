from fastapi import FastAPI, Depends, Request, HTTPException, Form, status, Response
from . import schemas, models
from typing import Annotated
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from . import auth
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


@app.get("/", status_code=status.HTTP_200_OK)
def user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return {"User": user}


@app.get("/buses/")
def all(db: Session = Depends(get_db)):
    try:
        buses = db.query(models.Bus).all()
        return buses
    except Exception as e:
        return {"error": str(e)}


@app.get("/routes/")
def all(db: Session = Depends(get_db)):
    try:
        routes = db.query(models.Route).all()
        return routes
    except Exception as e:
        return {"error": str(e)}


@app.get("/buses/search")
def search(source: str, destination: str, db: Session = Depends(get_db)):
    try:
        routes = (
            db.query(models.Route)
            .filter(
                models.Route.source == source
                and models.Route.destination == destination
            )
            .all()
        )
        return routes
    except Exception as e:
        return {"error": str(e)}


@app.post("/bus/booking")
def bookings(route_id: int, seat_number: int, db: Session = Depends(get_db)):
    try:
        booking = models.Booking(route_id=route_id, seat_number=seat_number)
        db.add(booking)
        db.commit()
        db.refresh(booking)
        return booking
    except Exception as e:
        return {"error": str(e)}


@app.delete("/bus/")
def delete(db: Session = Depends(get_db)):
    buses = db.query(models.Bus).all()
    for bus in buses:
        del_bus = db.query(models.Bus).filter(models.Bus.id == bus.id).first()
        db.delete(del_bus)
        db.commit()
    return "deleted"


@app.delete("/route/")
def delete(db: Session = Depends(get_db)):
    routes = db.query(models.Route).all()
    for route in routes:
        del_route = db.query(models.Route).filter(models.Route.id == route.id).first()
        db.delete(del_route)
        db.commit()
    return "deleted"


@app.delete("/booking/")
def delete(db: Session = Depends(get_db)):
    bookings = db.query(models.Booking).all()
    for booking in bookings:
        del_booking = (
            db.query(models.Booking).filter(models.Booking.id == booking.id).first()
        )
        db.delete(del_booking)
        db.commit()
    return "deleted"
