# Cat VS Dog Classifier

Train a machine to identify whether an image contains a cat or a dog using deep learning techniques. Achieve up to 96% accuracy with transfer learning and the VGG16 model.

## Table of Contents

- [Introduction](#introduction)
- [Technologies/Tools Used](#technologies-tools-used)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Cat VS Dog Classifier is a deep learning project developed with TensorFlow and Streamlit. It uses a pre-trained model to classify images as either cats or dogs, achieving high accuracy rates.

## Technologies/Tools Used

- TensorFlow
- Streamlit
- NumPy
- Pandas
- PIL (Python Imaging Library)

## Description

The Cat VS Dog Classifier is a Streamlit web application that allows users to upload images and predict whether they contain a cat or a dog. The model is based on a TensorFlow Lite quantized model (`quantized_model.tflite`), which is loaded using the TensorFlow Lite interpreter. Images are preprocessed using the Python Imaging Library (PIL) and then passed through the model for prediction.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/cat-vs-dog-classifier.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit web application:

    ```bash
    streamlit run app.py
    ```

2. Upload an image using the file uploader.
3. Click the "Predict" button to classify the uploaded image as either a cat or a dog.

## Screenshots

![Cat Prediction](screenshots/cat_prediction.png)
![Dog Prediction](screenshots/dog_prediction.png)

<!-- Add more screenshots as needed -->

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).
