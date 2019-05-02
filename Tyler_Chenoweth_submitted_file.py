# Tyler Chenoweth
# 4/30/19
# Interview Parsing Question

# I used a guide on python web scaping from this webisite:
# https://first-web-scraper.readthedocs.io/en/latest/
# as well as a few bits and pieces of python references from https://www.w3schools.com/

import requests
from BeautifulSoup import BeautifulSoup
import os
import urllib2
import re

def startProgram():
	for i in range(5):
		print("")

	os.system("clear")

def findLink(url):

	lookingFor = "historical-inflation-rates/"
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		if link.get('href') == (url + lookingFor):
			return url+link.get('href')

	return ""

def addSpaces(n):

	numSpace = 1;
	
	if len(n) == 3:
		print "  |  ",
	elif len(n) == 4:
		print "  | ",
	else:
		print "  |",

def printTableLines():

	print " ",
	for i in range(14):
		print ("+--------"),

	print "+"

def printTable(values):

	count = 0
	maxCellSize = 5
	rowSize = 14

	printTableLines()

	for i in values:
		addSpaces(i)

		print i,
		count += 1

		# go to next line
		if(count%rowSize == 0):
			print "  |"
			printTableLines()

def getMonth(n):
	months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]	
	return months[n]

def main():
	#original url
	url = "http://www.usinflationcalculator.com/inflation/"

	# get url for historical inflation
	url = findLink(url)

	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.tbody
	count = 1

	values = []

	for row in table.findAll("tr"):

		for year in row.findAll("th"):
			values.append(year.text)

		for cell in row.findAll("td"):
			count += 1
			if cell.text == "&nbsp;":
				values.append("    ")
			else:
				values.append(cell.text)

	sMonth, eMonth = "Jan", "Jan"
	sYear, eYear = "1914", "1914"

	# find end month and year
	count = 0
	for i in values:
		if count%14 == 0:
			eYear = i
		if i == "    ":
			eMonth = getMonth(count%14-1)
			break

		count += 1
	
	print "  On this page, annual inflation..."
	print "  This page contains data from ",sMonth, " ",sYear, " to ", eMonth, " ",eYear
	print ""

	printTable(values)
	
# non-function code	
startProgram()
main()
