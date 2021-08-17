from flask import Flask, jsonify, request
from flasgger import Swagger
import pickle
import pandas as pd

app = Flask(__name__)
swagger = Swagger(app)


pickle_in = open("model/logreg.pkl","rb")
model=pickle.load(pickle_in)

@app.route('/predict',methods=["Get"])
def predict_class():
    """Predict if Customer would buy the product or not.
    ---
    parameters:
      - name: age
        in: query
        type: number
        required: true
      - name: new_user
        in: query
        type: number
        required: true
      - name: total_pages_visited
        in: query
        type: number
        required: true
    responses:
        500:
          description: Prediction
    """
    age=int(request.args.get("age"))
    new_user=int(request.args.get("new_user"))
    total_pages_visited=int(request.args.get("total_pages_visited"))
    prediction=model.predict([[age,new_user,total_pages_visited]])
    print(prediction[0])
    return "Model prediction is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def prediction_test_file():
    """Prediction on multiple input test file.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
        500:
            description: Test file Prediction
    """
    df_test=pd.read_csv(request.files.get("file"))
    prediction=model.predict(df_test)
    return str(list(prediction))

if __name__=='__main__':
  app.run(debug=True,host='0.0.0.0')

