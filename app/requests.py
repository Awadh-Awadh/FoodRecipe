# import urllib.request,json
from .models import Recipe
from app.main.forms import IngredientsForm
import requests as rq

api_key = None
search_recipe_url = None
recipe_result = None

def configure_request(app):
    global api_key,search_recipe_url
    api_key = app.config['RECIPE_API_KEY']
    search_recipe_url = app.config['RECIPE_URL']

def search_recipe(ingredient1,ingredient2,ingredient3):
    search_recipe = search_recipe_url.format(api_key,ingredient1,ingredient2,ingredient3)
    print(search_recipe)
    
    with rq.get(search_recipe) as data:
        recipe_data= data.json()
        recipe_response =  recipe_data
    
    
    return recipe_response
        
        # with urllib.request.urlopen(search_recipe) as data:
    #     recipe_data= data.read()
    #     recipe_response = json.loads(recipe_data)
        
        # if recipe_response['missedIngredients']: