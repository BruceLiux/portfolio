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


# Debug
# if __name__ == '__main__':
#     app.run(host=config.env['host'], port=config.env['port'], debug=True)