# Fastfeed

Een feed-collector, jaja. Weer een feed collector.

* Sla de items niet op, maar cache de feed voor een kwartier of een half uur.
  * De oudere items lees ik toch niet terug
* Toon alleen de meest recente twee of drie items
  * Als er nieuwe items zijn ga ik toch naar de website toe om de anderen
    te bekijken.
    
## Development

Start een python omgeving waarin de applicatie kan draaien.
```
$ . ./bin/init.sh
```

## Techniek

* Framework
  * FastAPI?
  * Masonite?
  * Django?
* Redis
* request

## Pagina's

### Registreren

* Een pagina met invoeroptie voor email en wachtwoord.
* Sla de gegevens op.
  * In een gewoon bestandje in json formaat.
  * Onder een hash van email en wachtwoord.

### Inloggen

* Authenticatie volgens een hash van gebruikersnaam en wachtwoord.
* Start een sessie
  * Laadt gegevens om de voorpagina te vullen.


### Landingspagina

* Toon van alle geregistreerde feeds de meest recente items.
* Sla het feed-resultaat op in een redis store voor 30 minuten o.i.d.
* Toon een lijstje met alle websites
  * Als een website geen artikelen heeft kan je er toch 
    gemakkelijk bij.
* Inloggen verplicht

### Account

* Beheer de feeds.
  * Feed toevoegen.
  * Feed uitzetten.
  * Feed verwijderen.
* Sta wachtwoord verversen toe,
  * Invoer oude wachtwoord.
  * Bestandje hernoemen.
* Inloggen verplicht.



## Interessante bronnen

* Meerdere redis instanties op de mac:
  * https://jeremy.wordpress.com/2012/07/05/multiple-redis-instances-on-mac-os-x-with-homebrew/
* Meerdere redis instanties op ubuntu server:
  * 