from os import path

def replaceProjectPath(path):
	f = open("config.ini", "w")
	lines = f.readlines()
	for line in lines:
		if "project" in line:
			line = "project = \"{}\"".format(path)
		f.write(line + "\n")

	f.close()

def replaceHost(host):
	replaceFileContent("tex/scripts/tag_up.py", "http://stacks.math.columbia.edu/tag/", host)

def bootstrapXyJax:
	searchString = 'MathJax.Ajax.loadComplete("[MathJax]/extensions/TeX/xypic.js");'
	replaceString = 'MathJax.Ajax.loadComplete("/js/XyJax/extensions/TeX/xypic.js");'
	replaceFileContent("js/XyJax/extensions/TeX/xypic.js", searchString, replaceString)

def replaceFileContent(path, searchString, replaceString):
	f = open(path, "w")
	content = f.read()
	content.replace(searchString, replaceString)
	f.write(content)
	f.close()


host = argv[1]
currentpath = os.path.dirname(sys.argv[0])

replaceProjectPath(join(currentpath, 'stacks-website'))
replaceHost(host)
bootstrapXyJax()
