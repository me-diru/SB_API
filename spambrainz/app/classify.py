from app import model, db
from tensorflow.keras.models import load_model
from .preprocessing import preprocess_editor
import json
import datetime
import numpy as np
import flask 
model = model


# initialize constants used for redis server
EDITOR_QUEUE = "editor_queue"
BATCH_SIZE = 1
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25

# function used to convert string to datetime, used before preprocessing
def string_to_datetime(string_dt):
    if string_dt is None:
        return None
    return datetime.datetime(*[int(v) for v in string_dt.replace('T', '-').replace(':', '-').split('-')])

# function used to retrive editor_data from redis and store the results back 
def classify_process():
    
    print("* Loading model...")
    global model
    model = load_model('static/models/weights/current_lodbrok.h5')
    print("* Model loaded")

    # All the editor detials are retrived here from redis
    queue = db.lrange(EDITOR_QUEUE, 0, BATCH_SIZE - 1)
    editorIDs = []
    
    queue = json.loads(queue[0])
    editorIDs.append(queue["id"])
    
    # changing string datetime to datetime objects
    queue["birth_date"] = string_to_datetime(queue["birth_date"])
    queue["member_since"] = string_to_datetime(queue["member_since"])
    queue["email_confirm_date"] = string_to_datetime(queue["email_confirm_date"])
    queue["last_updated"] = string_to_datetime(queue["last_updated"])
    queue["last_login_date"] = string_to_datetime(queue["last_login_date"])
    
    # preprocessing the given input to get prediction
    queue = preprocess_editor(queue)

    # defining the structure
    queue = np.array([queue])
    
    # only data from index 1 is considered while predicting, thus 
    # not taking the spam value into consideration
    predict_data = {
        "main_input": np.array(queue[:,1:10]),
        "email_input": np.array(queue[:,10]),
        "website_input": np.array(queue[:,11]),
        "bio_input": np.array(queue[:,12:]),
    }

    # check to see if we need to process the batch
    if len(editorIDs) > 0:
        
        result = model.predict(x = [
            predict_data["main_input"], 
            predict_data["email_input"],
            predict_data["website_input"],
            predict_data["bio_input"],
        ])

        # identifying the prediction done by lodbrok
        # if closer to 1 it's a spam account else a non spam account
        if(result[0][1]>result[0][0]) :
            prediction = {
                'result' : "Spam Editor Account"
            }

        else:
            prediction = {
                'result' : "Non Spam Editor Account"
            }        

        # converting to fit in redis
        prediction = json.dumps(prediction)        

        #storign the result in redis
        db.set(str(editorIDs[0]), prediction)

        # remove the set of editor from our queue
        db.ltrim(EDITOR_QUEUE, len(editorIDs), -1)

  


