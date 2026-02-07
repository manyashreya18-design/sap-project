# SAP Phishing Detection Project

This project is a machine learning-based phishing website detection system developed as part of the SAP initiative. It uses deep learning models to analyze URLs and determine if they are safe or phishing attempts.

## Features

- Web-based interface for URL analysis
- Machine learning models for phishing detection
- REST API for integration
- Confidence scoring system

## Models

- Model 1: URL-based classification
- Model 2: BiLSTM model for text analysis
- Combined heuristic scoring

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the API server: `python api_server.py`
3. Open `index.html` in a browser

## Usage

Enter a URL in the web interface to get a safety analysis with confidence score.

## Branch Information

- `master`: Clean branch with README only
- `feature/v1`: Full implementation with models and code
