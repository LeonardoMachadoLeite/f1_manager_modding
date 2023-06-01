from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Float

def get_RaceModel(db):
    class Race(db.Model):
        __tablename__ = 'Races'
        RaceID = Column(Integer, primary_key=True)
        SeasonID = Column(Integer)
        Day = Column(Integer)
        TrackID = Column(Integer)
        State = Column(Integer)
        RainPractice = Column(Integer)
        TemperaturePractice = Column(Float)
        WeatherStatePractice = Column(Integer)
        RainQualifying = Column(Integer)
        TemperatureQualifying = Column(Float)
        WeatherStateQualifying = Column(Integer)
        RainRace = Column(Integer)
        TemperatureRace = Column(Float)
        WeatherStateRace = Column(Integer)
    
    return Race