import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#Filler Ratio Section
df_filler = pd.read_csv("compute_filler_ratio.csv")
st.title("Filler Ratios Dashboard")

st.subheader("Transcript with Filler Ratios")
st.dataframe(df_filler, use_container_width=True)

# Show overall average filler ratio
avg_filler_ratio = df_filler["Filler Ratio"].mean()
st.metric("Average Filler Ratio", f"{avg_filler_ratio:.3f}")

st.subheader("Filler Ratio Chart")
st.line_chart(df_filler.set_index(df_filler.columns[0])[df_filler.columns[-1]])

#Sentiment Section
df_sentiment = pd.read_csv("compute_sentiment.csv")
st.title("Sentiment Dashboard")

st.subheader("Transcript with Sentiment")
st.dataframe(df_sentiment, use_container_width=True)

# Show overall average sentiment probabilities
avg_pos = df_sentiment["POS"].mean()
avg_neu = df_sentiment["NEU"].mean()
avg_neg = df_sentiment["NEG"].mean()

st.subheader("Average Sentiment Scores")
col1, col2, col3 = st.columns(3)
col1.metric("Average POS", f"{avg_pos:.3f}")
col2.metric("Average NEU", f"{avg_neu:.3f}")
col3.metric("Average NEG", f"{avg_neg:.3f}")

st.subheader("Sentiment Chart")
st.line_chart(df_sentiment.set_index(df_sentiment.columns[0])[["POS", "NEU", "NEG"]])


# Bonus Visualization: Most Common Filler Words
st.title("Most Common Filler Words")

filler_words = ["um", "uh", "like", "you know", "ah", "yeah"]

counts = {}
for word in filler_words:
    count = df_filler["Context"].str.lower().str.count(rf"\b{word}\b").sum()
    counts[word] = count

filler_df = pd.DataFrame(list(counts.items()), columns=["Filler Word", "Count"]).sort_values(by="Count", ascending=False)

st.dataframe(filler_df)
st.bar_chart(filler_df.set_index("Filler Word"))

#Bonus Visualization: Sentiment Distribution Pie Chart
st.title("Sentiment Distribution Pie Chart")
sentiment_counts = df_sentiment["Sentiment"].value_counts()
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)