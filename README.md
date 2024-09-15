
# Course information Q&A: Question and Answer System Based on Google Palm LLM and Langchain for E-learning company  

This is an LLM project based on Google Palm and Langchain. Aim is to build a Q&A system for an e-learning company called. The Ed-tech sells data related courses and bootcamps. They have thousands of learners who uses discord server or email to ask questions. This system will provide a streamlit based user interface for students where they can ask questions and get answers. 

![](ed-tech_banner.png)

## Project Highlights

- Use a CSV file containing a collection of FAQs that Ed-tech company is using right now to answer the questions. 
- The comapny's human staff will use this file to assist their course learners.
- We can replace the human work with an LLM based question and answer system that can reduce the workload of their human staff.
- Students should be able to use this system to ask questions directly and get answers within seconds

## Technologies used:
  - Langchain + Google Palm: LLM based Q&A
  - Streamlit: UI
  - Huggingface instructor embeddings: Text embeddings
  - FAISS: Vector databse

## Installation
1. Install the required dependencies using pip:

```bash
  pip install -r requirements.txt
```
2. Acquire an api key through makersuite.google.com and replace the your_google_api in .env file

```bash
  GOOGLE_API_KEY="your_google_api"
```
## Usage

1. Run the Streamlit app by executing:
```bash
streamlit run main.py

```

2. The web app will open in your browser.

- To create a knowledebase of FAQs, click on Create Knolwedge Base button. It will take some time before knowledgebase is created.

- Once knowledge base is created you will see a directory called faiss_index in your current folder

- Now you are ready to ask questions. Type your question in Question box and hit Enter

## Sample Questions
  - Do you guys provide internship and also do you offer EMI payments?
  - Do you have javascript course?
  - Should I learn power bi or tableau?
  - I've a MAC computer. Can I use powerbi on it?
  - I don't see power pivot. how can I enable it?

## Project Structure

- main.py: The main Streamlit application script.
- langchain_helper.py: This has all the langchain code
- requirements.txt: A list of required Python packages for the project.
- .env: Configuration file for storing your Google API key.