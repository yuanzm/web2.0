#!/usr/bin/env python
# coding=utf-8

import os.path
import tornado.web

from user import searchUserFromTxt
from user import userSignAble
from file import writeToFile
from question import LoadQuestionsFromTxt
from question import questionInfo

class HTTP404Error(tornado.web.ErrorHandler):
    def initialize(self):
        tornado.web.ErrorHandler.initialize(self, 404)

    def prepare(self):
        self.render('404.html')

class IndexHandler(tornado.web.RequestHandler):
	def get(self):
		name = self.get_secure_cookie("user")
		title = "SegmentFault"
		userPath = os.path.join(os.path.dirname(__file__), "../static/questionData/questions.txt")
		questions = LoadQuestionsFromTxt(userPath)
		self.render('index.html', title=title, questions=questions, name=name)

class SignupHandler(tornado.web.RequestHandler):
	def get(self):
		name = self.get_secure_cookie("user")
		if name:
			self.redirect('/')
		else:
			title = "注册-SegmentFault"
			buttonText = "注册"
			formText = "注册新账号"
			self.render('signinup.html', title=title, buttonText=buttonText, formText=formText)
	def post(self):
		name = self.get_argument('name', None)
		password = self.get_argument('password', None)
		userPath = os.path.join(os.path.dirname(__file__), "../static/userData/users.txt")
		if name != None and len(name) > 0:
			if password != None and len(password) > 0:
				userInfo = name + ',' + password + '\n'
				if userSignAble(userPath, name):
					writeToFile(userPath, userInfo)
					self.set_secure_cookie("user", name)
					self.redirect('/')
				else:
					self.redirect('/signup')	
			else:
				self.redirect('/signup')
		else:
			self.redirect('/signup')

class LoginHandler(tornado.web.RequestHandler):
	def get(self):
		name = self.get_secure_cookie("user")
		if name:
			self.redirect('/')
		else:
			title = "登录 - SegmentFault"
			buttonText = "登录"
			formText = "登录到SegmentFault"
			self.render('signinup.html', title=title, buttonText=buttonText, formText=formText)
	def post(self):
		name = self.get_argument('name', None)
		password = self.get_argument('password', None)
		userPath = os.path.join(os.path.dirname(__file__), "../static/userData/users.txt")
		if searchUserFromTxt(userPath, name, password):
			self.set_secure_cookie("user", name)
			self.redirect('/')
			return
		self.redirect('/login')
		
class LogoutHandler(tornado.web.RequestHandler):
	def get(self):
		self.set_secure_cookie("user", '')
		self.redirect('/')

class AskHandler(tornado.web.RequestHandler):
	def get(self):
		name = self.get_secure_cookie("user")
		if not name:
			self.redirect('/login')
			return
		else:
			title = "提出问题 - SegmentFault"
			self.render('ask.html', title=title, name=name)
	def post(self):
		name = self.get_secure_cookie("user")
		title = self.get_argument('title', None)
		tags = self.get_argument('tags', None)
		content = self.get_argument('content', None)

		question = questionInfo()
		question.name = name
		question.title = title
		question.tags = tags
		question.time = "刚刚"
		questionPath = os.path.join(os.path.dirname(__file__), "../static/questionData/questions.txt")
		writeToFile(questionPath, question.infoString())	
		self.redirect('/')
