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


def build_lda_model(CIKs):
    main_path = dirname(realpath(__file__)) + "/data/14d9"
    for CIK in CIKs:
        files = [f for f in listdir(main_path + '/' + CIK) if isfile(join(main_path + '/' + CIK, f))]
        for file in files:
            try:
                print(main_path + '/' + CIK + '/' + file)
                with open(main_path + '/' + CIK + '/' + file, "r", encoding="latin-1") as f:
                    for row in f:
                        print(row, 'here')
                        document = [word for word in row.split(" ") if len(word) > 2]
                        documents.append(document)
            except IOError as e:
                print("Couldn't open file (%s)." % e)

    bigram = Phrases(documents, threshold=10)
    #trigram = Phrases(bigram[documents], threshold=10)
    for idx in range(len(documents)):
        for token in bigram[documents[idx]]:
            if '_' in token:
                documents[idx].append(token)

    # Dictionary
    dct = corpora.Dictionary(documents)
    #dct.filter_extremes(no_above=0.5)

    # Corpus
    corpus = [dct.doc2bow(line) for line in documents]

    mallet_path = dirname(realpath(__file__)) + "/mallet-2.0.8/bin/mallet"
    environ['MALLET_HOME'] = dirname(realpath(__file__)) + '/mallet-2.0.8/'
    lda_mallet = LdaMallet(mallet_path, corpus=corpus, num_topics=NUM_TOPICS, id2word=dct, iterations=ITERATIONS)

    # Show Topics
    print("LDA Model MALLET")
    for idx in range(NUM_TOPICS):
        print("Topic #%s-" % idx, lda_mallet.print_topic(idx, 10))


if __name__ == '__main__':
    build_lda_model(['100412'])