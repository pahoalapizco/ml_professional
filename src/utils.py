# Tipado
from typing import List, Tuple, Callable
from pathlib import Path

import pandas as pd
import numpy as np
import joblib

class Utils():
  
  def load_from_csv(self, path: Path) -> pd.DataFrame:
    return pd.read_csv(path)
  
  def load_form_mysql(self):
    pass
  
  def features_target(self, dataset: pd.DataFrame, drop_cols: List[str], target: str) -> Tuple[pd.DataFrame, np.array]:
    X = dataset.drop(columns=drop_cols, axis=1)
    y = dataset[target]
    
    return X, y

  def model_export(self, model, score, model_name):
    joblib.dump(model, f"./models/best_model.pkl")
    print(f"El modelo {model_name} con un score de {score:.4f} exportado exitosamente.")


if __name__ == "__main__":
  pass