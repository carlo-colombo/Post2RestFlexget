Post 2 Rest Flexget plugin 0.1.0
================================
Post your entry data as json payload to a rest url endpoint. (couchdb anyone?)

Install
-------
Drop `P2RFlexget.py` in `~/.flexget/plugins`

Flexget info
------------
It is an output plugin (`on_task_output`)


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