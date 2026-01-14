"""
Test script to verify the prediction pipeline works correctly
"""
from src.Brain_Tumor_Detection.pipeline.prediction import PredictionPipeline
import os

# Test with the existing input image
filename = "inputImage.jpg"

if os.path.exists(filename):
    print(f"Testing prediction with {filename}...")
    print("-" * 50)
    
    # Create prediction pipeline
    classifier = PredictionPipeline(filename)
    
    # Run prediction
    result = classifier.predict()
    
    print("-" * 50)
    print(f"Final Result: {result}")
    print("-" * 50)
else:
    print(f"Error: {filename} not found!")
