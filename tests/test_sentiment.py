from textblob import TextBlob

def test_positive_sentiment():
    text = "I love using this banking app!"
    sentiment = TextBlob(text).sentiment.polarity
    assert sentiment > 0

def test_negative_sentiment():
    text = "This app crashes all the time!"
    sentiment = TextBlob(text).sentiment.polarity
    assert sentiment < 0