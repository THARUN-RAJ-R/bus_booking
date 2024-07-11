from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base, SessionLocal, engine


class Bus(Base):
    __tablename__ = "bus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)

    routes = relationship("Route", back_populates="bus")


class Route(Base):
    __tablename__ = "route"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    destination = Column(String)
    bus_id = Column(Integer, ForeignKey("bus.id"))
    departure_time = Column(Integer)
    arrival_time = Column(Integer)

    bus = relationship("Bus", back_populates="routes")
    bookings = relationship("Booking", back_populates="route")


class Booking(Base):
    __tablename__ = "booking"

    user_id = Column(String, primary_key=True, index=False)
    route_id = Column(Integer, ForeignKey("route.id"))
    seat_number = Column(Integer)

    route = relationship("Route", back_populates="bookings")


Base.metadata.create_all(engine)


db = SessionLocal()

if db.query(Bus).count() == 0:
    bus_1 = Bus(name="Bus_A", type="type_A")
    bus_2 = Bus(name="Bus_B", type="type_B")
    bus_3 = Bus(name="Bus_C", type="type_C")
    db.add(bus_1)
    db.add(bus_2)
    db.add(bus_3)
    db.commit()
    id_1 = bus_1.id
    id_2 = bus_2.id
    id_3 = bus_3.id

    route_1 = Route(
        source="Station A",
        destination="Station B",
        bus_id=id_1,
        departure_time=800,
        arrival_time=1000,
    )
    route_2 = Route(
        source="Station C",
        destination="Station D",
        bus_id=id_1,
        departure_time=1200,
        arrival_time=1400,
    )
    route_3 = Route(
        source="Station A",
        destination="Station B",
        bus_id=id_2,
        departure_time=900,
        arrival_time=1100,
    )
    route_4 = Route(
        source="Station C",
        destination="Station D",
        bus_id=id_2,
        departure_time=1300,
        arrival_time=1500,
    )
    route_5 = Route(
        source="Station A",
        destination="Station B",
        bus_id=id_3,
        departure_time=1000,
        arrival_time=1200,
    )
    route_6 = Route(
        source="Station C",
        destination="Station D",
        bus_id=id_3,
        departure_time=1400,
        arrival_time=1600,
    )

    db.add(route_1)
    db.add(route_2)
    db.add(route_3)
    db.add(route_4)
    db.add(route_5)
    db.add(route_6)
    db.commit()


db.close()
