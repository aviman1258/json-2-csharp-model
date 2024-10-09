from flask import Flask
from flask_cors import CORS
from json_2_tree_direct import analyze_bp
from json_2_csharp_model_direct import model_bp

app = Flask(__name__)
CORS(app)

# Register the blueprints
app.register_blueprint(analyze_bp)
app.register_blueprint(model_bp)

if __name__ == "__main__":
    app.run(debug=True)