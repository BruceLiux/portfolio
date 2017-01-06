#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os

import config
import controllers

from flask import Flask, render_template


# Initialize Flask app with the template folder address
app = Flask(__name__,template_folder='templates')

# Register the controllers
app.register_blueprint(controllers.main)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404
