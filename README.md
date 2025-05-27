Spotify Music Genre Classification Project
Project Overview
This project aims to classify Spotify songs into different genres based on song lyrics and audio features using natural language processing (NLP) and machine learning techniques. Leveraging transformer-based models such as BERT, the system analyzes song lyrics and combines them with audio metadata to predict the genre of a track accurately.

Dataset
The dataset contains Spotify track metadata, audio features, and lyrics.

Key columns include:

track_id

artists

album_name

track_name

lyrics

popularity

duration_ms

Audio features: danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature

track_genre (target label)

Objectives
Preprocess and clean the dataset, including handling missing values.

Encode categorical features and labels.

Tokenize song lyrics using transformer tokenizers.

Fine-tune a pretrained BERT model for multi-class genre classification.

Evaluate model performance using accuracy, precision, recall, and F1-score.

Visualize performance metrics and confusion matrices.

Technologies & Libraries
Python 3.x

Pandas, NumPy

Transformers (Hugging Face)

PyTorch or TensorFlow

Scikit-learn

Matplotlib / Seaborn

Usage
Setup Environment
bash
Copy
Edit
pip install -r requirements.txt
Run Training
bash
Copy
Edit
python train.py --data_path ./data/spotify_dataset.csv
Evaluate Model
bash
Copy
Edit
python evaluate.py --model_path ./results/best_model
Folder Structure
graphql
Copy
Edit
.
├── data/
│   └── spotify_dataset.csv      # Raw dataset CSV file
├── notebooks/
│   └── exploratory_analysis.ipynb
├── src/
│   ├── preprocess.py            # Data cleaning and preprocessing scripts
│   ├── train.py                 # Model training scripts
│   ├── evaluate.py              # Model evaluation scripts
├── results/
│   └── best_model/              # Saved trained model files
├── requirements.txt             # Python dependencies
└── README.md                   # Project documentation

References
Hugging Face Transformers

Spotify Web API Documentation

Research papers on music genre classification using NLP and audio features.

