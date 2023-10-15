import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from collections import Counter
import matplotlib.pyplot as plt

text = open("Here-You-Want-To-Analyse-Something.txt", encoding = "utf-8").read()
text = text.lower()
text = text.translate(str.maketrans('','',string.punctuation))
text = word_tokenize(text,'english')

final_word = []
for word in text:
    if word not in stopwords.words('english'):
      final_word.append(word)
#print(final_word)
text = ' '.join(final_word)

emotion_list = []
with open('emotions.txt','r') as file:
   for line in file:
        clear_line = line.replace('\n','').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        if word in final_word:
          emotion_list.append(emotion)
         # print('WORD : ',word,"    ",'EMOTIONS : ',emotion)

print(emotion_list)


emotion_count = Counter(emotion_list)
print(emotion_count)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg > pos:
      print("YOU HAVE NEGATIVE SENTIMENTS")
    elif neg < pos:
      print("YOU HAVE POSITIVE SENTIMENTS")
    else:
       print("YOU HAVE NEUTRAL VIBE")
sentiment_analyse(text)

plt.bar(emotion_count.keys(), emotion_count.values())
plt.savefig('Sentimental-analysisGRAPH-using-NLP.png')
plt.show()