import pandas as pd
from fastapi import FastAPI
import uvicorn

inf = pd.read_csv('dataset_final.csv')

# Para ver las canciones y albums de los artistas
