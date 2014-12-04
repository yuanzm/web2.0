#!/usr/bin/env python
# coding=utf-8

def readContentFromFile(path):
	fs = open(path)
	allLines = fs.readlines()
	fs.close()
	return allLines

def writeToFile(path, content):
	fs = open(path, "a")
	fs.write(content)
	fs.close()