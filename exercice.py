#!/usr/bin/env python
# -*- coding: utf-8 -*-

def check_brackets(text, brackets):
	pile =[]
	result = True
	for n in text:
		if n in brackets:
			if brackets.index(n)%2 == 0: pile.append(n) # n pair donc ouverture
			elif brackets.index(n)%2 != 0: # n impair donc fermeture
				if pile[-1] == brackets[brackets.index(n)-1]: pile.pop(-1)
				else: result = False
	if pile != []: result = False
	return result

def remove_comments(full_text, comment_start, comment_end):
	if comment_start not in full_text and comment_end not in full_text:
		return full_text
	elif comment_start in full_text and comment_end in full_text:
		start = full_text.index(comment_start)
		end = full_text.index(comment_end) + len(comment_end)
		return full_text[:start] + full_text[end:]
	else: return None

def get_tag_prefix(text, opening_tags, closing_tags):
	for n in range(len(opening_tags)):
		if opening_tags[n] in text: 
			if text.index(opening_tags[n]) == 0: return(opening_tags[n],None)
	for n in range(len(closing_tags)):
		if closing_tags[n] in text: 
			if text.index(closing_tags[n]) == 0: return(None,closing_tags[n])
	return(None, None)
	
	

def check_tags(full_text, tag_names, comment_tags): ### ABANDONNÉ À REFAIRE
	coorect = True
	for n in tag_names:
		if "<"+n+">" in full_text:
			if "</"+n+">" in full_text and full_text.index("</"+n+">") > full_text.index("<"+n+">"): correct = True
			else: correct = False
	return correct


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}", "[", "]")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	dead_parrot = "Hello, /*oh brave new */world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print(remove_comments(dead_parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

