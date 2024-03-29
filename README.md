# Helmetcheck

Tällä sovelluksella voit ylläpitää listaa [Helmet-kirjastojen](https://www.helmet.fi/fi-FI) teoksista ja linkeistä, sekä hakea niiden saatavuutta eri kirjastoista.

![Kuva1](https://github.com/mizhonka/helmetcheck/blob/main/documentation/images/page1.png)
![Kuva2](https://github.com/mizhonka/helmetcheck/blob/main/documentation/images/page2.png)
![Kuva3](https://github.com/mizhonka/helmetcheck/blob/main/documentation/images/page3.png)

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
   psql -d <tietokannan-nimi> < schema.sql
   ```
5. Aktivoi virtuaaliympäristö:
   ```
   poetry shell
   ```
6. Käynnistä:
   ```
   flask run
   ```

## Käyttöohjeet

[Uuden teoksen lisääminen](https://github.com/mizhonka/helmetcheck/blob/main/documentation/manual_new.md)

[Teoksen muokkaaminen ja linkkien lisääminen / poisto](https://github.com/mizhonka/helmetcheck/blob/main/documentation/manual_edit.md)

[Teoksen piilottaminen / näyttäminen](https://github.com/mizhonka/helmetcheck/blob/main/documentation/manual_hiding.md)

[Teoksen poistaminen](https://github.com/mizhonka/helmetcheck/blob/main/documentation/manual_delete.md)

[Haku-toiminto](https://github.com/mizhonka/helmetcheck/blob/main/documentation/manual_search.md)

[Teoksen saatavuuden tarkistaminen](https://github.com/mizhonka/helmetcheck/blob/main/documentation/manual_availability.md)
