from flask import Flask, render_template
from flask_cors import CORS
from .analyze import analyze_bp
from .model import model_bp
import os
import webbrowser
from threading import Timer  # Import Timer
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
CORS(app)

# Register the blueprints
app.register_blueprint(analyze_bp)
app.register_blueprint(model_bp)

# Serve json-analyzer.html as a template
@app.route('/')
def serve_html():
    logging.info("Serving json-analyzer.html")
    return render_template('json-analyzer.html')  # Renders the HTML from templates folder

def open_browser():
    logging.info("Opening browser...")
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    if os.environ.get('FLASK_DEBUG') == 'production':
        Timer(1, open_browser).start()  # Open the browser after a 1-second delay
        debugval = False
    else:
        debugval = True
    
    app.run(debug=debugval)
