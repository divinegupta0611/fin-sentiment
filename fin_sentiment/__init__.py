"""
fin_sentiment
A simple Python library for fetching company news and performing sentiment analysis.
"""

from .news_fetcher import fetch_company_news
from .sentiment_model import SentimentModel
from .analyzer import SentimentAnalyzer

__version__ = "0.1.0"

__all__ = ["fetch_company_news", "SentimentModel", "SentimentAnalyzer"]
