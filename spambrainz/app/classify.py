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
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25

# function used to convert string to datetime, used before preprocessing


def string_to_datetime(string_dt):
    if string_dt is None:
        return None
    return datetime.datetime(*[int(v) for v in string_dt.replace('T', '-').replace(':', '-').split('-')])

# function used to retrive editor_data from redis and store the results back


def classify_process(size):

    print("* Loading model...")
    global model
    model = load_model('static/models/weights/current_lodbrok.h5')
    print("* Model loaded")

    BATCH_SIZE = size

    # All the editor detials are retrived here from redis
    queue = db.lrange(EDITOR_QUEUE, 0, BATCH_SIZE - 1)

    for q in queue:

        q = json.loads(q)
        editor_id = q["id"]

        # changing string datetime to datetime objects
        q["birth_date"] = string_to_datetime(q["birth_date"])
        q["member_since"] = string_to_datetime(q["member_since"])
        q["email_confirm_date"] = string_to_datetime(q["email_confirm_date"])
        q["last_updated"] = string_to_datetime(q["last_updated"])
        q["last_login_date"] = string_to_datetime(q["last_login_date"])

        # preprocessing the given input to get prediction
        q = preprocess_editor(q)

        # defining the structure
        q = np.array([q])

        # only data from index 1 is considered while predicting, thus
        # not taking the spam value into consideration
        predict_data = {
            "main_input": np.array(q[:, 1:10]),
            "email_input": np.array(q[:, 10]),
            "website_input": np.array(q[:, 11]),
            "bio_input": np.array(q[:, 12:]),
        }

        result = model.predict(x=[
            predict_data["main_input"],
            predict_data["email_input"],
            predict_data["website_input"],
            predict_data["bio_input"],
        ])

        # identifying the prediction done by lodbrok
        # if closer to 1 it's a spam account else a non spam account
        if(result[0][1] > result[0][0]):
            prediction = {
                'result': "Spam Editor Account"
            }

        else:
            prediction = {
                'result': "Non Spam Editor Account"
            }

        # converting to fit in redis
        prediction = json.dumps(prediction)

        # storign the result in redis
        db.set(str(editor_id), prediction)

    # remove the set of editor from our queue
    db.ltrim(EDITOR_QUEUE, size, -1)
