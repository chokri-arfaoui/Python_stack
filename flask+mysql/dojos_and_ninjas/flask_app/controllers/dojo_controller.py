from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import dojo_model

@app.route('/')
def index():
    all_dojos = dojo_model.Dojo.get_all()
    return render_template("index.html", dojos = all_dojos)

@app.route('/create_dojo', methods=['post'])
def create():
    dojo_model.Dojo.create(request.form)
    return redirect('/')

@app.route('/dojos/<int:id>')
def one_dojo(id):
    one_dojo = dojo_model.Dojo.dojo_with_its_ninjas_by_id({'id':id})
    return render_template('on_dojo.html', one_dojo= one_dojo)