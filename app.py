from flask import Flask, request

# Create a Flask application instance
app = Flask(__name__)

# Initialize an empty list to store friend data
model = []

# Route to get all friends
@app.get('/estudiante')
def get_estudiante():
    # Return the list of friends
    return model

# Route to get a specific friend by ID
@app.get('/estudiante/<int:id>')
def get_un_estudiante(id):
    # Check if the ID is within the list's bounds
    if id < 0 or id >= len(model):
        return {"error": "estudiante no encontrado"}, 404  # Handle non-existent friend

    # Return the friend data and a 200 status code
    return model[id], 200

# Route to create a new friend
@app.post('/estudiante')
def create_estudiante():
    # Get the friend data from the request body (assuming JSON)
    request_data = request.get_json()

    # Validate the request data (optional)
    if not request_data or "nombre" not in request_data:
        return {"error": "Invalid request data"}, 400  # Handle bad request

    # Create a new friend object with ID and name
    new_friend = {
        "nombre": request_data["nombre"], 
        "apellido": request_data["apellido"],
        "materia": request_data["materia"],
        "id": len(model)
        }

    # Add the new friend to the model list
    model.append(new_friend)

    # Return the created friend data and a 201 status code
    return new_friend, 201

# Route to delete a friend
@app.delete('/estudiante/<int:id>')
def delete_estudiante(id):
    # Check if the ID is within the list's bounds
    if id < 0 or id >= len(model):
         return {"error": "Invalid request data"}, 404  

    # Remove the friend from the list
    del model[id]

    # Return a success message and a 200 status code
    return {"success": "Dato eliminado con exito"}, 200