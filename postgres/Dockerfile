FROM postgres:latest

# Setze Umgebungsvariablen für den Datenbanknamen, Benutzer und das Passwort
ENV POSTGRES_DB=keycloak
ENV POSTGRES_USER=cloak
ENV POSTGRES_PASSWORD=cloak

# Kopiere eventuell benötigte Skripte oder Konfigurationen
COPY ./init.sql /docker-entrypoint-initdb.d/

# Der Standardport von PostgreSQL
EXPOSE 5432