from app import *
from app.classify import classify_process

# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    
    # load the function used to classify input images in a *separate*
    # thread than the one used for main classification
    # print("* Starting model service...")
    
    # t = Thread(target=classify_process, args=())
    # t.daemon = True
    # t.start()

    # # start the web server
    print("* Starting web service...")
    app.run(debug=True)
    