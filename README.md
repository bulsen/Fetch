###Fetch.

this is a very very preliminary search engine for indexing slides and pdfs.

## steps

first run install_script.sh which will install the depedencies

then paste your files to the `slides/` folder. after that run `sweep.py` file, this process may take a while. after all these steps you can do searchs by running `server.py`.

note: if you want to run it on another port, just change the port value on the last line of `server.py.

##depedencies

python 2.7
Mongodb
Flask
python-pptx
