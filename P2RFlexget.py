import requests
import json
import time

class Post2RestFlexget(object):

    def on_process_start(self,feed):
        self.config = feed.config['post2rest']

    def validator(self):
        from flexget import validator
        d = validator.factory('dict')
        d.accept('url', key='url')
        d.accept('dict', key='data').accept_any_key('any')
        return d

    @staticmethod
    def serialize(o):
        if not isinstance(o, (str, unicode, int, long, float, bool) ):
           return None
        else:
           return o

    def on_task_output(self,task):
        for entry in task.entries:
            entry_dict = dict(entry)
            if 'data' in self.config:
                entry_dict.update(self.config['data'])
            entry_dict['post2rest']={
                'time': time.asctime(),
                'timestamp': time.time()
            }
            data=json.dumps(entry_dict,default=Post2RestFlexget.serialize)
            headers = {'content-type': 'application/json'}
            requests.post(self.config['url'], data=data, headers=headers)

try:
    from flexget.plugin import register_plugin
    register_plugin(Post2RestFlexget, 'post2rest')
except:
    pass
