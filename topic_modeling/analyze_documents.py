from os import listdir, environ
from os.path import isfile, join, dirname, realpath
from gensim import corpora
from gensim.models import Phrases
from gensim.models.wrappers import LdaMallet

ITERATIONS = 200

def build_lda_model(CIKs, num_topics):
    documents = []
    lda_model = None
    dct = None
    corpus = None

    main_path = dirname(realpath(__file__)) + "/data/14d9"
    for CIK in CIKs:
        files = [f for f in listdir(main_path + '/' + CIK) if isfile(join(main_path + '/' + CIK, f))]
        for file in files:
            try:
                with open(main_path + '/' + CIK + '/' + file, "r", encoding="latin-1") as f:
                    for row in f:
                        document = [word for word in row.split(" ") if len(word) > 2]
                        documents.append(document)
            except IOError as e:
                print("Couldn't open file (%s)." % e)

    phrases_only = [[] for _ in range(len(documents))]

    # Add bigram, trigrams, and quadgrams
    bigram = Phrases(documents)
    trigram = Phrases(bigram[documents])
    quadgram = Phrases(trigram[documents])
    for idx in range(len(documents)):
        for token in bigram[documents[idx]]:
            if '_' in token:
                phrases_only[idx].append(token)
        for token in trigram[documents[idx]]:
            if token.count('_') == 2:
                phrases_only[idx].append(token)
        for token in quadgram[documents[idx]]:
            if token.count('_') == 3:
                phrases_only[idx].append(token)

    documents = phrases_only

    # Dictionary
    dct = corpora.Dictionary(documents)

    # Corpus
    corpus = [dct.doc2bow(line) for line in documents]

    environ['MALLET_HOME'] = dirname(realpath(__file__)) + '/mallet-2.0.8/'
    mallet_path = dirname(realpath(__file__)) + "/mallet-2.0.8/bin/mallet"
    lda_mallet = LdaMallet(mallet_path, corpus=corpus, num_topics=num_topics, id2word=dct, iterations=ITERATIONS)

    # Show Topics
    print("LDA Model MALLET")
    for idx in range(num_topics):
        print("Topic #%s-" % idx, lda_mallet.print_topic(idx, 10))

    # Format topic and percentage for api export
    formatted_topics = []
    for _, topic_str in lda_mallet.print_topics():
        current_topic = []
        for percent_topic in topic_str.split(' + '):
            percent, term = percent_topic.split('*')
            current_topic.append({'weight': float(percent), 'term': term[1:-1]})
        formatted_topics.append(current_topic)
    return formatted_topics

if __name__ == '__main__':
    build_lda_model(CIKs=['1001258'], num_topics=5)