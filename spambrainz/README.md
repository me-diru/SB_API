## Functioning of requests:

1) There are two request codes namely classify_request.py and train_request.py for /predict and /train respectively.
2) The classify_request.py sents a spam editor account to be classified by the lodbrok model running in the backend. The command ```python classify_request.py```  gives the following output: 

![](static/images/classify_request.png)
3) The train_request.py sents a spam editor accounts along with **verdict** given by SpamNinja as spam or not. The command ```python train_request.py```  gives the following output: 

![](static/images/train_request.png)

More details regarding the API functioning is written [here](app/README.md).