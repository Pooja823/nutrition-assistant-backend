from flask import Flask
from src.routes.auth import auth  # Import the auth Blueprint

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(auth)

@app.route('/')
def home():
    return {"message": "Nutrition Assistant Backend is running!"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
