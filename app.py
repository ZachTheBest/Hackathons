import ollama
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Function to interact with Ollama API
def get_response(statement):
    response = ollama.chat(
        model="llama3", 
        messages=[{
            "role": "user",
            "content": statement
        }]
    )
    return response["message"]["content"]

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        # Safely get form inputs
        mood = request.form.get('mood', '').strip()
        cuisine = request.form.get('cuisine', '').strip()
        ingredients = request.form.get('ingredients', '').strip()
        dishes = request.form.get('dishes', '').strip()
        meal_of_the_day = request.form.get('meal_of_the_day', '').strip()
        dietary_restrictions = request.form.get('dietaryRestrictions', '').strip()
        additional_restrictions = request.form.get('additionalRestrictions', '').strip() if dietary_restrictions in ['allergies', 'others'] else ''
        recipe_type = request.form.get('recipeType', '').strip()
        cost = request.form.get('cost', '').strip()
        num_people = request.form.get('numPeople', '1').strip()
        spice_level = request.form.get('spiceLevel', '5').strip()

        # Build the prompt
        statement = f"""
        This user is feeling {mood} and is looking for a meal suggestion for {meal_of_the_day}.
        Dietary restrictions: {dietary_restrictions} {f"({additional_restrictions})" if additional_restrictions else ''}.
        Preferred cuisine: {cuisine or "Any"}.
        Ingredients available: {ingredients or "N/A"}.
        Desired dish types: {dishes or "Any"}.
        They want something that is around {spice_level}/10 on the spice scale.
        This recipe should serve {num_people} people and have a cost around {cost or "N/A"}.
        They prefer a recipe type like: {recipe_type or "Any"}.

        Generate a recipe that fits these needs. Include a dish name, ingredients, and simple steps. 
        Keep it under 100 characters if possible.
        """

        try:
            response = get_response(statement)
            result = response
        except Exception as e:
            result = f"An error occurred: {str(e)}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
