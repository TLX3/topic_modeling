# Course Project - Topic modeling on select 14D9 documents
### Introduction

There exists a large amount of unstructured textual data with regards to SEC filings. Based on the immense size and continual growth of the SEC filing corpus, it is difficult to access relevant content within the collection. By using topic modeling on SEC filings, we uncover hidden topics that are present across the collection that can facilitate the reduction of irrelevant documents for users. 

This backend Python code takes select prescraped documents obtained from my workplace Lazard and runs topic modeling by using LDA on those documents. The web application allows users select a company by CIK ([You can search using these using Fast Search on the SEC site](https://www.sec.gov/edgar/searchedgar/companysearch.html)), the number of topics, and the size of n-grams to generate the topic model. The presentation and visualization of results are then both available in tabular form and in a word cloud

The goal of this project is to build an investment banking specific tool that uncover both single word and phrases as topics in SEC filings. Additionally, uncovered topics might provide grounds or inspiration for research into some other domain. In other words, detect trends that would have otherwise been difficult to capture or would have been missed.
## Getting Started

These instructions will get the project up and running.

### Prerequisites

You will require both Node and Python installed to run locally.
If you don't have them installed they can be obtained from 
```
https://nodejs.org/en/download/
https://www.python.org/downloads/
```
You will also require LDA MALLET to be extracted locally. Download from [http://mallet.cs.umass.edu/dist/mallet-2.0.8.zip](http://mallet.cs.umass.edu/dist/mallet-2.0.8.zip). Then extract the contents of the zip to /topic_modeling. You should now have the directory
```
Course_Project/topic_modeling/mallet-2.0.8
```
### Installation

Instructions to get the application running locally

At the main project directory level, run these commands from a terminal.
* If you have many other projects locally, it would be advised to first create a new virtual environment before installing Python packages.
```
pip install -r requirements.txt 
# The installation might take a while during setup.py for pycparse and nltk.
```

And then

```
cd frontend
npm install
```

## Deploying locally
At the main project directory level, run these commands from a terminal. Make sure ports 8080 and 5000 are available locally.
Start the Flask server at port 5000 by
```
cd topic_modeling
python app.py
```
then from another terminal, serve the client side application by
```
cd frontend
npm run serve
```
Go to [http://localhost:8080/](http://localhost:8080/) and use the web app!
## Project Structure
### /topic_modeling
    .
    ├── data                   # Cleansed and scraped 14D9 files
    ├── mallet-2.0.8           # Files needed to run LDA Mallet model
    ├── __init__.py            # Define variables at package level
    ├── analyze_documents.py   # Build LDA model and returns various analytics
    ├── app.py                 # Flask endpoints for client
    └── fetch_documents.py     # Get and save prescraped files from Azure cloud container
### /frontend
    .
    ├── node_modules           # Various packages and dependencies required to run web application
    ├── public                 # Static assets not processed through webpack
    ├── src                        
        ├── assets             # Images and logos
        ├── components         # Vue.js components 
            ├── Main.vue                 # Parent component for both user inputs and output charts and tables
            ├── SelectCIKs.vue           # Various select inputs
            ├── TopicAnalytics.vue       # Various data tables to display analytics information
            └── TopicVisualization.vue   # Highcharts word cloud and table by topic
        ├── plugins            # Enables and imports Vuetify
        ├── App.vue            # Core Vue component that is mounted to markup
        └── main.js            # Initialzation of app along with imports
    ├── .env.development       # Environment variables
    ├── .env.production        
    ├── .gitignore
    ├── .babel.config.js       # Javascript compiler config
    ├── .package-lock.json
    ├── README.md
    └── vue.config.js          # vue-cli config
## Built With

* [Flask](http://flask.palletsprojects.com/en/1.1.x/) - Micro web framework used to build APIs
* [Vue](https://vuejs.org/) - Framework for building user interfaces and single page applications
* [Gensim](https://radimrehurek.com/gensim/) - Open-source library for unsupervised topic modeling and natural language processing
* [Highcharts](https://www.highcharts.com/) - Javascript library for charting
* [Vuetify](https://vuetifyjs.com/en/) - Material design component framework for Vue.js
* and many more python and node dependencies
## API
app.py has two endpoints GET /get_CIKs and GET /get_topics. Since the user intially doesn't know what the possible companies/CIKs are, the backend will have to provide it to them. available_CIKs gets the directory names inside of data/14d9 in a list and returns them. The directory names correspond to a CIK.

/get_topics uses the build_lda_model method imported from analyze_documents. The arguments required for this method are CIKs, number of topics, and the size of the n-grams of the phrases within each topic.

## Backend functions explanation
get_SEC_Documents takes in the number of documents needed to be fetched from one of Lazard's Azure cloud containers. The cloud container that I've been permitted to use was made public for testing purposes for potential hires and side projects so it contains only a select number of prescraped SEC documents.
The function connects to the Azure container and pulls blobs from Blob storage. Then transforms them to text and strips the html using BeautifulSoup. Then the text is cleansed by lemmatization and removing stopwords, non-ASCII characters, and short words. These then get saved locally.

build_lda_model takes in CIKs, number of topics, and size of ngrams and outputs a 2D array of topics, where each topic is an array of objects which each have a term and weight. Also, it outputs 2 dictionaries, one for dominant topic of each document and another for the most representative document for a topic. 
To begin, I first have to obtain the documents to feed into the LDA MALLET model. I go through the /data/14d9 directory and find the respective CIK directories. I take the documents for each of CIK directories and collect them. Those documents are then transformed using gensim's Phrases method to generate bigrams, trigrams, etc. Then a dictionary is generated and along with a corpus using those documents. With those in place, I can run Ldamallet and generate the topics.
I then call the create_topic_analytics methods to get the dataframes to show analytics about the topics. By feeding the corpus to the model, I can get the topic breakdown at the document level. I can then sort those documents by topic weight and collect the most dominant one. By grouping the dataframe by the dominant topic, I can obtain the most relevant document for each topic.

## Vue Components explanation
As with any Vue app, the core component mounted is App.
Main components consists of SelectCIKs and TopicVisualization components. SelectCIKs consists of the select inputs for CIKs, number of topics, and size of n-grams. Also, when the SelectCIKs component is mounted, a async call is made to the backend for GET /get_CIKs which returns a list of all available CIKs. TopicVisualization consists of the highcharts word cloud for topics / table of term and weights and also TopicAnalytics which are multiple tables for displaying topic analytics information. The Main components maintains the state for selectedCIKs, num_topics, and ngram_num, chartData, and analyticsData and passes these as props to the children mentioned earlier. selectedCIKs, num_topics, and ngram_num are updated in state as they are selected by the user. The change event emits the update to Main. Once selectedCIKs, num_topics, and ngram_num are all selected, the generate topics button will be displayed. When this button is clicked, a async call is made to the backend to GET /get_topics with required params. Then the response contains the json for chartData and also analyticsData. Intially, I have TopicVisualization hidden until chartData is updated. Once the state change occurs, I have a watcher pick up the update and create the series needed to render the word cloud chart. Also, all of TopicVisualization is shown now. I have multiple tabs on the bottom of the card containing the chart which can toggle to the analytics view. The analytics view hides the word cloud and topic selection select and renders the selected data table for the analytics type.
## Future extensions

Currently, the application is tied to prescraped 14D9 found on Lazard's cloud. Also, the files are persisted and stored locally. In the future, the application can be extended to include arbitrary SEC documents across any CIK/ticker.
 
A company to CIK/Ticker mapping can be implemented to support this application. 

The files can have metadata associated with it such as Date Filed, Form Type, Company Name, CIK. These along with the file can be persisted to a cloud elasticsearch instance. This will allow analytics with a time dimension and also improve the UI with greater search filters.
## Author

* **Tseten Lama** - tsetenl2@illinois.edu

## License

This project is licensed under the MIT License

