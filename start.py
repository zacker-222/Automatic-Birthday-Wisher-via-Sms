import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define, options

from bota import respond
port = int(os.environ.get("PORT", 5000))

class IndexHandler(tornado.web.RequestHandler):
 def get(self):
 	query = self.get_argument('query')
 	reply = respond(query)
 	
 	self.write(str(reply))
 	
      
if __name__ == "__main__":
 tornado.options.parse_command_line()
 app = tornado.web.Application(handlers=[(r"/", IndexHandler)],debug = True)
 http_server = tornado.httpserver.HTTPServer(app)
 http_server.listen(options.port)
 tornado.ioloop.IOLoop.instance().start()