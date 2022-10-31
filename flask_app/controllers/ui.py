from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

@app.route('/')
def home():
    return redirect('/dojos')

@app.route('/dojos')
def readall():
    return render_template('Dojos.html', dojos = Dojo.get_all_dojos())

@app.route('/create_dojo', methods = ['POST'])
def f_create_dojo():
    Dojo.insert_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojos(id):
    data = {
        "id":id
    }
    return render_template('DojoShow.html', dojo = Dojo.get_dojos_with_ninjas(data))
    #have to learn how to join things from thursday lecture

@app.route('/ninjas')
def ninjas():
    return render_template('Ninjas.html', dojos = Dojo.get_all_dojos())

@app.route('/create_ninja', methods = ['POST'])
def f_create_ninja():
    Ninja.insert_ninja(request.form)
    return redirect('/')

#ask for TA help on how to edit something that comes from a left join table JINJA syntax stuff

# @app.route('/edit-ninja/<int:id>')
# def r_edit_ninja(id):
#     data = {
#         "id":id
#     }
#     return render_template('Edit_Ninja.html', dojo = Dojo.get_dojos_with_ninjas(data))

# @app.route('/edit_ninja', methods = ['POST'])
# def f_edit_ninja():
#     Ninja.update_one(request.form)
#     return redirect('/dojos/<int>')

# @app.route ('/ninjas/delete/<int:id>')
# def delete_this_ninja(id):
#     data = {
#         "id":id
#     }
#     Ninja.delete_user(data)
#     return redirect('/')