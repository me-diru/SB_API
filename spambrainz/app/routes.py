# import the necessary packages

from app import app, db
import flask
import numpy as np
import uuid
import time
import json
import sys
import io
import datetime
from .preprocessing import preprocess_editor
from .classify import classify_process, EDITOR_QUEUE, CLIENT_SLEEP

@app.route("/predict", methods=["POST"])
def predict():

    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        if flask.request.json:
           
            #idi chudu okasari ****************************************************
            editor_account = flask.request.json

            # print(type(editor_account))
            # print(editor_account["member_since"])
            # print(type(editor_account["member_since"]))

            editor_id = editor_account["id"]

            if(editor_account["area"]  is ''):
                editor_account["area"] = None
            if(editor_account["bio"]  is ''):
                editor_account["bio"] = None

            editor_account = dict(editor_account)

            
            # editor_account = np.array([editor_account])

            

            #idi chudu okasari ****************************************************
            # print("step 1")
            db.rpush(EDITOR_QUEUE, json.dumps(editor_account))
            classify_process()
            # keep looping until our model server returns the output
            # predictions
            # while True:
                # attempt to grab the output predictions
            output = db.get(editor_id)

              
            if output is not None:
                    
                data["predictions"] = json.loads(output)

                    # delete the result from the database and break
                    # from the polling loop
                db.delete(editor_id)
                    

                # sleep for a small amount to give the model a chance
                # to classify the input image
            #time.sleep(CLIENT_SLEEP)

            # indicate that the request was a success
                data["success"] = True

        else:
            return "No data found"

    # return the data dictionary as a JSON response
    return flask.jsonify(data)

