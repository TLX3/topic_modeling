from os import listdir, environ
from os.path import isfile, join, dirname, realpath
from gensim import corpora
from gensim.models import Phrases
from gensim.models.wrappers import LdaMallet

NUM_TOPICS = 5
ITERATIONS = 300

documents = []
lda_model = None
dct = None
corpus = None


def build_lda_model():
    path = dirname(realpath(__file__)) + "/data/14d9"
    files = [f for f in listdir(path) if isfile(join(path, f))]

    for file in files[:100]:
        f = open(path + '/' + file, "r", encoding="latin-1")
        for row in f:
            document = [word for word in row.split(" ") if len(word) > 2]
            documents.append(document)

    bigram = Phrases(documents, threshold=10)
    #trigram = Phrases(bigram[documents], threshold=10)
    for idx in range(len(documents)):
        for token in bigram[documents[idx]]:
            if '_' in token:
                documents[idx].append(token)

    # Dictionary
    dct = corpora.Dictionary(documents)
    dct.filter_extremes(no_below=20, no_above=0.5)

    # Corpus
    corpus = [dct.doc2bow(line) for line in documents]

    mallet_path = dirname(realpath(__file__)) + "/mallet-2.0.8/bin/mallet"
    environ['MALLET_HOME'] = dirname(realpath(__file__)) + '/mallet-2.0.8/'
    print(mallet_path)
    lda_mallet = LdaMallet(mallet_path, corpus=corpus, num_topics=NUM_TOPICS, id2word=dct, iterations=ITERATIONS)

    # Show Topics
    print("LDA Model MALLET")
    for idx in range(NUM_TOPICS):
        print("Topic #%s-" % idx, lda_mallet.print_topic(idx, 10))

    lda_model.save('lda_model.model')


if __name__ == '__main__':
    build_lda_model()