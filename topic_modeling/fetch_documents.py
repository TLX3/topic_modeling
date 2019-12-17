import os
import string
import re
from azure.storage.blob import BlockBlobService
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import download

download('stopwords')
download('wordnet')

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()


def cleanse(doc):
    # Remove stopwords and short words
    stop_word_removed = " ".join([i for i in doc.lower().split() if i not in stop and len(i) > 2])

    # Remove punctuations
    puncs_removed = "".join(ch for ch in stop_word_removed if ch not in exclude)
    lemmatized_doc = " ".join(lemma.lemmatize(word) for word in puncs_removed.split())

    # Remove non-ASCII characters and words mixed with numbers
    lemmatized_doc = re.compile(r"\d*([^\d\W]+)\d*").sub(r"\1", lemmatized_doc)
    cleansed_doc = re.sub(r'[^\x00-\x7f]', r'', lemmatized_doc)

    return cleansed_doc


def get_SEC_Documents():
    # Azure blob credentials for LDAG
    account_name = 'stanfordproject'
    account_key = 'Brs84kSEd9yycVvTvbjuGxYlqBsROZHFi2CHV48tRDGO5 + jFwG83j0hraXPDogAeFZNUlBLKMCyhBeX / iWo9bA =='

    # Create the BlockBlockService to call the Blob service for the storage account
    block_blob_service = BlockBlobService(account_name, account_key)

    # Check 14d9 container
    generator = block_blob_service.list_blobs('14d9')

    blob_list = [b for b in generator]
    count = 0

    for blob in blob_list[0:100]:
        blob_text = block_blob_service.get_blob_to_text('14d9', blob.name, encoding='latin-1')
        raw_text = blob_text.content
        try:
            soup = BeautifulSoup(raw_text, 'html.parser')
            # remove html tags
            text_only = soup.get_text()
            processed_text = cleanse(text_only)
            CIK = blob.name.split('/')[0:1][0]
            fname = ''.join(blob.name.split('/')[1:])
            CIK_directory = os.path.dirname(os.path.realpath(__file__)) + '/data/14d9/' + CIK
            file_path = CIK_directory + '/' + fname
            if not os.path.exists(CIK_directory):
                os.makedirs(CIK_directory)
            try:
                with open(file_path, 'w') as f:
                    f.write(processed_text)
                    print("Added 14d9 file for CIK: ", CIK)
                    f.close()
            except IOError as e2:
                print(e2)
        except Exception as e1:
            print(e1)
            count += 1

    print('Number of Errors: ', count)


if __name__ == '__main__':
    get_SEC_Documents()
