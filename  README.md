# Diary Tone Analyzer

## Overview
Diary Tone Analyzer is a web application built with Flask that analyzes the sentiment of diary entries. It uses the NLTK library's SentimentIntensityAnalyzer to calculate the positivity and negativity scores for each diary entry and displays the results on a web page.

## Features
- Analyzes sentiment of diary entries
- Displays positivity and negativity scores on a web page

## Technologies Used
- Python
- Flask
- NLTK (Natural Language Toolkit)

## Setup
1. **Clone the repository:**

    ```bash
    git clone https://github.com/Tanunagar1/Diary_Tone_Analyzer.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Dockerfile**
4. **Run the Flask application:**

    ```bash
    python app.py
    ```

5. **Open your web browser and go to [http://localhost:5000/](http://localhost:5000/)**

## Usage
- Diary entries should be stored as text files in the "diary" directory.
- Each text file represents a single diary entry.
- The web page will display the positivity and negativity scores for each diary entry along with the date of the entry.

## File Structure
- **app.py**: Flask application file containing the route definitions and logic for sentiment analysis.
- **templates/index.html**: HTML template for the web page displaying sentiment analysis results.
- **diary/**: Directory containing diary entry text files.


## Author
Tannu Nagar
