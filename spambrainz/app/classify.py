from app import model, db
from tensorflow.keras.models import load_model
from .preprocessing import preprocess_editor
import json
import datetime
import numpy as np
import flask 
model = model


# initialize constants used for server queuing
EDITOR_QUEUE = "editor_queue"
BATCH_SIZE = 1
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25

def string_to_datetime(string_dt):
    return datetime.datetime(*[int(v) for v in string_dt.replace('T', '-').replace(':', '-').split('-')])


def classify_process():
    # load the pre-trained Keras model (here we are using a model
    # pre-trained on ImageNet and provided by Keras, but you can
    # substitute in your own networks just as easily)
    print("* Loading model...")
    global model
    model = load_model('static/models/weights/lodbrok1.h5')
    print("* Model loaded")

   
    queue = db.lrange(EDITOR_QUEUE, 0, BATCH_SIZE - 1)
    editorIDs = []
    # batch = None

    # loop over the queue
    # for q in queue:
        # deserialize the object and obtain the input image
    queue = json.loads(queue[0])
    editorIDs.append(queue["id"])
    
    # changing string datetime to datetime objects
    queue["birth_date"] = string_to_datetime(queue["birth_date"])
    queue["member_since"] = string_to_datetime(queue["member_since"])
    queue["email_confirm_date"] = string_to_datetime(queue["email_confirm_date"])
    queue["last_updated"] = string_to_datetime(queue["last_updated"])
    queue["last_login_date"] = string_to_datetime(queue["last_login_date"])
    
    queue = preprocess_editor(queue)

    queue = np.array([queue])
            
    

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

        if(result[0][1]>result[0][0]) :
            prediction = {
                'result' : "Spam Editor Account"
            }

        else:
            prediction = {
                'result' : "Non Spam Editor Account"
            }        

        print(prediction) 
        print(type(prediction))
        print(editorIDs[0])
        prediction = json.dumps(prediction)
        print(type(prediction))

        db.set(str(editorIDs[0]), prediction)

        # remove the set of editor from our queue
        db.ltrim(EDITOR_QUEUE, len(editorIDs), -1)

    # sleep for a small amount
    # time.sleep(SERVER_SLEEP)
    # return


