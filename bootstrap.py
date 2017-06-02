import sys
from os.path import join, dirname, realpath
import re

def bootstrapXyJax():
	searchString = "MathJax.Ajax.loadComplete(\"[MathJax]/extensions/TeX/xypic.js\");"
	replaceString = "MathJax.Ajax.loadComplete(\"/js/XyJax/extensions/TeX/xypic.js\");"
	replaceFileContent("js/XyJax/extensions/TeX/xypic.js", searchString, replaceString)

def replacePDFLATEXCommand():
	replaceFileContentRegex('tex/tags/Makefile', r"PDFLATEX := .*", "PDFLATEX := pdflatex")

def replaceFileContent(relpath, searchString, replaceString):
	path = join(bootstrapRoot, relpath)
	print(path)
	f = open(path, "r")
	content = f.read()
	f.close()
	content = content.replace(searchString, replaceString)
	f = open(path, "w")	
	f.write(content)
	f.close()

def replaceFileContentRegex(relpath, regex, replaceString):
	path = join(bootstrapRoot, relpath)
	f = open(path, "r")
	content = f.read()
	f.close()
	content = re.sub(regex, replaceString, content)
	f = open(path, "w")	
	f.write(content)
	f.close()


if len(sys.argv) == 2:
	host = sys.argv[1]
else:
	host = "localhost/tag"

currentpath = dirname(sys.argv[0])
bootstrapRoot = dirname(realpath('__file__'))

replaceFileContent("config.ini", "project = \"\"", "project = \"stacks-website\"")
replaceFileContent("config.ini", "database = \"\"", "database = \"database/stacks.sqlite\"")
replaceFileContent("tex/scripts/tag_up.py", "http://stacks.math.columbia.edu/tag/", host)
bootstrapXyJax()
