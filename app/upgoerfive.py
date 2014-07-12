import os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from forms import QueryForm
from logic import app_logic
import nltk

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
  DATABASE=os.path.join(app.root_path, 'upgoerfive.db'),
  DEBUG=True,
  SECRET_KEY='dev_key',
  USERNAME='admin',
  PASSWORD='hackny'
))

@app.route('/', methods=['GET', 'POST']) 
def index():
  #return 'Hello World!'
  form = QueryForm()
  if request.method == 'POST': 
    return query(request.form['sentence'])
  return render_template('index.html', form=form)

@app.route('/query/<my_string>')
def query(my_string):
  return app_logic(my_string)

def connect_db():
  rv = sqlite3.connect(app.config['DATABASE'])
  rv.row_factory = sqlite3.Row
  return rv

def init_db():
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursour().executescript(f.read())
    db.commit()

def get_db():
  if not hasattr(g, 'sqlite_db'):
    g.sqlite_db = connect_db()
  return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
  if hasattr(g, 'sqlite_db'):
    g.sqlite_db.close()

if __name__ == '__main__':
  app.debug = True
  app.run()
