from pathlib import Path

import pandas as pd


def lector_de_csv(ruta_csv: Path):
    
    archivo = pd.read_csv(ruta_csv, encoding="utf-8")
    
    print(archivo)
    
lector_de_csv("fase-00\\fase-00.csv")
    
    