import pandas as pd
from datasets import load_dataset
from transformers import pipeline
from pathlib import Path

#text.csv contains the text upon which text-analysis and classification will be performed. Text was copied from data.pulls and data.comments
#text from data.pulls : text under column 'title' and then text under column 'body'
#text from data.comments : text under column 'body'
#text was cleaned to remove any special characters, links and other noise before text analysis and classification was performed

filepath = Path('/Users/akshajsrinivasan/Desktop/text.csv') 
PATH = r"/Users/akshajsrinivasan/Desktop/results.csv"             
df = pd.read_csv(PATH, skip_blank_lines=False)
df2 = pd.DataFrame(index=range(len(df.index)),columns=range(1))

#modelnames for different hugging face models used:

#  https://huggingface.co/j-hartmann/emotion-english-distilroberta-base : j-hartmann/emotion-english-distilroberta-base
#  https://huggingface.co/shahrukhx01/question-vs-statement-classifier : shahrukhx01/question-vs-statement-classifier
#  https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment : cardiffnlp/twitter-xlm-roberta-base-sentiment
#  https://huggingface.co/madhurjindal/autonlp-Gibberish-Detector-492513457 : madhurjindal/autonlp-Gibberish-Detector-492513457
#  https://huggingface.co/neuralsentry/starencoder-git-commit-bugfix-classification : MODEL CURRENTLY UNAVAILABLE

classifier = pipeline(model="cardiffnlp/twitter-xlm-roberta-base-sentiment", return_all_scores=True) #Change model by inserting appropriate model name here
for ind in df.index:
    df2.iloc[ind] = classifier(df.iloc[ind].to_string())
    print(df2.iloc[ind])


df2.to_csv(filepath)




