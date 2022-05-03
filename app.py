import os

from flask import Flask, abort, redirect, render_template, request

from src.models import db
from src.repos import cat_repo_singleton

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/cats')
def get_all_cats():
    cats = cat_repo_singleton.get_all_cats()
    return render_template('all_cats.html', cats=cats)


@app.get('/cats/<int:cat_id>')
def get_cat(cat_id: int):
    cat = cat_repo_singleton.get_cat(cat_id)
    if cat is None:
        abort(404)
    return render_template('single_cat.html', cat=cat)


@app.get('/cats/new')
def get_new_cat_page():
    return render_template('create_cat.html')


@app.post('/cats')
def create_cat():
    name = request.form.get('name', '')
    breed = request.form.get('breed', '')
    num_legs = request.form.get('numLegs')
    if name == '' or breed == '':
        abort(400)
    cat_repo_singleton.create_cat(name, breed, num_legs)
    return redirect('/cats')


@app.post('/cats/<int:cat_id>/delete')
def delete_cat(cat_id: int):
    deleted_cat = cat_repo_singleton.delete_cat(cat_id)
    if deleted_cat is None:
        abort(404)
    return redirect(f'/cats')
