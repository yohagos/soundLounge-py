CREATE DATABASE keycloak;
CREATE USER cloak WITH ENCRYPTED PASSWORD 'cloak';
GRANT ALL PRIVILEGES ON DATABASE keycloak TO cloak;