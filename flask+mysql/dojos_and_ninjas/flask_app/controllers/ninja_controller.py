from flask import request, redirect, render_template
from flask_app import app
from flask_app.models import ninja_model, dojo_model

# Display route
@app.route('/ninjas')
def new_ninja():
    dojos = dojo_model.Dojo.get_all()
    return render_template('ninjas.html', dojos = dojos)

# Action route
@app.route('/create_ninja', methods=['post'])
def create_ninja():
    ninja_model.Ninja.create(request.form)
    return redirect('/')