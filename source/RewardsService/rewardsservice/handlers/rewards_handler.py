import json
import tornado.web

from pymongo import MongoClient
from tornado.gen import coroutine


class RewardsHandler(tornado.web.RequestHandler):

    @coroutine
    def get(self):
        client = MongoClient("mongodb", 27017)
        db = client["Rewards"]
        rewards = list(db.rewards.find({}, {"_id": 0}))
        self.write(json.dumps(rewards))

# error handler	
    def write_error(self, status_code, **kwargs):	
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:	
            # in debug mode, try to send a traceback	
            self.set_header("Content-Type", "text/plain")	
            for line in traceback.format_exception(*kwargs["exc_info"]):	
                self.write(line)	
            self.finish()	
        else:	
            self.finish(	
                "<html><title>%(code)d: %(message)s</title>"	
                "<body>%(code)d: %(message)s</body></html>"	
                % {"code": status_code, "message": self._reason}	
            )