from app import *
from app.classify import classify_process

if __name__ == "__main__":    
   
    # start the web server
    print("* Starting web service...")
    app.run(debug=True)
    