
from flask import render_template,request
from . import main
from ..requests import search_recipe
from .forms import IngredientsForm
from flask_login import login_required,current_user


@main.route('/')
def index():
    return render_template('hero.html')

@main.route('/recipe_list', methods=['GET','POST'])
@login_required
def give_recipe():

    form = IngredientsForm()
    search_result = []
    if form.validate_on_submit():
        search_result = search_recipe(form.ingredient1.data, form.ingredient2.data,form.ingredient3.data)
        
    return render_template('search.html', form = form, recipe_result = search_result)

