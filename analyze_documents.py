import os
from os import listdir
from os.path import isfile, join
from gensim import corpora
from gensim.models import LdaMulticore

NUM_TOPICS = 5
documents = []

path = os.path.dirname(os.path.realpath(__file__)) + "/data/14d9"
files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    f = open(path + '/' + file, "r")
    for row in f:
        document = [word for word in row.split(" ")]
        documents.append(document)

# LDA model: Dictionary and Corpus
dct = corpora.Dictionary(documents)
corpus = [dct.doc2bow(line) for line in documents]

# Train the LDA model
lda_model = LdaMulticore(corpus=corpus,
                         id2word=dct,
                         random_state=100,
                         num_topics=NUM_TOPICS,
                         passes=10,
                         chunksize=1000,
                         alpha='asymmetric',
                         decay=0.5,
                         offset=64,
                         eta=None,
                         eval_every=0,
                         iterations=100,
                         gamma_threshold=0.001,
                         per_word_topics=True)

print("LDA Model")
for idx in range(NUM_TOPICS):
    print("Topic #%s-" % idx, lda_model.print_topic(idx, 10))

