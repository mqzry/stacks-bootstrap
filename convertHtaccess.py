

def writeRewriteRulesToCaddyFile(base, rules, filepath):
	f = open(filepath, "a")
	f.write("\n")
	for rule in rules:
		caddyRule = getCaddyRule(base, rule)
		f.write(caddyRule)
		f.write("\n")

def getCaddyRule(base, rule):
	formatString = """rewrite {0} {{
	r  {1}
	to {2}
}}"""
	print rule
	return formatString.format(base, rule['reg'], rule['repl'])

htaccess = open("stacks-website/.htaccess", 'r')
lines = htaccess.readlines()

rewriteRules = []
base = ""

for line in lines:
	line = line.strip()
	if "RewriteBase" in line:
		base = line.split(" ")[1]
	if "RewriteRule" in line:
		lineParts = line.split(' ');
		regex = lineParts[1]
		replacement = lineParts[2]
		for i in range(0,100):
			searchTerm = "${}".format(i)
			replacement = replacement.replace(searchTerm, "{" + str(i) + "}")
		rule = {}
		rule['reg'] = regex
		rule['repl'] = replacement
		rewriteRules.append(rule)


writeRewriteRulesToCaddyFile(base, rewriteRules, "webserver/Caddyfile")