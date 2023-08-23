from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)




#_____________________________________________ INDEX

@app.route('/')
def index():
    return render_template("index.html")

#__________________________________________ DASHBOARD

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    
    logged_user = User.get_by_id({'id':session['user_id']})
    users =User.get_all()
    return render_template("dashboard.html", user = logged_user)
@app.route('/users/create', methods=['POST'])
def register():
    # Get The FORM data from the front-end
    print(request.form)
    #VALIDATE the form  DATA
        #- if data is valid 
    if User.validate(request.form):

        # 1 Secure password = Hash using bcrypt
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
            'password':pw_hash
        }

        # 2 Create the new user
        user_id = User.create(data) # return from create to follow USER
        session['user_id'] = user_id
        return redirect('/dashboard')
    #- If data not valid
    return redirect('/')

@app.route('/login', methods =['POST'])
def login():
    # 1 Get user by Email !
    user = User.get_by_email({'email':request.form['email']})
    # - If user DONT exist : error and message  > redirect 
    if not user:
        flash("Invalid Email / Password", "login")
        return redirect('/')
    # - If user exist : check password 
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email / Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/users/create', methods=['POST'])
def add_user():
    print(request.form)
    if User.validate(request.form):
        data= {
            **request.form,
            'user_id':session['user_id']
        }
        User.create(data)
        return redirect('/dashboard')
    return redirect('/users/new')





#_____________________________________________ LOGOUT
@app.route('/logout', methods =['POST'])
def logout():
    session.clear()
    return redirect('/')
    
@app.route('/users/<int:user_id>/show')
def one_user(user_id):
    user= User.get_by_id({'id':user_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template("show_user.html",user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.get_by_id({'id':user_id})
    user = User.get_by_id({'id':session['user_id']})
    return render_template("edit_user.html", user=user)

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    
    data = {
        **request.form,
        'id':user_id
    }
    User.update(data)
    
    return redirect('/dashboard')


@app.route('/users/<int:user_id>/destroy')
def destroy(user_id):
    User.delete({'id':user_id})
    return redirect('/dashboard')

