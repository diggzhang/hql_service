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

# POST /hql input hql query output hive calculation result
curl -X POST \
  http://localhost:9000/hql \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"hql": "select * from default.guojie_vip limit 3"
}'
# return
{
    "hive_results": [
        [
            "date",
            "user",
            "start",
            "end",
            "week",
            "month"
        ],
        [
            "2017-08-29",
            "57bc376bfe3a33e93de8be35",
            "2017-08-29",
            "2018-03-03",
            "2017-08-28",
            "2017-08-01"
        ],
        [
            "2017-08-29",
            "57e71b362ad556bd3e075bca",
            "2018-02-04",
            "2018-08-09",
            "2017-08-28",
            "2017-08-01"
        ]
    ]
}


# POST /event query eventKey
curl -X POST \
  http://localhost:9000/event \
  -H 'content-type: application/json' \
  -d '{
  "appVersion": "4.1.0",
  "eventKey": "clickVideoResume",
  "userId": "58d91f0586fd470********0"
}'
# output
{
    "fieldsList": [
        "id",
        "event_key",
        "category",
        "platform",
        "os",
        "device",
        "d_app_version",
        "u_user"
    ],
    "results": [
        [
            "59eeccc3c31b763e2d321afd",
            "clickVideoResume",
            "video",
            "app",
            "android",
            "864410030261255",
            "4.1.0",
            "58d91f0586fd***********0"
        ],
        [
            "59eeccd5c31b763e2d323b7d",
            "clickVideoResume",
            "video",
            "app",
            "android",
            "864410030261255",
            "4.1.0",
            "58d91f0586fd4705f5dc58b0"
        ],
        [
            "59eeccf3c31b7**********2",
            "clickVideoResume",
            "video",
            "app",
            "android",
            "864410030261255",
            "4.1.0",
            "58d91f0586fd***********0"
        ]
    ]
}

```
