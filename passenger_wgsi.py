#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os

import config
import controllers

from flask import Flask, render_template
# INTERP = os.path.join(os.environ['HOME'], 'newapp.xiangliux.com', 'bin', 'python')
# if sys.executable != INTERP:
#     os.execl(INTERP, INTERP, *sys.argv)
# sys.path.append(os.getcwd())

#sys.path.append('sample')
#from sample import app 


# Initialize Flask app with the template folder address
app = Flask(__name__,template_folder='templates')

# Register the controllers
app.register_blueprint(controllers.main)


if __name__ == '__main__':
    # listen on external IPs
    app.run(host=config.env['host'], port=config.env['port'], debug=True)