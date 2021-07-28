import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import date

from app.database import Base


class Fish(Base):
    __tablename__ = "fish"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # year = Column(Integer, nullable=False)
    # month = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    facility_ref_number = Column(Integer, nullable=False)
    licence_holder = Column(String, nullable=False)
    site_name = Column(String, nullable=False)
    fish_health_zone = Column(Float, nullable=False)
    counts_performed = Column(Integer, nullable=True)



'''
Year
Month
Facility Reference 
Number
Licence Holder
Site Common Name
Fish Health Zone
Comments
Year Class
'''