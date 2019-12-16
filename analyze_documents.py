from os import listdir
from os.path import isfile, join, dirname, realpath
from gensim import corpora
from gensim.models import LdaModel, Phrases

NUM_TOPICS = 10
NUM_PASSES = 20
ITERATIONS = 300
CHUNKSIZE = 2000
documents = []

path = dirname(realpath(__file__)) + "/data/14d9"
files = [f for f in listdir(path) if isfile(join(path, f))]

for file in files:
    f = open(path + '/' + file, "r")
    for row in f:
        document = [word for word in row.split(" ")]
        documents.append(document)

bigram = Phrases(documents, min_count=20)
#trigram = Phrases(bigram[documents], threshold=10)
for idx in range(len(documents)):
    for token in bigram[documents[idx]]:
        if '_' in token:
            documents[idx].append(token)

# Dictionary and Corpus
dct = corpora.Dictionary(documents)
dct.filter_extremes(no_below=20, no_above=0.5)
corpus = [dct.doc2bow(line) for line in documents]

# Train LDA model
lda_model = LdaModel(corpus=corpus,
                         id2word=dct,
                         random_state=100,
                         num_topics=NUM_TOPICS,
                         passes=NUM_PASSES,
                         chunksize=CHUNKSIZE,
                         iterations=ITERATIONS,
                         alpha='auto',
                         eta='auto',
                         eval_every=None)

print("LDA Model")
for idx in range(NUM_TOPICS):
    print("Topic #%s-" % idx, lda_model.print_topic(idx, 10))

