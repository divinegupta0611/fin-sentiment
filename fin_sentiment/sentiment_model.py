import torch
import torch.nn as nn
import torch.nn.functional as F
import re
import os


class SentimentLSTM(nn.Module):
    def __init__(self, vocab_size, embed_dim=128, hidden_dim=128, num_classes=3):
        super(SentimentLSTM, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim, padding_idx=0)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, num_classes)

    def forward(self, x):
        embedded = self.embedding(x)
        _, (h_n, _) = self.lstm(embedded)
        out = self.fc(h_n[-1])
        return out


def preprocess(text: str) -> str:
    """Clean and normalize input text"""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.strip()


class SentimentModel:
    def __init__(self, model_path: str = None):
        """Load the trained LSTM model and preprocessing artifacts."""
        # Resolve model path dynamically relative to this file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        if model_path is None:
            model_path = os.path.join(base_dir, "models", "sentiment_lstm.pth")

        # Safety check
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"❌ Model file not found at: {model_path}")

        # Load checkpoint
        checkpoint = torch.load(model_path, map_location=torch.device("cpu"))

        self.vocab = checkpoint["vocab"]
        self.labels = checkpoint["label_encoder"]

        # Initialize and load model weights
        self.model = SentimentLSTM(vocab_size=len(self.vocab))
        self.model.load_state_dict(checkpoint["model_state_dict"], strict=False)
        self.model.eval()

    def encode_text(self, text: str):
        """Convert text to numerical tokens"""
        tokens = preprocess(text).split()
        return [self.vocab.get(word, 1) for word in tokens]  # 1 = <UNK>

    def predict(self, text: str) -> str:
        """Predict sentiment of input text"""
        encoded = self.encode_text(text)
        if not encoded:
            return "neutral"

        x = torch.tensor(encoded, dtype=torch.long).unsqueeze(0)
        with torch.no_grad():
            outputs = self.model(x)
            probs = F.softmax(outputs, dim=1)
            pred_idx = torch.argmax(probs, dim=1).item()

        # Handle cases where label_encoder is a dict instead of LabelEncoder
        if isinstance(self.labels, dict):
            return self.labels.get(pred_idx, "neutral")
        elif hasattr(self.labels, "inverse_transform"):
            return self.labels.inverse_transform([pred_idx])[0]
        else:
            return str(pred_idx)
