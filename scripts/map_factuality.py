from sklearn import multiclass
from textblob import TextBlob
import pandas as pd
from transformers import pipeline


def map_factuality(df):
    '''
    Maps tweet to its factuality score.

    Args:
        df (pandas.DataFrame): DataFrame containing tweets.

    Returns:
        (pandas.DataFrame): DataFrame with factuality scores under factuality_score column.
    '''
    df['factuality'] = df['tweet'].apply(
        lambda x: 1 - TextBlob(x).sentiment.subjectivity)
    return df


def map_claim_score(df):
    '''
    Maps tweet to its claim score.

    Args:
        df (pandas.DataFrame): DataFrame containing tweets.

    Returns:
        (pandas.DataFrame): DataFrame with claim scores under claim_score column.
    '''
    classifier = pipeline('zero-shot-classification')
    label = 'This tweet contains a bold factual claim.'
    df['claim_score'] = df['tweet'].apply(lambda x: classifier(x, label,
                                                               hypothesis_template='{}')['scores'][0])
    return df


if __name__ == '__main__':
    df = pd.read_csv('../data/Tweets.csv')
    df = map_claim_score(df)
    df.to_csv('../data/Tweets_factuality.csv', index=False)
