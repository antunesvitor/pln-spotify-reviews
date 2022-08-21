from time import sleep
from textblob import TextBlob
from newspaper import Article
from tqdm.auto import tqdm
import nltk
import pandas as pd


# nltk.download('punkt')

# url = 'https://wiki.archlinux.org/title/Installation_guide'
# article = Article(url=url)

# article.download()
# article.parse()
# article.nlp()


# text = article.summary
# text = 'I can\'t listen to my DOWNLOADED playlist while I\'m offline. So what\'s the point of this feature? Disappointed..'

# blob = TextBlob(text)
# sentiment = blob.sentiment.polarity
# print('Texto: {};\nSentimento: {}'.format(text, sentiment))


data = pd.read_csv('reviews.csv')
reviews = pd.DataFrame(columns=["index", "Review", "Rating", "sentimento_pontuacao"])

for row_index, registro in tqdm(iterable=data.iterrows(),total=data.shape[0]):
    
    indice = row_index
    review_txt = registro["Review"]     # texto da avaliação
    nota = registro["Rating"]           # de 1 a 5

    blob = TextBlob(review_txt)
    sentimento = blob.sentiment.polarity
    review = pd.DataFrame([[indice, review_txt, nota, sentimento]], columns=["index", "Review", "Rating", "sentimento_pontuacao"])
    reviews = pd.concat([reviews, review])
    
    sleep(0.001)

    