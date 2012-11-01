Post 2 Rest Flexget plugin 0.1.0
================================
Post your entry data as json payload to a rest url endpoint. (couchdb anyone?)

Install
-------
Drop `P2RFlexget.py` in `~/.flexget/plugins`

Flexget info
------------
- It is an output plugin (`on_task_output`)
- All entry field are added but quality
- Additional keys from data field are added to the payload
- Timestamp (human readable and seconds since epoch) are added to payload in post2rest key

Configuration example
---------------------
```
tasks:
  my task:
    rss: http://...
    accept_all:yes
    post2rest:
      url: 'http://.../..'
      data: #optional, entry will be extended with this data
        additional_data: 'one more'
```

Payload example
---------------
```
{
   "_id": "21b4ee6acae7dd560242b252f8008927",
   "_rev": "1-df3010dbd3ecb65b7f258eafa08576e1",
   "accepted_by": "accept_all",
   "task": "test P2R",
   "subtitle": true,
   "title": "Name.Of.The.Series.S01E01.XviD-FlexGet",
   "url": "http://localhost/mock/z0koMotGz5OBNdsXC2kmkBJFjQM6A",
   "series_name": "Name Of The Series",
   "original_url": "http://localhost/mock/z0koMotGz5OBNdsXC2kmkBJFjQM6A",
   "series_season": 1,
   "series_episode": 1,
   "post2rest": {
       "timestamp": 1351802766.637263,
       "time": "Thu Nov  1 21:46:06 2012"
   }
}
```

