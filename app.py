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

app = Flask(__name__)

def get_data(stock):
    api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
    session = requests.Session()
    session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
    raw_data = session.get(api_url)
    data=raw_data.json()
    column_names=data['column_names']
    ndata=data['data']
    df = pd.DataFrame(ndata, columns=column_names)
    return df

def plot_close(stock):
    df=get_data(stock)
    close=pd.to_numeric(df['Close'])
    date=pd.to_datetime(df['Date'])
    p = figure(tools="pan,wheel_zoom,box_zoom,reset",
              title='Data from Quandle WIKI set',
              x_axis_label='Date',
              x_axis_type='datetime',
              y_axis_label='Closing price',
              x_range=(datetime.now()-timedelta(days=31),datetime.now()))
    p.line(date, close, line_width=2, legend=stock)
    return p

@app.route('/', methods=['GET'])
def post():
    return render_template("post.html")

@app.route('/graph', methods=['POST'])#output
def stock():
#	stock = request.args.get("stock")
        stock=str(request.form['stock'])

	# Create the plot
	plot = plot_close(stock)
		
	# Embed plot into HTML via Flask Render
	script, div = components(plot)
	return render_template("graph.html", script=script, div=div)

# With debug=True, Flask server will auto-reload 
# when there are code changes
if __name__ == '__main__':
	app.run(port=5000, debug=True)

