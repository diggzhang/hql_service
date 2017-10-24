## Install Requirements

```shell
$ python setup.py install
```

## Start Service

```shell
$ python run.py
# output
* Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 176-141-767
```

## API Usage

```shell
# ping-pong test
$ curl -X GET http://localhost:9000/
{
    "ping": "pong"
}

# POST /hql
curl -X POST \
  http://localhost:9000/hql \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"hql": "select * from default.guojie_vip limit 3"
}'
```
