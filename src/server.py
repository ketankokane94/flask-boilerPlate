from flask import Flask
import simplejson as json

app = Flask('First Server')

@app.route('/getMenuItems')
def hello():
    items = [
    {"label":'Bio',"icon":'fa-user'},
    {"label": 'Stats', "icon": 'fa-bar-chart',"url":'#/csrScreening'},
    {"label": 'Calendar', "icon": 'fa-calendar',"url":'#/gcarsSearch'}
    ]
    return json.dumps(items)

# export FLASK_ENV = development
# flask run