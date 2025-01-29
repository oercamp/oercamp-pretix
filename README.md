
## (nova) Pretix  

### Tech stack

Pretix uses following tech-stack:

* Gunicorn - webserver for Python/Django apps
* ~~MySQL~~ PostgreSQL
* Python / Django Framework
* Production runs a nginx webserver as a proxy.

## Installation for local Development

* Create ``src/pretix.cfg``from ``src/pretix.example.cfg`` and edit it to your needs.


* Create ``.env``from ``.env.example`` and edit it.


* `docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d`


* inside src directory: `make npminstall`


* `./bin/pretix compress`


* Run ``sudo ./bin/build`` to build the project and the database.

* Please check the (nova) pretalx readme. The environment setup works in a similar way.


* Please check the official documentation for more infos: [Pretix Docker ](https://docs.pretix.eu/en/latest/admin/installation/docker_smallscale.html)

### Creating a superuser

You can create a super-user interactively inside the docker container, which is also
one of the first things to do after installing pretix:

* connect to your docker container: ``docker exec -it pretix /bin/bash``
* create one with ``python3 /pretix/src/manage.py createsuperuser``


### MailPit

A mailcatcher, Mailpit, is already configured for the local dev-environment.
Access it at http://localhost:8025/


### Tips for developing

* Use ``./bin/build`` to build the project after changes, and to
  re-generate static files, translations, migrations etc.


## Installation for production

* Installation is similar to local development instructions, but with following notable changes:


* Edit ``src/pretix.cfg`` and ``.env`` for production (see above).


* Include the ``docker-composer.prod.yml`` and exclude the ``docker-composer.dev.yml``
  when running docker-compose. Example:
  ``docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d``


* Configure a reverse-proxy for better security and to handle TLS.
  Please check ``reverse-proxy-examples/nginx`` inside the (nova) pretalx (!) project,
  where you will find a copy/example of a current nginx configuration.

#### Setting up cronjobs on production (important for pretix API):

* See (nova) pretalx instructions first.  
Add these instructions to (currently root) crontab:

```
45 * * * * cd /sites/oercamp/oercamp-pretix && docker compose exec -u pretixuser -T pretix python3 /pretix/src/manage.py runperiodic 2>&1
```

## Live deployment procedure

* SSH to the live server, change to workdir ``cd /sites/oercamp/oercamp-pretix/`` and run ``./bin/deploy-prod``


* the deployment-script restarts the docker containers to flush the cash. This is suboptimal.  
See (nova) pretalx on how to do it better (by restarting gunicorn workers).  
A similar solution could be implemented in pretix at some point. 


#### Programming Tips

* Log file `.docker/volumes/data/logs/pretix.log` 

Please also see the (nova) pretalx Readme for more infos & tips. 
Both projects are similar, because
they are based on the same framework (Django) and were coded by the same people. 
