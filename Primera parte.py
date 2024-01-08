import pandas as pd
import json

# se importa el json
with open('Prueba-T-cnica-R5-Kevin-Bonnin/taylor_swift_spotify.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Crea listas para cada columna
disc_numbers = []
duration_ms = []
explicit = []
track_numbers = []
track_popularity = []
track_ids = []
track_names = []
danceability = []
energy = []
key = []
loudness = []
mode = []
speechiness = []
acousticness = []
instrumentalness = []
liveness = []
valence = []
tempo = []
audio_ids = []
time_signature = []
artist_ids = []
artist_names = []
artist_popularity = []
album_ids = []
album_names = []
album_release_dates = []
album_total_tracks = []

# Itera sobre los datos para extraer la información
for album in data['albums']:
    for track in album['tracks']:
        # Extrae la información de las pistas y álbumes
        disc_numbers.append(track['disc_number'])
        duration_ms.append(track['duration_ms'])
        explicit.append(track['explicit'])
        track_numbers.append(track['track_number'])
        track_popularity.append(track['track_popularity'])
        track_ids.append(track['track_id'])
        track_names.append(track['track_name'])
        danceability.append(track['audio_features']['danceability'])
        energy.append(track['audio_features']['energy'])
        key.append(track['audio_features']['key'])
        loudness.append(track['audio_features']['loudness'])
        mode.append(track['audio_features']['mode'])
        speechiness.append(track['audio_features']['speechiness'])
        acousticness.append(track['audio_features']['acousticness'])
        instrumentalness.append(track['audio_features']['instrumentalness'])
        liveness.append(track['audio_features']['liveness'])
        valence.append(track['audio_features']['valence'])
        tempo.append(track['audio_features']['tempo'])
        audio_ids.append(track['audio_features']['id'])
        time_signature.append(track['audio_features']['time_signature'])
        artist_ids.append(data['artist_id'])
        artist_names.append(data['artist_name'])
        artist_popularity.append(data['artist_popularity'])
        album_ids.append(album['album_id'])
        album_names.append(album['album_name'])
        album_release_dates.append(album['album_release_date'])
        album_total_tracks.append(album['album_total_tracks'])

# Crea un DataFrame con las listas
inf = pd.DataFrame({
    'disc_number': disc_numbers,
    'duration_ms': duration_ms,
    'explicit': explicit,
    'track_number': track_numbers,
    'track_popularity': track_popularity,
    'track_id': track_ids,
    'track_name': track_names,
    'audio_features.danceability': danceability,
    'audio_features.energy': energy,
    'audio_features.key': key,
    'audio_features.loudness': loudness,
    'audio_features.mode': mode,
    'audio_features.speechiness': speechiness,
    'audio_features.acousticness': acousticness,
    'audio_features.instrumentalness': instrumentalness,
    'audio_features.liveness': liveness,
    'audio_features.valence': valence,
    'audio_features.tempo': tempo,
    'audio_features.id': audio_ids,
    'audio_features.time_signature': time_signature,
    'artist_id': artist_ids,
    'artist_name': artist_names,
    'artist_popularity': artist_popularity,
    'album_id': album_ids,
    'album_name': album_names,
    'album_release_date': album_release_dates,
    'album_total_tracks': album_total_tracks
})

# Guarda el DataFrame como un archivo CSV
inf.to_csv('dataset_final.csv', index=False)