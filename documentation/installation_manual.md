# Asennusohje

## Asennus paikallisesti

1. Lataa sovellus esimerkiksi komentorivikomennolla `git clone https://github.com/jp-tulijoki/Kilometrikisa`.
2. Ota käyttöön python-virtuaaliympäristö suorittamalla komento python3 -m venv venv siinä hakemistossa, johon latasit sovelluksen.
3. Aktivoi virtuaaliympäristö komennolla `source venv/bin/activate`.
4. Asenna sovelluksen tarvitsemat riippuvuudet komennolla `pip install -r requirements.txt`.
5. Käynnistä sovellus komennolla `python run.py`.
6. Avaa sovellus selaimessa. Osoite näkyy komentorivillä sovelluksen käynnistämisen jälkeen.

## Asennus Herokuun

1. Luo tunnus [herokuun](https://www.heroku.com/).
2. Lisää sovellukselle web-palvelin, jota Heroku osaa käyttää esim. komennolla `pip install gunicorn`.
3. Jäädytä riippuvuudet komennolla `pip freeze requirements.txt`. Poista requirements.txt:stä tarvittaessa rivi `pkg-resources==0.0.0`.
4. Lisää projektille Procfile-tiedosto: `echo "web: gunicorn --preload --workers 1 application:app" > Procfile`.
5. Luo sovellukselle paikka Herokuun: `heroku create (uniikki sovelluksen nimi)`.
6. Lisää versionhallintaan tieto Herokusta: `git remote add heroku https://git.heroku.com/(sovelluksen nimi).git`
7. Lähetä projekti Herokuun: `git add .`, `git commit -m "(viesti)"`, `git push heroku master`.

### PostgreSQL:n käyttöönotto Herokussa

1. Asenna ajuri: `pip install psycopg2`.
2. Luo uusi versio requirements.txt:stä: `pip freeze | grep -v pkg-resources > requirements.txt`.
3. Luo ympäristömuuttuja Herokuun: `heroku config:set HEROKU=1`.
4. Ota käyttöön tietokanta: `heroku addons:add heroku-postgresql:hobby-dev`.
