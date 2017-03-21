import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os
from tornado.options import define, options

from bota import respond
port = int(os.environ.get("PORT", 5000))

      


 
class MainHandler(tornado.web.RequestHandler):
    def get(self):
    	
        self.write("Hello world ")
 
def main():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()
 
if __name__ == "__main__":
    main()