from nltk.tokenize import word_tokenize
import PyPDF2
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
filename = 'JavaBasics-notes.pdf'
doc = open(filename,'rb')
pdf = PyPDF2.PdfFileReader(doc)
count = 0
text = ''
while count < pdf.numPages:
    page = pdf.getPage(count)
    count = count + 1
    text = text + page.extractText()
if text != "":
   text = text

import re   
X = re.sub('[^a-zA-Z]',' ',text)
X = X.lower()
X = X.split()
stop_words = stopwords.words('english')

keywords = [word for word in X if not word in stop_words]
for i in range(len(keywords)):
    keywords[i] = keywords[i].lower()
from sklearn.feature_extraction.text import CountVectorizer  
cv = CountVectorizer(max_features = 500)


keywords=pd.DataFrame(keywords)
Y = keywords[0].value_counts()

Y = Y[0:500]





































