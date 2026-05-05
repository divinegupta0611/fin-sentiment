# fin-sentiment

**Financial News Sentiment Analysis using LSTM**

`fin-sentiment` is a Python package that analyzes the sentiment of financial news headlines using an LSTM-based deep learning model. It helps traders, investors, and analysts gauge market sentiment by classifying news as positive, neutral, or negative.

---

## Features

- 📰 Fetch latest financial news for any company
- 🤖 LSTM-based sentiment classification
- 📊 Aggregate sentiment analysis across multiple headlines
- ⚡ Simple, intuitive API
- 🎯 Trained on real financial news data

---

## Installation

```bash
pip install fin-sentiment
```

---

## Quick Start

```python
from fin_sentiment.news_fetcher import fetch_company_news
from fin_sentiment.analyzer import SentimentAnalyzer

# Step 1: Fetch latest news for a company
news = fetch_company_news("TCS", limit=10)

# Step 2: Initialize sentiment analyzer
analyzer = SentimentAnalyzer()

# Step 3: Analyze each news headline
for article in news:
    sentiment = analyzer.analyze(article["title"])
    print(f"{article['title']} → {sentiment}")

# Step 4: Get overall market sentiment
overall = analyzer.overall_sentiment(news)
print(f"Market Mood: {overall}")

# Step 5: Analyze a custom headline
custom_sentiment = analyzer.analyze("Stock prices surged after positive earnings report")
print(custom_sentiment)  # Output: positive
```

---

## API Reference

### Module: `fin_sentiment.news_fetcher`

#### `fetch_company_news(company_name: str, limit: int = 10) -> list`

Fetches the latest news headlines for a specified company from financial sources.

**Parameters:**
- `company_name` (str): Name of the company to fetch news for
- `limit` (int): Maximum number of headlines to retrieve (default: 10)

**Returns:** List of news articles with titles and metadata

**Example:**
```python
news = fetch_company_news("Infosys", limit=5)
```

---

### Module: `fin_sentiment.analyzer`

#### `SentimentAnalyzer()`

Initializes the LSTM-based sentiment analysis model.

**Example:**
```python
analyzer = SentimentAnalyzer()
```

#### `.analyze(text: str) -> str`

Analyzes the sentiment of a single text string.

**Parameters:**
- `text` (str): The headline or text to analyze

**Returns:** Sentiment label: `"positive"`, `"neutral"`, or `"negative"`

**Example:**
```python
sentiment = analyzer.analyze("Company shares hit record high")
print(sentiment)  # Output: positive
```

#### `.overall_sentiment(news_list: list) -> str`

Aggregates sentiment across multiple news headlines to determine overall market mood.

**Parameters:**
- `news_list` (list): List of news articles (with "title" key)

**Returns:** Overall sentiment: `"positive"`, `"neutral"`, or `"negative"`

**Example:**
```python
overall = analyzer.overall_sentiment(news)
print(overall)  # Output: neutral
```

---

## Example Output

```
TCS shares rise 5% after strong Q3 results → positive
TCS faces data breach allegations → negative
TCS announces dividend payout → positive
Market closes flat amid mixed signals → neutral

Market Mood: neutral
```

---

## Model Details

| Property | Details |
|----------|---------|
| **Architecture** | LSTM (Long Short-Term Memory) |
| **Framework** | PyTorch |
| **Dataset** | Financial headlines from multiple market sources |
| **Classes** | Positive, Neutral, Negative |
| **Output** | Softmax probability distribution → final label |

---

## Use Cases

- 📈 **Trading Signals**: Gauge market sentiment before making trades
- 📰 **News Monitoring**: Track sentiment trends for specific companies
- 🤖 **Automated Analysis**: Integrate sentiment into trading bots
- 📊 **Market Research**: Analyze sentiment patterns over time

---

## Requirements

- Python 3.7+
- PyTorch
- NumPy
- Requests (for news fetching)
- Feedparser

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

