#  Nepali Songs Language Classification

This project implements a deep learning pipeline to classify Nepali songs into five different language categories. The model is built using TensorFlow/Keras and trained on a custom dataset of audio clips.

##  Features

- **Multi-class Audio Classification**: Classifies audio into 5 languages:
  - Nepali (नपल)
  - Bhojpuri (भजपर)
  - Maithili (मथल)
  - Newari (नवर)
  - Tamang (तमङ)
- **Data Visualization**: Includes extensive visualization of audio features and model performance.
- **Custom CNN Model**: A custom-built Convolutional Neural Network (CNN) designed for audio spectrograms.
- **Complete Pipeline**: From data preprocessing to model training, evaluation, and prediction.
- **High Accuracy**: Achieves high accuracy on the test set.

##  Project Structure

`
nepaliSongsClassify/
 dataset/                # Processed and balanced dataset
    bhojpuri/
    maithili/
    nepali/
    newari/
    tamang/
 models/                 # Saved models and artifacts
    label_mapping.json
    nepali_songs_classifier_best.keras
    nepali_songs_classifier_final.keras
    normalization_params.json
 originalDataset/        # Original, unbalanced dataset
 dataPrepare.py          # Script for preparing the dataset
 train.ipynb             # Jupyter notebook for training and evaluation
 README.md               # This file
`

##  Methodology

The project follows a standard deep learning pipeline:

1.  **Data Exploration**: The dataset is analyzed to understand class distribution and identify any imbalances.
2.  **Audio Visualization**: Various audio features are visualized, including:
    - Waveforms
    - Mel Spectrograms
    - MFCCs
    - Spectral Centroids
    - Chroma Features
3.  **Data Preprocessing**:
    - Audio files are loaded and trimmed/padded to a fixed duration (40 seconds).
    - Mel Spectrograms are extracted as features.
    - The dataset is balanced using undersampling to ensure each class has the same number of samples.
    - Data is split into training, validation, and test sets.
    - Features are normalized.
4.  **Model Building**:
    - A custom CNN model is built, inspired by VGG-style architectures.
    - The model uses Conv2D, BatchNormalization, MaxPooling2D, and Dropout layers.
5.  **Training**:
    - The model is trained using the Adam optimizer and categorical cross-entropy loss.
    - Callbacks like ModelCheckpoint, EarlyStopping, and ReduceLROnPlateau are used to optimize training.
6.  **Evaluation**:
    - The model's performance is evaluated on the test set using:
      - Classification Report
      - Confusion Matrix (both counts and percentages)
      - Per-class accuracy visualization.

##  Results

The model achieves a high accuracy on the test set. For detailed results, including precision, recall, and F1-score for each class, please refer to the 	rain.ipynb notebook.

The training history, confusion matrix, and per-class accuracy are saved as images in the models/ directory.

##  How to Use

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Required libraries (see 	rain.ipynb for a full list):
  - 	ensorflow
  - librosa
  - pandas
  - 
umpy
  - scikit-learn
  - matplotlib
  - seaborn

### Steps

1.  **Prepare the Data**:
    - Place your raw audio files in the originalDataset/ directory, organized by class folders.
    - Run the dataPrepare.py script to create the balanced dataset in the dataset/ folder.

    `ash
    python dataPrepare.py
    `

2.  **Train the Model**:
    - Open and run the 	rain.ipynb notebook in a Jupyter environment.
    - The notebook will handle everything from loading the data to training the model and saving the final artifacts.

3.  **Prediction**:
    - The notebook includes a predict_audio() function that can be used to classify new audio files.
    - You will need the saved model (
epali_songs_classifier_final.keras), the label mapping (label_mapping.json), and the normalization parameters (
ormalization_params.json), all located in the models/ directory.

##  Future Improvements

- **Data Augmentation**: Implement audio data augmentation techniques (e.g., pitch shifting, time stretching) to increase the diversity of the training data.
- **Transfer Learning**: Experiment with pre-trained audio models like VGGish or YAMNet for transfer learning.
- **Hyperparameter Tuning**: Perform a more exhaustive search for optimal hyperparameters.
- **Real-time Classification**: Build a simple web application or tool for real-time audio classification.