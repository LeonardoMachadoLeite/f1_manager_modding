from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv, find_dotenv
import sys

load_dotenv(find_dotenv())

app = Flask(__name__)
MODDED_SAVE_DIR = os.getenv("MODDED_SAVE_DIR")
TARGET_SAVE = "save9"
SAVEFILE_PATH = "{}\\{}\\main.db".format(MODDED_SAVE_DIR, TARGET_SAVE)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{SAVEFILE_PATH}'
sys.path.append(os.getenv("SRC_DIR"))

from Schemas.RacesSchema import get_RacesSchema
from Model.Races import get_RaceModel

db = SQLAlchemy(app)
ma = Marshmallow(app)

Race = get_RaceModel(db)
RacesSchema = get_RacesSchema(ma)

races_schema = RacesSchema(many=True)
race_schema = RacesSchema()

@app.route('/')
def check_server():
    print(f'Type(Race): {type(Race)}')
    print(f'Type(RacesSchema): {type(RacesSchema)}')
    return jsonify(message="The server is online."), 200

@app.route('/races', methods=['GET'])
def get_races():
    SeasonID = request.args.get("SeasonID")

    if SeasonID:
        races_list = Race.query.filter(Race.SeasonID == int(SeasonID)).all()
    else:
        races_list = Race.query.all()
    
    result = races_schema.dump(races_list)
    return jsonify(result), 200

@app.route('/races/<int:RaceID>', methods=['GET', 'PUT'])
def get_race(RaceID:int):
    if request.method == 'GET':
        race = Race.query.filter(Race.RaceID == int(RaceID)).first()
        result = race_schema.dump(race)
        return jsonify(result), 200
    if request.method == 'PUT':
        race = Race.query.filter(Race.RaceID == int(RaceID)).first()
        if race:
            race.SeasonID = int(request.form['SeasonID'])
            race.Day = int(request.form['Day'])
            race.TrackID = int(request.form['TrackID'])
            race.State = int(request.form['State'])

            race.RainPractice = int(request.form['RainPractice'])
            race.TemperaturePractice = float(request.form['TemperaturePractice'])
            race.WeatherStatePractice = int(request.form['WeatherStatePractice'])

            race.RainQualifying = int(request.form['RainQualifying'])
            race.TemperatureQualifying = float(request.form['TemperatureQualifying'])
            race.WeatherStateQualifying = int(request.form['WeatherStateQualifying'])

            race.RainRace = int(request.form['RainRace'])
            race.TemperatureRace = float(request.form['TemperatureRace'])
            race.WeatherStateRace = int(request.form['WeatherStateRace'])

            db.session.commit()
            return jsonify(message="The Race has been updated"), 202
        else:
            return jsonify(message="The Race {RaceID} has not been found"), 404


if __name__ == '__main__':
    app.run()
