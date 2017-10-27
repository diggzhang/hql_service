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
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
"appVersion": "4.1.0",
    "eventKey": "clickVideoPause",
    "userId": "58514b50feefebf505954408",
    "os": "android"
}'
#output 15 items as json array or "[]"
"[{\"id\": \"59f06c25c31b763e2d62d3ed\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06a42c31b763e2d5de11d\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06a54c31b763e2d5e0e76\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06a72c31b763e2d5e5a0e\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06b74c31b763e2d60f970\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f067d2c31b763e2d57d24c\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06862c31b763e2d593074\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f068f2c31b763e2d5a9be9\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06ce5c31b763e2d64df50\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06cf4c31b763e2d6511c1\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06943c31b763e2d5b63cb\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06964c31b763e2d5bb24e\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}, {\"id\": \"59f06ac3c31b763e2d5f2393\", \"event_key\": \"clickVideoPause\", \"category\": \"video\", \"platform\": \"app\", \"os\": \"android\", \"device\": \"A00000704911E4\", \"d_app_version\": \"4.1.0\", \"u_user\": \"58514b50feefebf505954408\"}]"
```
