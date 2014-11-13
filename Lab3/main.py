#coding:utf-8
import os.path
import random
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("ports", default=8000, help="Run on the given port ", type=int)

class song:
	def __init__(self, name, mainName, size):
		self.name = name
		self.mainName = mainName
		self.initialSize = size
		if size < 1024:
			self.size = "%d b" % size
		elif size < 1024 * 1024:
			self.size = "%d Kb" % (size / 1024)
		else:
			self.size = "%d Mb" % (size/(1024*1024))

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		playList = self.get_argument("playList", None)
		back = self.get_argument("back", None)
		bySize = self.get_argument("bySize", None)
		shuffle = self.get_argument("shuffle", None)

		path = os.path.join(os.path.dirname(__file__), "static/songs")
		allSongs = getDirFileMessage(path, ".mp3")
		allTxt = getDirFileMessage(path, ".m3u")
		isBackShow = False
		isPlayList = False

		if back is not None:
			return self.redirect("/")
		if playList is not None:
			fs = open(os.path.join(path, playList + '.m3u'))
			songList = fs.read().splitlines()
			fs.close()
			playSong = []
			for song in songList:
				if song[0] != "#":
					for aSong in allSongs:
						if aSong.name == song:
							playSong.append(aSong)
			allSongs = playSong
			allTxt = []
			isBackShow = True
			isPlayList = playList
		if bySize is not None:
			allSongs.sort(lambda x, y: -cmp(x.initialSize, y.initialSize))
		if shuffle is not None:
			random.shuffle(allSongs)


		self.render('music.html', allSongs=allSongs,
            allTxt=allTxt, isBackShow=isBackShow, isPlayList=isPlayList)

def getDirFileMessage(path, filetype):
	allFile = []
	fileList = os.listdir(path)

	for oneFile in fileList:
		fileMessage = []
		fileType = os.path.splitext(path + '/' + oneFile)[1]
		if fileType == filetype:
			size = os.path.getsize(path + '/' + oneFile)
			name = oneFile
			mainName = oneFile.split(".")[0]
			aSong = song(name, mainName, size)
			allFile.append(aSong)
	return allFile

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[(r'/', IndexHandler)],
		template_path=os.path.join(os.path.dirname(__file__), "template"),
		static_path=os.path.join(os.path.dirname(__file__), "static"),
		debug=True
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.ports)
	tornado.ioloop.IOLoop.instance().start()
