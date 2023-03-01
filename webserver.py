#! /usr/bin/python3

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from tornado.web import Application
from tornado.log import enable_pretty_logging

from tornado.web import RequestHandler

from views import MainHandler, HelloWorld

import os

# Start webserver

def main():
    """Construct and serve the tornado application."""
    define('port', default=8000, help='port to listen on')
    enable_pretty_logging()

    app = Application(
        [
            ('/', MainHandler),
            ('/helloworld', HelloWorld)
        ],
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print('Listening on http://localhost:%i' % options.port)
    IOLoop.current().start()


if __name__ == "__main__":
    print("Webserver Starting...")
    main()
    print("Webserve End")

