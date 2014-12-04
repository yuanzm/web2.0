#!/usr/bin/env python 
# coding=utf-8

from file import readContentFromFile

def searchUserFromTxt(path, userName, userPassword):
	allLines = readContentFromFile(path)
	for line in allLines:
		userInfo = line.split(',')
		name = userInfo[0]
		password = userInfo[1].replace('\n','')
		if userName == name:
			if userPassword == password:
				return True
	return False

def userSignAble(path, userName):
	allLines = readContentFromFile(path)
	for line in allLines:
		userInfo = line.split(',')
		name = userInfo[0]
		if userName == name:
			return False
	return True
