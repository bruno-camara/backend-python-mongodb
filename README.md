# Backend Project using Python and MongoDB
> Challenge RHOBS

## Challenge
"Ton challenge si tu l'acceptes, est :
1. D'installer une base de données Mongodb
2. D'insérer les données du fichier data.json.codechallenge.janv22.RHOBS.json
3. Répondre aux exercices suivants en écrivant le code python :
       - Compter le nombre de femmes / d'hommes.
       - Écrire une fonction qui renvoie les entreprises de plus de N personnes.
       - Écrire une fonction qui prend en paramètre un métier et qui renvoie la pyramide des âges pour ce métier. "

## Requirements:
- Docker

## How to run:
```bash
# docker build -t backend-python-mongodb .
# docker run backend-python-mongodb
docker run -d -p 27017:27017 --name m1 mongo # in another terminal
python3 ./main.py
docker stop m1 # to stop the container
docker rm m1 # to remove the container
```
> use -i if interactive and -t for a sudo terminal

Or, to run all at once:
```bash
docker compose up -d
```

## MongoDB notation:
- Documents --> Data
- Collection --> Table
- A collection is composed by documents
