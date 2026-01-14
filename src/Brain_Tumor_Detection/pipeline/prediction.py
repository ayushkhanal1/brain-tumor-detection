import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    """
    Pipeline to handle the loading of a trained model and performing inference on a single image.
    """
    def __init__(self, filename):
        """
        Initializes the pipeline with the input image path.
        Note: The model is loaded from the 'artifacts' directory.
        """
        self.filename = filename
        # Load the trained model from the artifacts directory
        self.model = load_model(os.path.join("artifacts", "training", "model.h5"))
    
    def predict(self):
        """
        Loads the image, preprocesses it, and runs it through the model to get a prediction.
        """
        # Reference the pre-loaded model
        model = self.model

        # 1. Load the image from the specified path
        # target_size is set to (224, 224) to match the VGG16 input requirement.
        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        
        # 2. Convert the PIL image into a numerical numpy array.
        test_image = image.img_to_array(test_image)
        
        # 3. Expand Dimensions:
        # Keras models expect input as a batch (number_of_images, height, width, channels).
        # We add a leading dimension to transform (224, 224, 3) into (1, 224, 224, 3).
        test_image = np.expand_dims(test_image, axis=0)
        
        # 4. Normalization:
        # The model was trained using 1./255 rescaling, so we must apply it here too.
        test_image = test_image / 255.0
        
        # 5. Model Prediction:
        # model.predict returns a list of probabilities (confidence scores) for each class.
        prediction_scores = model.predict(test_image)
        print(f"Prediction scores: {prediction_scores}")
        
        # np.argmax picks the index [0, 1, 2, or 3] with the highest score.
        result = np.argmax(prediction_scores, axis=1)
        print(f"Prediction index: {result}")

        # 6. Result Interpretation:
        # Based on alphabetical order of folders: glioma (0), meningioma (1), notumor (2), pituitary (3)
        if result[0] == 0:
            prediction = 'Glioma'
        elif result[0] == 1:
            prediction = 'Meningioma'
        elif result[0] == 2:
            prediction = 'No Tumor'
        else:
            prediction = 'Pituitary'
            
        return [{"image": prediction}]
