from azure.storage.blob import BlockBlobService
from bs4 import BeautifulSoup
import os
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


def cleanse(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = "".join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized


if __name__ == '__main__':
    # Azure blob credentials for LDAG
    account_name='stanfordproject'
    account_key='Brs84kSEd9yycVvTvbjuGxYlqBsROZHFi2CHV48tRDGO5 + jFwG83j0hraXPDogAeFZNUlBLKMCyhBeX / iWo9bA =='

    # Create the BlockBlockService to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name, account_key)

    # Get all containers
    containers = block_blob_service.list_containers()
    containers_name = [c.name for c in containers]
    #print("Available containers: {}".format(containers_name))
    #['14d9', 'earnings-call', 'ldag', 'meta', 'news', 'proxystatement']

    # check 14d9 container
    generator = block_blob_service.list_blobs(containers_name[0])

    blob_list = [b for b in generator]
    count = 0

    for blob in blob_list[0:10]:
        blob_text = block_blob_service.get_blob_to_text(containers_name[0], blob.name, encoding='latin-1')
        raw_text = blob_text.content
        try:
            soup = BeautifulSoup(raw_text, 'html.parser')
            # remove html tags
            text_only = soup.get_text()
            # remove stopwords and punctuations
            processed_text = cleanse(text_only)
            file_name = os.path.dirname(os.path.realpath(__file__)) + '/data/14d9/' + ''.join(blob.name.split('/')[1:])
            with open(file_name, 'a') as f:
                f.write(processed_text)
                f.close()
        except Exception as e:
            print(e)
            count += 1

    print('Number of Errors: ', count)
