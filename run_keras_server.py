# USAGE
# Start the server:
# 	python run_keras_server.py
# Submit a request via cURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
# Submita a request via Python:
#	python simple_request.py

# import the necessary packages
import keras
from tensorflow.keras.models import load_model
import numpy as np
import flask
import io
from preprocessing import preprocess_editor
import datetime
#https://stackoverflow.com/questions/33224068/how-convert-datetime-local-to-datetime-in-python/33224436

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None

def load_lodbrok():
	# load the pre-trained Keras model (LodBrok)
	global model
	model = load_model('static/models/weights/lodbrok1.h5')


@app.route("/predict", methods=["POST"])
def predict():
	
	# get editor data from the form submitted
	
	editor_data = flask.request.get_json(force=True)	
	

	# #converting html datetime-local to python datetime
	print(editor_data["birth_date"])	
	
	# editor_data["birth_date"] = datetime.strptime(editor_data["birth_date"], '%Y-%m-%dT%H:%M')
	# editor_data["member_since"] = datetime.strptime(editor_data["member_since"], '%Y-%m-%dT%H:%M')
	# editor_data["email_confirm_date"] = datetime.strptime(editor_data["email_confirm_date"], '%Y-%m-%dT%H:%M')
	# editor_data["last_updated"] = datetime.strptime(editor_data["last_updated"], '%Y-%m-%dT%H:%M')
	# editor_data["last_login_date"] = datetime.strptime(editor_data["last_login_date"], '%Y-%m-%dT%H:%M')
	
	# https://stackoverflow.com/questions/33224068/how-convert-datetime-local-to-datetime-in-python/33224436

	temp = editor_data["birth_date"]
	editor_data["birth_date"] = datetime.datetime(*[int(v) for v in temp.replace('T', '-').replace(':', '-').split('-')])

	temp = editor_data["member_since"]
	editor_data["member_since"] = datetime.datetime(*[int(v) for v in temp.replace('T', '-').replace(':', '-').split('-')])

	temp = editor_data["email_confirm_date"]
	editor_data["email_confirm_date"] = datetime.datetime(*[int(v) for v in temp.replace('T', '-').replace(':', '-').split('-')])

	temp = editor_data["last_updated"]
	editor_data["last_updated"] = datetime.datetime(*[int(v) for v in temp.replace('T', '-').replace(':', '-').split('-')])

	temp = editor_data["last_login_date"]
	temp = editor_data["last_login_date"] = datetime.datetime(*[int(v) for v in temp.replace('T', '-').replace(':', '-').split('-')])
	
	editor_data = dict(editor_data)
	if(editor_data["area"]  is ''):
		editor_data["area"] = None
	if(editor_data["bio"]  is ''):
		editor_data["bio"] = None
	preprocess_editor_data = preprocess_editor(editor_data)
	
	preprocess_editor_data = np.array([preprocess_editor_data])
	predict_data = {
		"main_input": np.array(preprocess_editor_data[:,1:10]),#.reshape(1,9),
		"email_input": np.array(preprocess_editor_data[:,10]),
		"website_input": np.array(preprocess_editor_data[:,11]),#.reshape(1),
		"bio_input": np.array(preprocess_editor_data[:,12:]),
	}	
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
	return flask.jsonify(prediction)

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading Keras model and Flask starting server..."
		"please wait until server has fully started"))
	load_lodbrok()
	app.run()