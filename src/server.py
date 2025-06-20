import joblib
import numpy as np

from flask import Flask, jsonify

# Creamos el servidor 
app = Flask(__name__)

@app.route("/predict", methods=["GET"])
def predict():
  X_test = np.array([7.59444482058287,7.47955553799868,1.61646318435669,1.53352355957031,0.796666502952576,0.635422587394714,0.36201223731041,0.315963834524155,2.27702665328979])
  predict = model.predict(X_test.reshape(1, -1))
  
  return jsonify({
    "predict": list(predict)
  })

if __name__ == "__main__":
  # Carga del modelo
  model = joblib.load("./models/best_model.pkl")
  
  app.run(port=8080)