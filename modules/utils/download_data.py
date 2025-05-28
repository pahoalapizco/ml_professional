import os

import kagglehub
from kagglehub import KaggleDatasetAdapter

import modules.utils.paths as p

def is_downloaded(file_path):
  exists = os.path.isfile(p.data_raw_dir(file_path))
  if exists: print(f"Dataset {file_path} is already downloaded")
  return exists

def from_kaggle(handle, file_path):
  if not is_downloaded(file_path):
  
    # Load the latest version
    df = kagglehub.load_dataset(
      KaggleDatasetAdapter.PANDAS,
      handle,
      file_path,
    )

    df.to_csv(p.data_raw_dir(file_path))
    print(f"Dataset {file_path} was downloaded successfully")


if __name__ == "__main__":
  pass