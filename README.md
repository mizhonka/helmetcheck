# Helmetcheck

Tällä sovelluksella voit ylläpitää listaa [Helmet-kirjastojen](https://www.helmet.fi/fi-FI) teoksista ja linkeistä, sekä hakea niiden saatavuutta eri kirjastoista.

## Asennusohjeet (Linux)

Sovellus käyttää PostgreSQL-tietokantaa. Ohjeita sen asennukseen [täällä](https://www.postgresql.org/download/).
1. Lataa uusin release (tai kloonaa repositorio) ja navigoi juurikansioon
2. Luo .env -tiedosto ja määritä sen sisältö näin:  
   ```
   DATABASE_URL=<tietokannan-paikallinen-osoite>  
   SECRET_KEY=<salainen-avain>
   ```
3. Asenna riippuvuudet:
   ```
   poetry install
   ```
4. Määritä tietokannan skeema:
   ```
   psql < schema.sql
   ```
5. Aktivoi virtuaaliympäristö:  
   ```
   python3 -m venv venv
   ```
   ```
   source venv/bin/activate
   ```
6. Käynnistä:  
   ```
   flask run
   ```
