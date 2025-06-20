import pandas as pd
import numpy as np

# Modulo propio
from utils import Utils

# Modelos a evaluar y optimizar.
from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
# optimizador
from sklearn.model_selection import GridSearchCV


class Models:
  
  def __init__(self):
    self._reg = {
      "SVR": SVR(),
      "GRADIENT": GradientBoostingRegressor()
    }
    
    self._params = {
      "SVR": {
        "kernel": ["linear", "poly", "rbf"],
        "gamma": ["auto", "scale"],
        "C": [1, 5, 10]
      },
      "GRADIENT": {
        "loss": ["absolute_error", "squared_error"],
        "learning_rate": [0.01, 0.05, 0.1]
      }
    }  

  def grid_training(self, X: pd.DataFrame, y: np.array):
    best_score = 999
    best_model = None
    best_model_name = ""
    
    for name, reg in self._reg.items():
      grid_reg = GridSearchCV(reg, self._params[name], cv=5).fit(X, y)
      score = np.abs(grid_reg.best_score_)
      
      if score < best_score:
        best_score = score
        best_model = grid_reg.best_estimator_
        best_model_name = name
    
    utils = Utils()
    utils.model_export(best_model, best_score, best_model_name)
    
if __name__ == "__main__":
  pass