# Tietokantakuvaus

Tietokanta on normalisoitu, mikä edesauttaa tiedon eheyttä, mutta asettaa reunaehdon, että sarjoja järjestävät vastuuhenkilöt
toimivat vastuullisesti. Käytännössä vastuuhenkilön vastuu ilmenee siinä, että hänen poistaessaan luomansa sarjan tai koko
käyttäjätunnuksensa, poistetaan tietokannasta myös sarjaan liittyvät ilmoittautumiset ja tapahtumat.

Tietokantaan liittyvät käyttäjäroolit ja autorisointi on pyritty pitämään kevyenä, koska kyse on matalan kynnyksen
epävirallisesta toiminnasta. Käytännössä tämä tarkoittaa, että käyttäjä voi vapaasti ottaa vastuuhenkilön roolin tai luopua
siitä, kun ei enää sitä tarvitse. Autorisointi liittyy ainoastaan sarjojen järjestämiseen. Muuten jokainen vastaa omaan 
käyttäjätiliinsä liittyvistä toiminnoista, eikä sovelluksessa ole admin-roolia.

Tietokantasovelluksen kieli on englanti, mutta käyttöohjeet ja dokumentaatio on suomeksi.

## Tietokantakaavio

## CREATE TABLE -LAUSEET

## Jatkokehitysideoita

- tietokannan laajentaminen siten, että se mahdollistaa myös joukkueiden välisen kilpailun
- sarjojen arkistoinnin mahdollistaminen
- sarjojen organisoinnin luovuttaminen toiselle käyttäjälle
