import pytest
import numpy as np 
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
import os

def test_model_architecture_and_weights(): 
    assert os.path.exists("model_weights.weights.h5"), "Weights file is missing"

    base = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')
    base.trainable = False
    model = models.Sequential([
        base, 
        layers.Dense(1, activation='sigmoid')
    ])

    try: 
        model.load_weights("model_weights.weights.h5")
        weights_loaded = True
    except Exception as e: 
        weights_loaded = False

    assert weights_loaded == True, "Model weights failed to load into architecture!!"

def test_model_prediction_shape():
    base = MobileNetV2(weights = 'imagenet', include_top = False, pooling='avg')
    base.trainable = False
    model = models.Sequential([base, layers.Dense(1, activation='sigmoid')])
    model.load_weights("model_weights.weights.h5")

    fake_image = np.random.rand(1,224, 224, 3)
    prediction = model.predict(fake_image)

    assert prediction.shape == (1,1), f"Expected output shape (1,1), got {prediction.shape}"