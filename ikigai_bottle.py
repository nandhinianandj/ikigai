# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : ikigai_bottle.py
#
#* Purpose :
#
#* Creation Date : 22-01-2024
#
#* Last Modified : Monday 22 January 2024 11:41:22 PM
#
#* Created By : Yaay Nands
#_._._._._._._._._._._._._._._._._._._._._.#
from bottle import route, run, template
from ikigai_diagram import draw

set_labels = ['Get Paid For', 'World Needs', 'You Love', 'You are good at']
data= {'Get Paid For': ['Systems Design', 'Coding/SW_Engineering'],
       'World Needs':  ['Writing','Connecting With People','Play Bass Guitar', 'Teach Philosophy Alignment',
                        'Systems Design', 'Coding/SW_Engineering', 'Making People Laugh'],
       'You Love':   ['Play badminton', 'Running', 'Reading', 'Dance', 'Making People Laugh'],
       'You are Good at':   ['Write Poetry','Teach Philosophy Alignment', 'Systems Design', 'Connecting with people',
           'Writing', 'Coding/SW_Engineering', 'Dance', 'Making People Laugh','Reading','Running',
           'Play Badminton']
       }

@route('/ikigai')
def index():
    ikigai_dict = request.cookies.get('data', data)
    img_path = draw(data)
    return template('<b>Hello Friend, here is your Ikigai</b>!  <img src={{path}} alt="Ikigai Diagram" width="500"height="600"> ', path=path)

@route('/image/<path>')
def image(path):
    return static_file(path, root='.', mimetype='image/jpg')
run(host='localhost', port=8080)

