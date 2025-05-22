from pysentimiento import create_analyzer
import re
import pandas as pd
from tabulate import tabulate
import os

output_dir = "SampleOutput"
os.makedirs(output_dir, exist_ok=True)

def read_transcript(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        turns = [line.strip() for line in f if line.strip()]
    return turns

#Filter ratio
def compute_filler_ratio(text_lines):
    filler_words = {"um", "uh", "like","ah","yeah"}
    data = []

    for num, line in enumerate(text_lines, 1):
        words = re.findall(r"\b\w+\b", line.lower())  # Lowercase for matching
        total_words = len(words)
        filler_count = sum(1 for word in words if word in filler_words)
        ratio = filler_count / total_words if total_words > 0 else 0
        data.append({
            "Line Number": num,
            "Context": line,
            "Filler Ratio": round(ratio, 5)
        })

    df =  pd.DataFrame(data)
    output_path = os.path.join(output_dir, "compute_filler_ratio.csv")
    df.to_csv(output_path, index=False)
    return df


#Sentiment
def compute_sentiment(text):
    analyzer = create_analyzer(task="sentiment", lang="en")
    data = []

    for num, line in enumerate(text, 1):
        result = analyzer.predict(line)
        probas = result.probas

        data.append({
            "Line Number": num,
            "Text": line,
            "Sentiment": result.output,
            "POS": round(probas.get("POS", 0),5),
            "NEU": round(probas.get("NEU", 0),5),
            "NEG": round(probas.get("NEG", 0),5),
        })

    df = pd.DataFrame(data)
    output_path = os.path.join(output_dir, "compute_sentiment.csv")
    df.to_csv(output_path, index=False)
    return df

#Bonus metric: emotions analysis
def compute_emotions(text):
    analyzer = create_analyzer(task="emotion", lang="en")
    data = []

    for num, line in enumerate(text, 1):
        result = analyzer.predict(line)
        data.append({
            "Line Number": num,
            "Text": line,
            "Overall Emotions": result.output,
            "Mixed": round(result.probas.get("others", 0),5),
            "Joy": round(result.probas.get("joy", 0),5),
            "Sadness": round(result.probas.get("sadness", 0),5),
            "Anger": round(result.probas.get("anger", 0), 5),
            "Surprise": round(result.probas.get("surprise", 0), 5),
            "Disgust": round(result.probas.get("disgust", 0), 5),
            "Fear": round(result.probas.get("fear", 0), 5)}
        )

    df = pd.DataFrame(data)
    output_path = os.path.join(output_dir, "compute_emotion.csv")
    df.to_csv(output_path, index=False)
    return df

#Parsing & Loading
dialogue_turns = read_transcript("transcript.txt")

#Sentiment Analysis
df_sentiment = compute_sentiment(dialogue_turns)
print(tabulate(df_sentiment, headers='keys', tablefmt='grid'))

#Filler-Word Ratio
df_filter = compute_filler_ratio(dialogue_turns)
print(tabulate(df_filter, headers='keys', tablefmt='grid'))

#Bonus metric: emotion analysis
df_emotions = compute_emotions(dialogue_turns)
print(tabulate(df_emotions, headers='keys', tablefmt='grid'))
