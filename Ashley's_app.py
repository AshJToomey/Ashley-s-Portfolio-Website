from flask import Flask, render_template, url_for

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Renders the index.html from templates folder

if __name__ == '__main__':
    app.run(debug=True)  # Run the app with debug mode enabled
