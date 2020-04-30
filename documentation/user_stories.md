# Käyttäjätarinat

Käyttäjä haluaa luoda tunnuksen. Toteutettu. SQL-kysely: 

```sql
INSERT INTO account (date_created, date_modified, name, username, role, password) 
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

Käyttäjä haluaa kirjautua sisään. Toteutettu. SQL-kysely: 

```sql
SELECT account.id,
    account.date_created,
    account.date_modified,
    account.name,
    account.username,
    account.role,
    account.password
FROM account 
WHERE account.username = ?
```

Käyttäjä haluaa muokata tietojaan. Toteutettu. SQL-kysely:

```sql
UPDATE account SET date_modified=CURRENT TIMESTAMP, name=?, role=?
WHERE account.id=?
````

Käyttäjä haluaa pystyä tarvittaessa poistamaan profiilinsa. Toteutettu. SQL-kysely:

```sql
DELETE FROM account WHERE account.id=?`
```
Samalla poistuu kaikki käyttäjän ilmoittautumiset ja suoritukset:

```sql
DELETE FROM sign_up WHERE sign_up.account_id = account.id

DELETE FROM event WHERE event.league_id = sign_up.league_id AND Event.account_id = account.id
```

Käyttäjä haluaa osallistua yhteen tai useampaan kilometrikisan sarjaan. Toteutettu. SQL-kysely:

```sql
INSERT INTO sign-up (date_created, date_modified, account_id, league_id)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)`
```

Käyttäjä haluaa tarvittaessa poistaa ilmoittautumisen. Toteutettu. SQL-kysely:

```sql
DELETE FROM sign_up WHERE sign_up.id=?`
```

Samalla poistuu kaikki käyttäjän kyseisen sarjan suoritukset:

```sql
DELETE FROM event WHERE event.league_id = sign_up.league_id AND Event.account_id = ?
```

Käyttäjä haluaa merkitä suorituksen. Toteutettu. SQL-kysely:

```sql
INSERT INTO event (date_created, date_modified, date, league_id, distance, description, account_id)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?)
```

Käyttäjä haluaa nähdä listan suorituksistaan eri sarjoissa. Toteutettu. SQL-kysely:

```sql
SELECT event.id,
    event.date_created,
    event.date_modified,
    event.date,
    event.league_id,
    event.distance,
    event.description,
    event.account_id 
FROM event 
WHERE event.account_id = ? AND event.league_id = ?
```` 

Käyttäjä haluaa muokata suorituksiaan. Toteutettu. SQL-kysely:

```sql
UPDATE event SET date_modified=CURRENT TIMESTAMP, date=?, league_id=?, distance=?, description=?
WHERE event.id = ?
````

Käyttäjä haluaa tarvittaessa poistaa suorituksia. Toteutettu. SQL-kysely:

```sql
DELETE FROM event WHERE event.id = ?
````

Käyttäjä haluaa nähdä oman ja muiden sijoitukset eri sarjoissa. Toteutettu. SQL-kysely:

```sql
SELECT Account.name,
    Sum(Event.distance) as total_distance 
FROM Account 
LEFT JOIN Event ON Event.account_id = Account.id 
WHERE Event.league_id = ? 
GROUP BY Account.name 
ORDER BY total_distance DESC
````

Käyttäjä haluaa nähdä, missä kolmessa sarjassa on eniten ilmoittautumisia. Toteutettu. SQL-kysely:

```sql
SELECT League.name,
    Count(Sign_up.league_id) as sign_ups 
FROM League 
LEFT JOIN Sign_up ON Sign_up.league_id = League.id 
GROUP BY League.name 
ORDER BY sign_ups DESC LIMIT 3
````

**Organisaation vastuuhenkilö haluaa tehdä kaikki asiat, mitä käyttäjäkin. Lisäksi:**

Vastuuhenkilö haluaa luoda sarjan. Toteutettu. SQL-kysely:

```sql
INSERT INTO league (date_created, date_modified, name, description, organizer_account_id)
    VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
````

Vastuuhenkilö haluaa nähdä luomansa sarjat. Toteutettu. SQL-kysely:

```sql
SELECT league.id,
    league.date_created,
    league.date_modified,
    league.name,
    league.description,
    league.organizer_account_id 
FROM league 
WHERE league.organizer_account_id = ?
````

Organisaation vastuuhenkilö haluaa pystyä tarvittaessa poistamaan sarjan. Toteutettu. SQL-kysely:

```sql
DELETE FROM league WHERE league.id = ?
```

Samalla poistuu kaikki kyseisen sarjan ilmoittautumiset ja suoritukset:

```sql
DELETE FROM sign_up WHERE sign_up.league_id = league.id

DELETE FROM event WHERE event.league_id = league.id
```

Organisaation vastuuhenkilö haluaa pystyä tarvittaessa poistamaan käyttäjätunnuksensa kuten kuvattu käyttäjän kohdalla. Samalla poistuu kaikki käyttäjän luomat sarjat sekä sarjoihin liitetyt ilmoittautumiset sekä suoritukset (eli ominaisuutta on käytettävä erittäin harkiten):

```sql
DELETE FROM league WHERE league_organizer_id = account.id

DELETE FROM sign_up WHERE sign_up.league_id = league.id

DELETE FROM event WHERE event.league_id = league.id
```
