
## NOVA Custom Pretix  

### Local Development Setup

* `docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d`
* inside src directory: `make npminstall`
* `./bin/pretix compress`
