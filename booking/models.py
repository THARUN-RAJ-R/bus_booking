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

    id = Column(Integer, primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey("route.id"))
    seat_number = Column(Integer)

    route = relationship("Route", back_populates="bookings")


class Seats(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True, index=True)
    seat_number = Column(Integer)
    route_id = Column(Integer)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashded_password = Column(String)


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
        source="A",
        destination="B",
        bus_id=id_1,
        departure_time=8,
        arrival_time=10,
    )
    route_2 = Route(
        source="C",
        destination="D",
        bus_id=id_1,
        departure_time=12,
        arrival_time=14,
    )
    route_3 = Route(
        source="A",
        destination="B",
        bus_id=id_2,
        departure_time=9,
        arrival_time=11,
    )
    route_4 = Route(
        source="C",
        destination="D",
        bus_id=id_2,
        departure_time=13,
        arrival_time=15,
    )
    route_5 = Route(
        source="A",
        destination="B",
        bus_id=id_3,
        departure_time=10,
        arrival_time=12,
    )
    route_6 = Route(
        source="C",
        destination="D",
        bus_id=id_3,
        departure_time=14,
        arrival_time=16,
    )

    db.add(route_1)
    db.add(route_2)
    db.add(route_3)
    db.add(route_4)
    db.add(route_5)
    db.add(route_6)
    db.commit()


db.close()
