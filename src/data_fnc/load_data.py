import pandas as pd
from ucimlrepo import fetch_ucirepo
from pathlib import Path

def cargar_data_uci(identificador):
    """
    Descarga y prepara un dataset desde UCI

    Argumentos:
        identificador (int)L Numero ID del dataset en UCI
    """
    try:
        # Obtener los datos desde la libreria
        dataset = fetch_ucirepo(id=identificador)

        # Extraer los DataFrames de forma limpia
        X = dataset.data.features
        y = dataset.data.targets
        ids = dataset.data.ids

        # Concatenar todo en un solo dataframe
        df = pd.concat([ids, X, y], axis=1)

        # Guardar 
        carpeta_destino = Path("data/raw")
        carpeta_destino.mkdir(parents=True, exist_ok=True)
        ruta_archivo = carpeta_destino / f"dataset_{identificador}.csv"

        df.to_csv(ruta_archivo, index=False)
        print(f"Dataset cargado y guardado en: {ruta_archivo}")

        return df
    
    except Exception as e:
        print(f"Ocurrio un error al descargar el dataset: {e}")
        return None



