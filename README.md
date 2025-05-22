# 📊 Sentiment Analysis, Filler-Word Ratio & Interactive Dashboard
## 🛠️ Necessary Libraries (some require installation)
- Torch
- transformers (uses pysentimiento)
- pysentimiento
- Built-in regular expression
- Pandas
- Matplotlib
- Streamit
- tabulate

## ⚙️Installation (assuming none of necessary libraries are pre-installed)
- pip install torch transformers pysentimiento matplotlib pandas tabulate streamlit
  
## 📂 Set up and run instruction
- Download Bones-ltd zip file and extract.
- Use **cd Bones-Ltd-main** to change directories.
- To run the analysis, installing all required libraries, run: **python3 analysis.py** on terminal.
- To launch the interactive dashboard, run **python -m streamlit run app.py** on terminal.

## 🎯 Sample Output
- Sample output files for Sentiment Analysis and Filler Word Ratio are provided in the **Sample Output folder**.
- Running the application will regenerate these files automatically based on the given **transcript file**.
- Dashboard HTML Sample Output is accessible via **https://bones-limited.streamlit.app/**.

## 📈 Description of each metrics
### 1. Sentiment analysis
- 💬 Text: The original line of dialogue or message.

- 🙂 Sentiment: The overall sentiment label for the line (Positive, Neutral, or Negative), determined by the highest predicted probability.

- 📊 POS (Positive Probability): The model’s confidence score that the line expresses positive sentiment.

- ⚪ NEU (Neutral Probability): The model’s confidence score that the line is neutral.

- 🔴 NEG (Negative Probability): The model’s confidence score that the line expresses negative sentiment.

### 2. Filler Ratio Metrics
- 💬 Text: The original line of dialogue or message.

- ⏳ Filler Ratio: The proportion of filler words (e.g., "um", "uh", "like") to the total number of words in the line. A higher ratio suggests less fluency or more hesitation in speech.

### BONUS: 3. Emotion Analysis Metrics
- 💬 Text: The original line of dialogue or message.

- 🙂 Sentiment: The overall sentiment label for the line (Positive, Neutral, or Negative), determined by the highest predicted probability.

- 🎭 Overall Emotions: The dominant emotion label predicted for the line, based on the highest probability among all emotion classes.

## 📊 Description of interactive dashboard's metrics
### 1. Filler Ratio Chart
- 📉 Percentage of filler words (e.g., "um", "uh", "like", "you know") relative to total words spoken.

### 2. Filler Ratio Chart
- 🙂⚪🔴Shows the proportion of positive, neutral, and negative sentiments across the transcripts.

### BONUS: 3. Most Common Filler Words
- 🗣️ Highlight the most used nad least used number of filler words in the conversations.

### BONUS: 4. Sentiment Distribution Pie Chart
- 🥧 Percentage of all sentiments relative(POS, NEU, NEG) to total lines of alternating speaker.

## ⚪⚪⚪ In one extra hour I would add…
- 🎯 Create more versatite conversations to improve testing.
- 🗃️ Enable transcript upload, allowing users to drag-and-drop their own transcripts for instant analysis. 
- 🔍 Analyze sentiment and filler use by conversation topic or phase (e.g., intro, feedback, wrap-up).
