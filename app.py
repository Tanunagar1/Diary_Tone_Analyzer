from flask import Flask, render_template
import glob
import nltk
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

def finding(filepaths):
    analyze = SentimentIntensityAnalyzer()
    positivity = []
    negativity = []
    dates = []

    for filepath in filepaths:
        with open(filepath, 'r') as file:
            content = file.read()

        score = analyze.polarity_scores(content)
        positivity.append(score['pos'])
        negativity.append(score['neg'])
        # dates.append(filepath.strip('.txt').strip('diary\\'))
        dates.append(Path(filepath).stem)

    return positivity, negativity, dates

@app.route("/")
def index():
    filepaths = sorted(glob.glob("diary/*"))
    positivity, negativity, dates = finding(filepaths=filepaths)
    return render_template('index.html', positivity=positivity, negativity=negativity, dates=dates)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
