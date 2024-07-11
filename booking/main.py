from fastapi import FastAPI, Depends, Request, HTTPException, Form, status, Response
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="booking/static"), name="static")

templates = Jinja2Templates(directory="booking/templates")

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "bus booking"}


@app.get("/bus/")
def all(db: Session = Depends(get_db)):
    try:
        bus = db.query(models.Bus).all()
        return {"bus": bus}
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
