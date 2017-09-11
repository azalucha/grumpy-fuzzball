from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/graph',methods=['GET','POST']')
def graph():
  print('Endless winter')
  return render_template('index.html')

if __name__ == '__main__':
  app.run(port=33507)
