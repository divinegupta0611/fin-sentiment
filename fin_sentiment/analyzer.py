# analyzer.py
from .sentiment_model import SentimentModel

class SentimentAnalyzer:
    def __init__(self):
        # Load your trained LSTM model
        self.model = SentimentModel()

    def analyze(self, text: str):
        """
        Analyze sentiment of one text/news headline
        Returns one of: 'positive', 'negative', 'neutral'
        """
        if not text or not isinstance(text, str):
            return "neutral"
        return self.model.predict(text)

    def overall_sentiment(self, news_list):
        """
        Compute overall sentiment across multiple news headlines/articles.
        Expects list of dicts, each containing a 'title' or 'Summary' key.
        """
        sentiments = []
        for item in news_list:
            # Try to use 'title' if available, else 'Summary' or 'Content'
            text = item.get("title") or item.get("Summary") or item.get("Content", "")
            sentiments.append(self.analyze(text))

        score = sum(
            1 if s == "positive" else -1 if s == "negative" else 0
            for s in sentiments
        )

        if score > 0:
            return "Overall Positive"
        elif score < 0:
            return "Overall Negative"
        else:
            return "Overall Neutral"
