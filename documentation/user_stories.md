# Käyttötapaukset

Käyttäjä haluaa luoda tunnuksen. Toteutettu. SQL-kysely: 

INSERT INTO account (date_created, date_modified, name, username, role, password) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)

Käyttäjä haluaa kirjautua sisään. Toteutettu. SQL-kysely: 

SELECT account.id, 
    account.date_created, 
    account.date_modified, 
    account.name, 
    account.username, 
    account.role, 
    account.password 
FROM account 
WHERE account.username = ?

Käyttäjä haluaa muokata tietojaan. Ei toteutettu.

Käyttäjä haluaa pystyä tarvittaessa poistamaan profiilinsa. Ei toteutettu.

Käyttäjä haluaa osallistua yhteen tai useampaan kilometrikisan sarjaan. Toteutettu. SQL-kysely:

INSERT INTO sign-up (date_created, date_modified, account_id, league_id)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)

Käyttäjä haluaa merkitä suorituksen. Toteutettu. SQL-kysely:

INSERT INTO event (date_created, date_modified, date, league_id, distance, description, account_id)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)

Käyttäjä haluaa nähdä listan suorituksistaan. Toteutettu. SQL-kysely:

SELECT event.id,
    event.date_created, 
    event.date_modified,
    event.date, 
    event.league_id, 
    event.distance,
    event.description,
    event.account_id 
FROM event 
WHERE event.account_id = ?

Käyttäjä haluaa muokata suorituksiaan. Toteutettu. SQL-kysely:

UPDATE event SET date_modified=CURRENT TIMESTAMP, date=?, league_id=?, distance=?, description=?
WHERE event.id = ?

Käyttäjä haluaa tarvittaessa poistaa suorituksia. Toteutettu. SQL-kysely:

DELETE FROM event WHERE event.id = ?

Käyttäjä haluaa nähdä oman ja muiden sijoitukset eri sarjoissa. Ei toteutettu.

Organisaation vastuuhenkilö haluaa tehdä kaikki asiat, mitä käyttäjäkin. Lisäksi:

Vastuuhenkilö haluaa luoda sarjan. Toteutettu. SQL-kysely:

INSERT INTO league (date_created, date_modified, name, description, organizer_account_id)
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)

Vastuuhenkilö haluaa nähdä luomansa sarjat. Toteutettu. SQL-kysely:

SELECT league.id,
    league.date_created,
    league.date_modified,
    league.name,
    league.description,
    league.organizer_account_id 
FROM league 
WHERE league.organizer_account_id = ?

Organisaation vastuuhenkilö haluaa pystyä tarvittaessa poistamaan sarjan. (Toteutettu, mutta harkinnassa jääkö lopulliseen versioon.)
