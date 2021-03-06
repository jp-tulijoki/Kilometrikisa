# Tietokantakuvaus

Tietokanta on normalisoitu ja tietokantataulut ovat funktionaalisesti riippuvaisia toisistaan. Tämä edesauttaa tiedon eheyttä, mutta asettaa reunaehdon, että sarjoja järjestävät vastuuhenkilöt toimivat vastuullisesti. Käytännössä vastuuhenkilön vastuu ilmenee siinä, että hänen poistaessaan luomansa sarjan tai kokokäyttäjätunnuksensa, poistetaan tietokannasta myös sarjaan liittyvät ilmoittautumiset ja tapahtumat. Sovellustasolla tähän on varauduttu siten, että muiden taulujen tietoihin vaikuttavia poistoja tehtäessä sovellus varoittaa poiston vaikutuksesta. Käytännön tasolla oletetaan myös, että sarjan vastuuhenkilö tekee sarjan nimeen ja kuvaukseen ainoastaan sellaisia muokkauksia, jotka eivät merkittävästi muuta sarjan luonnetta (esim. muuta juoksusarjaa kävelysarjaksi). 

Tietokantaan liittyvät käyttäjäroolit ja autorisointi on pyritty pitämään kevyenä, koska kyse on matalan kynnyksen
epävirallisesta toiminnasta. Käytännössä tämä tarkoittaa, että käyttäjä voi vapaasti ottaa vastuuhenkilön roolin tai luopua
siitä, kun ei enää sitä tarvitse. Autorisointi liittyy ainoastaan sarjojen järjestämiseen. Muuten jokainen vastaa omaan 
käyttäjätiliinsä liittyvistä toiminnoista, eikä sovelluksessa ole admin-roolia.

Hakutoimintojen nopeuttamiseksi viiteavaimet on indeksoitu. Sovelluksen luonteesta johtuen haut tehdään lähinnä avaimilla, eikä vapaata tekstihakua ole, joten muita indeksejä ei ole. 

Sovellus käyttää paikallisesta SQLite-tietokantajärjestelmää ja Herokussa PostgreSQL-tietokantajärjestelmää.

Tietokantasovelluksen kieli on englanti, mutta käyttöohjeet ja dokumentaatio on suomeksi. 

## Tietokantakaavio

![Tietokantakaavio](https://github.com/jp-tulijoki/Kilometrikisa/blob/master/documentation/database_diagram.jpg)

## CREATE TABLE -lauseet

```sql
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	role VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);
```
```sql
CREATE TABLE league (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR NOT NULL, 
	description VARCHAR NOT NULL, 
	organizer_account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (name), 
	FOREIGN KEY(organizer_account_id) REFERENCES account (id) ON DELETE CASCADE
);
CREATE INDEX ix_league_organizer_account_id ON league (organizer_account_id);
```
```sql
CREATE TABLE sign_up (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	account_id INTEGER NOT NULL, 
	league_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE, 
	FOREIGN KEY(league_id) REFERENCES league (id) ON DELETE CASCADE
);
CREATE INDEX ix_sign_up_account_id ON sign_up (account_id);
CREATE INDEX ix_sign_up_league_id ON sign_up (league_id);
```
```sql
CREATE TABLE event (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	date DATE NOT NULL, 
	league_id INTEGER NOT NULL, 
	distance INTEGER NOT NULL, 
	description VARCHAR, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(league_id) REFERENCES league (id) ON DELETE CASCADE, 
	FOREIGN KEY(account_id) REFERENCES account (id) ON DELETE CASCADE
);
CREATE INDEX ix_event_account_id ON event (account_id);
CREATE INDEX ix_event_league_id ON event (league_id);
```

## Jatkokehitysideoita

- tietokannan laajentaminen siten, että se mahdollistaa myös joukkueiden välisen kilpailun
- aikaleimojen hyödyntäminen (esim. ilmoittautumisten ja  sarjojen luontien päiväysten tarkastelu)
- sarjojen arkistoinnin mahdollistaminen
- sarjojen organisoinnin luovuttaminen toiselle käyttäjälle
