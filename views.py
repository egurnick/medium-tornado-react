from tornado.web import RequestHandler


class HelloWorld(RequestHandler):
    """Print 'Hello, world!' as the response body."""

    def get(self):
        """Handle a GET request for saying Hello World!."""
        self.write("Hello, world!")


class MainHandler(RequestHandler):
    def get(self):
        self.set_status(200)
        self.set_header("Content-Type", "text/html")
        with open("./static/dist/index.html", "r") as f:
            self.write(f.read())

