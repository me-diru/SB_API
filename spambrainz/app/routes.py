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
from .classify import classify_process, EDITOR_QUEUE, CLIENT_SLEEP, string_to_datetime
from .train import retrain_model

@app.route("/predict", methods=["POST"])
def predict():

    data = {"success": False}

    if flask.request.method == "POST":
        if flask.request.json:           
            
            editor_account = flask.request.json

            # taking editor ID to get the results from redis
            editor_id = editor_account["id"]

            # convert missing parts to None to be compatible with preprossing
            if(editor_account["area"]  is ''):
                editor_account["area"] = None
            if(editor_account["bio"]  is ''):
                editor_account["bio"] = None
            
            editor_account = dict(editor_account)
           
            # the editor accounts are pushed into the redis queue
            db.rpush(EDITOR_QUEUE, json.dumps(editor_account))

            # the classification model is called 
            classify_process()      

            # the classification done is retrived form redis
            output = db.get(editor_id)
            output =  json.loads(output)
            output["id"] = editor_id
            if output is not None:
                data["predictions"] = output              
                db.delete(editor_id)                    
                data["success"] = True


    # return the data dictionary as a JSON response
    return flask.jsonify(data)


@app.route("/train", methods=["POST"])

def train():
    if flask.request.method == "POST":
        if flask.request.json:           

            data = {"success": False}

            editor_accounts = flask.request.json

            for key, editor_account in editor_accounts.items(): 
                                
                # set unfilled values to None to be compatible with preprocessing
                if(editor_account["area"]  is ''):                    
                    editor_account["area"] = None
                if(editor_account["bio"]  is ''):
                    editor_account["bio"] = None

                # converting string json date atrributes data to datetime object
                editor_account["birth_date"] = string_to_datetime(editor_account["birth_date"])
                editor_account["member_since"] = string_to_datetime(editor_account["member_since"])
                editor_account["email_confirm_date"] = string_to_datetime(editor_account["email_confirm_date"])
                editor_account["last_updated"] = string_to_datetime(editor_account["last_updated"])
                editor_account["last_login_date"] = string_to_datetime(editor_account["last_login_date"])

                   

            number_of_editors = len(editor_accounts)

            preprocess_data = np.empty((number_of_editors*2 ,524)) 

            # preprocessing the given data for the model to train on
            for i in range(0,number_of_editors):
                print(int(editor_accounts[str(i)]['verdict']))
                preprocess_data[i] = preprocess_editor(editor_accounts[str(i)], int(editor_accounts[str(i)]['verdict']))

            # retraining the model with new data
            if retrain_model(preprocess_data):
                data["response"] = "Successfully retrianed the model"
                data["success"] = True
                
    return flask.jsonify(data)

            

                                            
