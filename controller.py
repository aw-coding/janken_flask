from flask import render_template #, request
from app import app

from src.player import *

@app.route('/')
def index():
    return render_template('index.html', title ='Home ')