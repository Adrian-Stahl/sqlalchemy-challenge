import numpy as np
import re
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.sql import exists  

from flask import Flask, jsonify

#Establishing Database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#Establishing Flask and Routes
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/prec<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/observations<br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)"
        

   
 
@app.route("/api/v1.0/precipitation") #Convert query results to a dictionary using `date` as the key and `tobs` as the value
def prec():
    # Create session (link) from Python to the DB
    session_link = Session(engine)

    # Query Measurement
    res = (session.query(Measurement.date, Measurement.tobs)
                      .order_by(Measurement.date))
    
     prec_date_obs = []
    for rows in results:
        dt_dictionary = {}
        dt_dictionary["date"] = rows.date
        dt_dictionary["tobs"] = rows.tobs
        prec_date_obs.append(dt_dictionary)

    return jsonify(prec_date_obs)     
        
@app.route("/api/v1.0/stations") 
def station():
    
    session_link = Session(engine)
    
    res = session.query(Station.name).all()

    details = list(np.ravel(res))

    return jsonify(details)
        
@app.route("/api/v1.0/tobs") 
def observations():
    
    session_link = Session(engine)
    end_date = (session.query(Measurement.date)
                          .order_by(Measurement.date
                          .desc())
                          .first())
        
        
        
        
        
        
        
        
        
        
        
        