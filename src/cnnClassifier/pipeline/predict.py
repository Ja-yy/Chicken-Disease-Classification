import os

import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import io

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # load model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        imagename = self.filename
        image = Image.open(io.BytesIO(imagename))
        image = image.resize((224, 224))  # Resize image to match model input size
        image = np.array(image) / 255.0  #
        test_image = np.expand_dims(image, axis=0)
        result = np.argmax(model.predict(test_image), axis=1)

        if result[0] == 1:
            prediction = "Healthy"
            return {"prediction": prediction}
        else:
            prediction = "Coccidiosis"
            return {"prediction": prediction}
