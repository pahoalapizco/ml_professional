import os
import subprocess

def download_data(url: str, file_name: str, file_path: str, drop_zip: bool = True):
    """
    Descarga un dataset desde Kaggle utilizando curl y lo descomprime con unzip.

    Parámetros:
    url (str): URL de descarga del dataset de Kaggle
    file_name (str): Nombre del archivo zip a guardar
    file_path (str): Ruta donde se almacenará el dataset
    """
    # Crear el directorio si no existe
    os.makedirs(file_path, exist_ok=True)

    # Ruta completa al archivo
    full_path = os.path.join(file_path, file_name)

    # Comando para descargar con curl
    curl_cmd = ["curl", "-L", url, "-o", full_path]

    # Ejecutar curl
    try:
        print(f"Descargando dataset desde {url}...")
        subprocess.run(curl_cmd, check=True)
        print("Descarga completada.")
    except subprocess.CalledProcessError as e:
        print("Error al descargar el archivo:", e)
        return

    # Comando para descomprimir con unzip
    unzip_cmd = ["unzip", "-o", full_path, "-d", file_path]

    # Ejecutar unzip
    try:
        print(f"Descomprimiendo archivo en {file_path}...")
        subprocess.run(unzip_cmd, check=True)
        print("Descompresión completada.")
    except subprocess.CalledProcessError as e:
        print("Error al descomprimir el archivo:", e)
        return		

    print("Dataset disponible en:", file_path)

    # Eliminar archivos zip descargados 
    if drop_zip:
      drop_zip_cmd = ["rm", full_path]
      try:
        print(f"Eliminando zip descargados en {file_path}...")
        subprocess.run(drop_zip_cmd, check=True)
        print("Archivo eliminado.")
      except:
        print("Error al eliminar el archivo:", e)
        return

if __name__ == "__main__":
  # Ejemplo de uso:
  download_data(
    url="https://www.kaggle.com/api/v1/datasets/download/unsdsn/world-happiness",
    file_name="world-happiness.zip",
    file_path="../data/raw"
  )