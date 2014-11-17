#coding:utf-8

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		film = self.get_argument("film", "tmnt")
		filepath = os.path.join(os.path.dirname(__file__), "static/" + film)

		info = getInfo(filepath)
		overView = getGeneralOverView(filepath)
		review = getReview(filepath)
		imgPath = film + "/generaloverview.png"

		self.render("movie.html", info=info, overView=overView, review=review, imgPath=imgPath)

def getDirFileMessage(path, fileName, fileType, isBroad):
	fileList = os.listdir(path)
	message = []
	for oneFile in fileList:
		fileText = os.path.splitext(oneFile)
		if isBroad == True:
			if fileName in fileText[0]:
				if fileText[1] == "." + fileType:
					fopen = open(os.path.join(path, oneFile),"r")
					message.append(fopen.readlines())
					fopen.close()
		elif isBroad == False:
			if fileText[0] == fileName:
				if fileText[1] == "." + fileType:
					fopen = open(os.path.join(path, oneFile),"r")
					message = fopen.readlines()
					fopen.close()

	return message

def getInfo(path):
	message = getDirFileMessage(path, "info", "txt", False)
	return message

def getGeneralOverView(path):
	overView = getDirFileMessage(path, "generaloverview", "txt", False)
	return overView

def getReview(path):
	review = getDirFileMessage(path, "review", "txt", True)
	return review

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),autoescape = None,debug = True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()