# Fastfeed

Een feed-collector, jaja. Weer een feed collector.

* Bewaar alleen de meest recente artikelen van alle feeds.
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

* FastAPI
* Redis
* Ninja2

## Pagina's

### Landingspagina

* Toon van alle geregistreerde feeds de meest recente items.
* Toon een lijstje met alle websites
  * Als een website geen artikelen heeft kan je er toch 
    gemakkelijk bij.

### Clear cache

* Pagina om de cache te clearen. Het on the fly laden van
  artikelen duurt toch wel lang :-(


## Interessante bronnen

* Meerdere redis instanties op de mac:
  * https://jeremy.wordpress.com/2012/07/05/multiple-redis-instances-on-mac-os-x-with-homebrew/
* Meerdere redis instanties op ubuntu server:
  * ...