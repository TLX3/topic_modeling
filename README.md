# CS410 Course Project - Topic modeling on select 14D9 documents
### Introduction

There exists a large amount of unstructured textual data with regards to SEC filings. Based on the immense size and continual growth of the SEC filing corpus, it is difficult to access relevant content within the collection. By using topic modeling on SEC filings, we uncover hidden topics that are present across the collection that can facilitate the reduction of irrelevant documents for users. 

This backend Python code takes select prescraped documents obtained from my workplace Lazard and runs topic modeling by using LDA on those documents. The web application allows users select a company by CIK, the number of topics, and the size of n-grams to generate the topic model. The presentation and visualization of results are then both available in tabular form and in a word cloud

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
        ├── plugins            # Enable Vuetify
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

## Author

* **Tseten Lama** - tsetenl2@illinois.edu

## License

This project is licensed under the MIT License

