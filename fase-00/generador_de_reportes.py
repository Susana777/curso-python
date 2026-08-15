from pathlib import Path

import pandas as pd


def generador_de_reporte(datos_csv: Path):
    '''Recibe un archivo csv con ventas e ingresos y genera un reporte de texto con el
    total de ventas y el total de ingresos'''
    
    datos = pd.read_csv(datos_csv, encoding="utf-8")
    
    total_de_ventas = datos["Ventas"].sum()
    total_de_ingresos = datos["Ingresos"].sum()
    
    with open("fase-00\\reporte.txt", "a") as archivo_reporte:
        
        archivo_reporte.write("---REPORTE DE VENTAS---\n")
        archivo_reporte.write(f"Total de ventas: {total_de_ventas}\n")
        archivo_reporte.write(f"Total de ingresos: ${total_de_ingresos}\n")

generador_de_reporte("fase-00\\datos.csv")     