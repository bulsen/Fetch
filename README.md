
<h1>fetchv2</h1>

is a basic search and show engine for my personal usage. this thing was written in python with non-oop aspect. 
there are two segments in this repo; a converter which needs libreoffice and the webUI powered by flask. this is a very preliminary and very robust application. this is for personal usage, maybe for education; to prevent people write bad code like mine.


<h2>dependencies:</h2>

	python-pptx				# for converter
	flask					# love this badboy
	pymongo					# python mongodb wrapper
	libxml					# for python-pptx <converter>
	libreoffice				# for converting jobs
	pdf2svg 				# for creating the static slides
	cowsay					# yes it's very juvenile, i know and still love it

<h2>anathomy:</h2>

	fetchv2/				# main folder

		static/				# flask related for webUI

		templates/			# flask realted

		pptxdude/			# can't remember why this is here <last place of pptx's><think as backup>

		slaytlar/			# can't remember either

		svgdude/			# static svgs of converted slides for flask related show things

		fetch_converter.py 		# the converter
		mockapp.py 			# main flask script
	
		sweep.sh 			# for all converting jobs /powered by cowsay

		readme				# readme file


<h2>notes:</h2>

i couldn't run it on my vps, so be carefull. this is just for linux.

encoding errors:
there might be some problems with mongo. you can handle that 

	export LC_ALL=C

it just works. by the way whole code coded with utf-8 support, so there shouldn't be any encoding problems.

changing the database names:

	@slides/fetch_converter.py -> @48th line there is a abstarction
	@mockapp.py 		-> @12nd line there is the same abstraction

you should change both of them.

