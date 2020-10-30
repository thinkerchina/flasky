# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:50:05 2020

@author: thron
"""

from hello import app
from flask import current_app
print(current_app.name)

app_ctx = app.app_context()
app_ctx.push()
print(current_app.name)
app_ctx.pop()