import modules.utils.paths as path
from utils import Utils
from models import Models


if __name__ == "__main__":
  # Creamos las instancias
  utils = Utils()
  models = Models()
  
  # Carga de los datos
  file_path = path.data_raw_dir("felicidad.csv")
  df = utils.load_from_csv(file_path)
  
  # Split de features y target
  X, y = utils.features_target(df, ["country", "score", "rank"], "score")
  
  # Buscamos el mejor modelo
  models.grid_training(X, y)
  
  print(X.head())