from flask import render_template,request,redirect,session,flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

#secure the route 
@app.route('/recipes/new')
def new_recipe():
    if 'user_id' not in session:#to secure
        return redirect('/')
    return render_template('new_recipe.html')

#create recipe
@app.route('/recipes/create',methods=['POST'])
def add_recipe():
    if not Recipe.validate_recipe(request.form):# check if recipe existing
        return redirect('/recipes/new')
    data={
        **request.form,
        'user_id':session['user_id']
    }  
    Recipe.create_recipe(data)
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:recipe_id>')
def edit(recipe_id):
    if 'user_id' not in session:#to secure
        return redirect('/')
    recipe = Recipe.get_by_id_recipe({'id':recipe_id})
    return render_template('edit_recipe.html',recipe=recipe)

@app.route('/recipes/update',methods=['POST'])
def update():
    if not Recipe.validate_recipe(request.form):# check if recipe existing
        return redirect('/recipes/new')
    #data={'name':request.form['name'], ...}

    Recipe.update_recipe(request.form)
    return redirect('/dashboard')



@app.route('/recipes/delete/<int:recipe_id>')
def delete(recipe_id):
    if 'user_id' not in session:#to secure
        return redirect('/')
    Recipe.delete_recipe({'id':recipe_id})
    return redirect('/dashboard')


@app.route('/recipes/show/<int:recipe_id>')
def show(recipe_id):
    recipe=Recipe.get_by_id_recipe({'id':recipe_id})
    log = User.get_by_id({'id':session['user_id']})
    return render_template('show_recipe.html',recipe=recipe,log=log)



