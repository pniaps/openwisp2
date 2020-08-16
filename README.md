# Developent installation  

### Create and activate vitual environment

This will install and use all python modules in `env` folder instead of system folder.

```shell script
$ mkdir openwisp2
$ cd openwisp2
$ python3 -mvenv --copies env
$ . ./env/bin/activate
(env)$ 
```

### Download and initialize project 

```
(env)$ git clone git@github.com:pniaps/openwisp2.git .
(env)$ ./install-dev.sh
```

This script install all required dependencies and creates a default administrator with username and password `admin`, and also sets the `Shared secret` for the default organization `------SECRET------`

### Run server
Start Redis and InfluxDB using docker-compose:
```shell script
docker-compose up -d redis influxdb
```
Run celery and celery-beat with the following commands (separate terminal windows are needed):
```shell script
celery -A openwisp2 worker -l info
celery -A openwisp2 beat -l info
```
Launch development server:
```shell script
./manage.py runserver 0.0.0.0:8000
```
You can access the admin interface at http://127.0.0.1:8000/admin/.
