import pandas as pd
from fastapi import FastAPI
import uvicorn

inf = pd.read_csv('dataset_final.csv')

app = FastAPI()

# Para poder ver los datos de una canción en especifico

@app.get("/canciones/{Cancion}/ver los datos de una canción en especifico.")
def canciones( Cancion: str ):
    informacion = inf[inf['track_name'] == Cancion]
    return informacion