from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from Brain_Tumor_Detection.utils.common import decodeImage
from Brain_Tumor_Detection.pipeline.prediction import PredictionPipeline

# Set environment variables for UTF-8 encoding to prevent characters issues in terminal output
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Initialize the Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) to allow browser interactions from different origins
CORS(app)

class ClientApp:
    """
    Helper class to manage global application state, such as image filenames 
    and the prediction pipeline instance.
    """
    def __init__(self):
        # Default filename for images uploaded via the web interface
        self.filename = "inputImage.jpg"
        
        # Initialize the PredictionPipeline which loads the trained model
        self.classifier = PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    """
    Route to render the main web interface (Dashboard).
    """
    return render_template('index.html')

@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def trainRoute():
    """
    Route to trigger the training pipeline.
    This uses DVC (Data Version Control) to reproduce the pipeline stages.
    """
    # Triggers 'dvc repro' to run only out-of-date stages in the pipeline
    os.system("dvc repro")
    
    return "Training process initiated and completed successfully!"

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    """
    API Route to handle image classification requests.
    Expects a JSON payload containing a Base64 encoded image string.
    """
    # Extract the Base64 image string from the incoming JSON request
    image_base64 = request.json['image']
    
    # 1. Decode the Base64 string and save it as a local image file
    # Uses the helper function from common.py
    decodeImage(image_base64, clApp.filename)
    
    # 2. Invoke the PredictionPipeline to run the image through the AI model
    result = clApp.classifier.predict()
    
    # 3. Return the prediction result (class and confidence info) as JSON
    return jsonify(result)

if __name__ == "__main__":
    # Create an instance of our ClientApp manager
    clApp = ClientApp()
    
    # Start the Flask web server
    # host='0.0.0.0' makes the app accessible from other devices in the same network
    # port 8080 is often used for production/deployment environments
    app.run(host='0.0.0.0', port=8080)
