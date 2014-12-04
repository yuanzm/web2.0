#!/usr/bin/env python
# coding=utf-8

from file import readContentFromFile 

class questionInfo:
	def __init__(self, votes="0", answers="0",state="回答", views="0", name=" ", time=" ", title=" ", tags=" "):
		self.votes = votes
		self.answers = answers
		self.state = state
		self.views = views
		self.name = name
		self.time = time
		self.title = title
		self.tags = tags
	def infoString(self):
		infoString = self.votes + ';' + self.answers + ';' + self.state + ';' +self.views + ';' + self.name + ';' + self.time + ';' + self.title + ';' + self.tags + '\n'
		return infoString

def LoadQuestionsFromTxt(path):
	allLines = readContentFromFile(path)
	allQuestions = []
	for line in allLines:
		if len(line) > 1:
			infos = line.split(';')
			info = questionInfo(infos[0], infos[1], infos[2], infos[3], infos[4],infos[5],infos[6],infos[7])
			allQuestions.append(info)
	return allQuestions