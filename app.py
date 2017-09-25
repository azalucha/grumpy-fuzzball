from flask import Flask, render_template, request, redirect
import pandas as pd
import bokeh
import dill
import jinja2
import pip
import simplejson as json
import requests
#import json
from bokeh.plotting import figure, show
from bokeh.embed import components 
from datetime import datetime,timedelta
#import datetime as dt

app = Flask(__name__)

def get_data(stock):
     x=42
#    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
#    session = requests.Session()
#    session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
#    raw_data = session.get(api_url)
#    data = raw_data.json()
#    column_names=data['column_names']
#    ndata=data['data']
#    df = pd.DataFrame(ndata, columns=column_names)
#    return df
     return x

def plot_close(stock):
#    df=get_data(stock)
     get_data(stock)
#    close=pd.to_numeric(df['Close'])
#    date=pd.to_datetime(df['Date'])
#    datelist = date.tolist()
#    p = figure(tools="pan,wheel_zoom,box_zoom,reset",
#              title='Data from Quandle WIKI set',
#              x_axis_label='Date',
#              x_axis_type='datetime',
#              y_axis_label='Closing price')
##              x_range=(dt.datetime.now()-dt.timedelta(days=31),dt.datetime.now()))
#    p.line(date, close, line_width=2, legend=stock)
    x=range(10)
    y=range(10)
    p = figure(tools="pan,wheel_zoom,box_zoom,reset",
              title='Data from Quandle WIKI set',
              x_axis_label='Date',
              y_axis_label='Closing price')
    p.line(x,y,line_width=2, legend=stock)



    script, div = components(p)
    return script, div

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/graph')#output
def graph():
#	stock = request.args.get("stock")
#        stock=str(request.form['stock'])
        stock = request.args.get('stock', '').upper()

	# Create the plot
	script, div = plot_close(stock)
		
	# Embed plot into HTML via Flask Render
	return render_template("graph.html", script=script, div=div)

# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
	app.run(port=33507, debug=True)

