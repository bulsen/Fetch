
<h1>Fetch</h1>

is a basic search and show engine for my personal usage. this thing was written in python with non-oop aspect. 
there are two segments in this repo; a converter which needs libreoffice and the webUI powered by flask. this is a very preliminary and very robust application. this is for personal usage, maybe for education; to prevent people write bad code like mine.


<h2>Dependencies:</h2>

	python-pptx				# for converter
	flask					# love this badboy
	pymongo					# python mongodb wrapper
	libxml					# for python-pptx <converter>
	libreoffice				# for converting jobs
	pdf2svg 				# for creating the static slides
	cowsay					# yes it's very juvenile, i know and still love it

<h2>Anathomy:</h2>

	static/				# flask related for webUI
	templates/			# flask related
	pptxdude/			# backup for pptxs
	slides/				# where all starts
	svgdude/			# static svgs of converted slides for flask related show things

	mockapp.py 			# main flask script
	sweep.sh 			# for all converting jobs /powered by cowsay


<h2>Notes:</h2>

i couldn't run it on my vps, so be carefull. this is just for linux.

encoding errors:
there might be some problems with mongo. you can handle that 

	export LC_ALL=C

it just works. by the way whole code coded with utf-8 support, so there shouldn't be any encoding problems.

changing the database names:

	@slides/fetch_converter.py -> @48th line there is a abstarction
	@mockapp.py 		-> @12nd line there is the same abstraction

you should change both of them.

and also in some segments there are turkish part which i intended to write how this things runs for my buddies. but main code is documented in english