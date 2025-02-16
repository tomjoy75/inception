# Utilisation d'une image légère avec SQLite
FROM alpine:latest

# Installation de SQLite
RUN apk add --no-cache sqlite

# Création d'un répertoire de travail
WORKDIR /data

# Copie du fichier CSV dans le conteneur
COPY chinook.db /data/chinook.db

# Expose SQLite en ligne de commande par défaut
#ENTRYPOINT ["sqlite3"]

