import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class info:
	def __init__(self, name, section, card):
		self.name = name
		self.section = section
		self.card = card

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('buyagrade.html')

class infoHandler(tornado.web.RequestHandler):
	def post(self):
		name = self.get_argument("name", "yuanzm")
		section = self.get_argument("section", "MA")
		card = self.get_argument("card", "1234123412341234")
		infoMessage = info(name, section, card)
		self.render('sucker.html', infoMessage=infoMessage)

if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r'/', IndexHandler),(r'/sucker', infoHandler)],
		template_path=os.path.join(os.path.dirname(__file__), "template"),
		static_path=os.path.join(os.path.dirname(__file__), "static"),autoescape = None,debug = True
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()