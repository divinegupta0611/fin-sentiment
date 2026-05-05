from setuptools import setup, find_packages

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fin-sentiment",
    version="0.1.4",
    author="Divine Gupta",
    author_email="your_email@example.com",  # optional but recommended
    description="Financial news sentiment analysis using LSTM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    
    # ✅ Include model files (.pth)
    include_package_data=True,
    package_data={
        "fin_sentiment": ["models/*.pth"],
    },
    
    install_requires=[
        "torch",
        "numpy",
        "requests",
        "beautifulsoup4",
        "feedparser"
    ],
    
    python_requires=">=3.8",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
