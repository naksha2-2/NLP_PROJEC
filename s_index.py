import matplotlib.pyplot as plt




from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity

    # Determine if sentiment is positive, negative, or neutral
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    return sentiment, polarity

# Example text
text = "I love this product! It's amazing."

# Perform sentiment analysis
sentiment, polarity = analyze_sentiment(text)

print(f"Sentiment: {sentiment}")
print(f"Polarity: {polarity}")
