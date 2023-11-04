import requests
import os

EDAMAM_API_KEY = os.getenv('EDAMAM_API_KEY')
EDAMAM_APP_ID = os.getenv('EDAMAM_APP_ID')

def get_ingredients(product_name):
    url = "https://api.edamam.com/api/food-database/v2/parser"

    params = {
        'app_id': EDAMAM_APP_ID,
        'app_key': EDAMAM_API_KEY,
        'ingr': product_name
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        
        for hint in data.get('hints', []):
            food_data = hint.get('food', {})
            if 'foodContentsLabel' in food_data:
                product_label = food_data.get('label', '')
                ingredients = food_data.get('foodContentsLabel', '')
                image_url = food_data.get('image', '')
                return f"Product: {product_label}\nIngredients: {ingredients}\nImage: {image_url}"

        return "No results found for ingredients."
    else:
        return f"Failed to retrieve data: {response.status_code}, {response.reason}"