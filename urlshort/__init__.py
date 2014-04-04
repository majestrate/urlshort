from flask import Flask

app = Flask(__name__)
from urlshort import views
from urlshort import config
app.config.from_object('urlshort.config')
