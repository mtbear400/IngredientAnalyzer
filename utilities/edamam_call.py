import requests
from settings import EDAMAM_API_KEY, EDAMAM_APP_ID

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
        
        # Check each food entry for 'foodContentsLabel'.
        for hint in data.get('hints', []):
            food_data = hint.get('food', {})
            if 'foodContentsLabel' in food_data:
                # When found, return the label and ingredients.
                product_label = food_data.get('label', '')
                ingredients = food_data.get('foodContentsLabel', '')
                return product_label, ingredients
        
        # If loop completes with no return, it means 'foodContentsLabel' was not found in any entry.
        print("No results found for ingredients.")
        return None, None

    else:
        print(f"Failed to retrieve data: {response.status_code}, {response.reason}")
        return None, None
# Example usage
product_name = "cocoa puffs"  # replace with the actual product name you're querying
product_label, ingredients = get_ingredients(product_name)
if product_label and ingredients:
    print(f"Product: {product_label}\nIngredients: {ingredients}")
else:
    print("Could not fetch ingredients.")
