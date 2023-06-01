from flask_marshmallow import Marshmallow

def get_RacesSchema(ma):
    class RacesSchema(ma.Schema):
        class Meta:
            fields = ('RaceID', 'SeasonID', 'Day', 'TrackID', 'State',
                    'RainPractice', 'TemperaturePractice', 'WeatherStatePractice',
                    'RainQualifying', 'TemperatureQualifying', 'WeatherStateQualifying',
                    'RainRace', 'TemperatureRace', 'WeatherStateRace')
    
    return RacesSchema