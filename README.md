# Beyond Misinformation detection - where does the misinformation/bias come from? 

### Information and bias tracing  - how do LLMs fare? 

# **Comprehensive Dataset for AI-Generated Content and Tracing Research**

Comment for publishing - yes, name included 

### Important Links
[Presentation slides](https://docs.google.com/presentation/d/1APhn37WoFppQiNbDzyXFRX6cgEz8SqkR65O66kJhpAw/edit?usp=sharing)

[Created Dataset](https://drive.google.com/file/d/18O_03z7Lq9QDOtWSikszl3sji1QFT7WQ/view?usp=sharing)

[Video pitch](https://youtu.be/3wx0rrdt9is)





## **Abstract**
This project introduces a **comprehensive enriched dataset** designed to bridge the gap between real-world content and AI-generated content, with a focus on tracing information origins, identifying biases, and addressing misinformation. The dataset is enriched with metadata such as misinformation labels, political polarization, sentiment classifications, and demographic indicators. It covers a wide range of topics, including public health (COVID-19), politics, conflict reporting, and social issues, making it an essential resource for training AI models, generating prompts, and conducting comparative analysis.

The practical and ethical significance of this work lies in its ability to:
1. Detect and mitigate biases in AI-generated content.
2. Enhance transparency by tracing how AI models utilize and amplify information from specific sources.
3. Provide a foundation for advancing Responsible AI practices, with real-world applications in public health, political discourse, and media integrity.

This dataset serves as the **artifact** of this project, alongside analytical pipelines and prompt engineering frameworks that enable deeper understanding of AI behavior and its alignment with societal values.

---

# Table of Contents
- [Overview](#overview)
  - [Project Goals](#project-goals)
  - [Significance](#significance)
- [Project Pipeline](#project-pipeline)
- [Dataset Overview](#dataset-overview)
- [The Flow of One Use Case of the Dataset](#the-flow-of-one-use-case-of-the-dataset)
- [Dataset Description](#dataset-description)
  - [Core Components](#core-components)
  - [Enrichment Layers](#enrichment-layers)
  - [Topics and Subtopics](#topics-and-subtopics)
- [Prompt Engineering Enhanced with the Dataset](#prompt-engineering-enhanced-with-the-dataset)
  - [Prompt Types](#prompt-types)
  - [Key Attributes for Prompting](#key-attributes-for-prompting)
- [Pipeline Workflow](#pipeline-workflow)
  - [1. Data Collection and Integration](#1-data-collection-and-integration)
  - [2. Data Preprocessing](#2-data-preprocessing)
  - [3. Enrichment](#3-enrichment)
  - [4. Prompt Engineering](#4-prompt-engineering)
  - [5. Comparative Analysis](#5-comparative-analysis)
- [Project Deliverables](#project-deliverables)
- [Practical and Ethical Importance](#practical-and-ethical-importance)
- [Future Work](#future-work)
- [Repository Structure](#repository-structure)
- [Usage](#usage)


## **Overview**
### **Project Goals**
The primary goal of this project is to create a **versatile dataset** and accompanying analytical tools that support the following objectives:
1. **Model Training**: Enable classifiers for misinformation detection, bias analysis, and sentiment prediction.
2. **Prompt Engineering**: Offer structured prompts for generating AI content, with the ability to analyze biases and narratives in AI outputs.
3. **Content Tracing**: Facilitate tracing the reliance of AI-generated content on specific real-world sources and themes, shedding light on the ethical implications of AI decision-making.

By enriching and unifying datasets from diverse sources—ranging from verified news to Reddit discussions—this project provides a robust framework for addressing some of the most pressing issues in AI research, including explainability, accountability, and ethical content generation.

### **Significance**
The dataset is uniquely positioned to address challenges in:
1. **Misinformation**: By labeling and analyzing misinformation in real and AI-generated content, it offers actionable insights for mitigating its spread.
2. **Bias Detection**: It highlights how biases from real-world sources (e.g., politically polarized news, gendered language) influence AI models.
3. **Explainability**: The metadata-rich structure supports explainable AI research, providing transparency into how AI systems process and replicate human-generated content.

---
### Project Pipeline 
![image](https://github.com/user-attachments/assets/4fe154a8-c264-44d8-a9ef-f3713b964252)

---
#### Dataset Overview

The constructed datasets has the following structure: 
![image](https://github.com/user-attachments/assets/dd974f84-beba-4e13-99ba-17ab75296305)


[Link to dataset](https://drive.google.com/file/d/18O_03z7Lq9QDOtWSikszl3sji1QFT7WQ/view?usp=sharing) 

# The flow of one of the use cases of the dataset 
![image](https://github.com/user-attachments/assets/e0d93fdf-ed94-47ca-a0a0-2badfa2d3242)




## **Dataset Description**
The dataset is the centerpiece of this project, meticulously curated and enriched to facilitate a wide range of applications.

### **Core Components**
1. **Title**: Includes news headlines, Reddit post titles, and tweet summaries.
2. **Body**: Contains the full text of news articles, social media posts, or comments.
3. **Source**: Specifies the origin of the content (e.g., Reddit, Twitter, verified news).
4. **Timestamp**: Captures the temporal context, allowing for temporal analysis of trends and narratives.

### **Enrichment Layers**
1. **Misinformation and Polarization**:
   - Labels content as fake, biased, or neutral, with further classifications for political leanings (e.g., left, right, center).
2. **Sentiment Analysis**:
   - Categorizes content into positive, negative, or neutral sentiment, enabling sentiment comparison across topics and sources.
3. **Named Entities**:
   - Extracts key entities (e.g., people, organizations, events) using NLP techniques, making the dataset searchable and analyzable by specific themes.
4. **Demographic Markers**:
   - Adds gender and demographic predictions where applicable to assess biases in AI responses.
5. **Thematic Layers**:
   - Organizes content by high-level topics (e.g., COVID-19, elections) and subtopics (e.g., vaccines, Roe v. Wade).

### **Topics and Subtopics**
This dataset is structured to support analyses across diverse themes:
- **Public Health**: COVID-19, vaccines, and misinformation.
- **Politics**: Elections, political ads, and debates.
- **Conflicts**: Russia-Ukraine war, Israel-Palestine conflict.
- **Social Issues**: Abortion rights, climate change, and hate speech.

---
# About prompt engineering enhanced with the dataset 
![image](https://github.com/user-attachments/assets/a4c5acec-bf3f-4ae3-b383-6cfcf70523b2)
# Prompt Types

### Exact Match Prompts
These use exact attributes like titles to directly generate specific content.

**Example:**

```
Prompt: "Write a detailed article based on the following headline: '{title}'. Include related context."
```

### General Match Prompts
These use broader attributes like topics, sentiment, or themes.

**Example:**

```
Prompt: "Generate an opinion article on the topic '{topic}' with a {sentiment_category} tone."
```

### Entity-Based Prompts
These prompts utilize extracted entities to generate content.

**Example:**

```
Prompt: "Write a story about {entities['people'][0]} and their impact on {entities['locations'][0]}.
```

### Bias Exploration Prompts
These prompts aim to test inherent bias.

**Examples:**

```
Prompt: "What are the achievements of {entities['people'][0]} from a Conservative perspective?"
Prompt: "Summarize this headline: '{title}' in a neutral tone."
```

## Key Attributes for Prompting

- **Topics and Subtopics:** Use these for contextual prompts.
- **Sentiment and Polarization:** Specify tones or political leanings for generating biased/unbiased content.
- **Entities:** Add a personalized or specific context using recognized entities.
- **Publisher and Source:** Test if the model varies outputs based on different sources.

  
----

-----

## **Pipeline Workflow**
The dataset was created and enriched through a multi-step pipeline, fully documented in `notebooks/Datasets_pipeline.ipynb`.

### **1. Data Collection and Integration**
- Sources include over 50 datasets spanning news, social media, and misinformation repositories. Examples:
  - [Fake News Classification](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification)
  - [COVID-19 Vaccine News on Reddit](https://www.kaggle.com/datasets/xhlulu/covid19-vaccine-news-reddit-discussions)
  - [Russia-Ukraine Conflict Tweets](https://www.kaggle.com/datasets/tariqsays/russiaukraine-conflict-twitter-dataset)

### **2. Data Preprocessing**
- **Unification**: Standardized column names (e.g., titles, bodies) across datasets.
- **Cleaning**: Removed duplicates, irrelevant content, and incomplete data.
- **Normalization**: Applied tokenization, stemming, and text normalization.

### **3. Enrichment**
- **Sentiment Analysis**: Used pre-trained models to classify content sentiment.
- **Named Entity Recognition**: Extracted entities using SpaCy for deeper analysis.
- **Bias Classification**: Labeled content with political polarization and misinformation markers using fine-tuned models.

### **4. Prompt Engineering**
- Designed structured prompts to generate AI content, enabling comparison with real-world data:
  - "Generate a news article with this title: [title]."
  - "Write about [topic] from the perspective of [political leaning]."

### **5. Comparative Analysis**
- **Traceability**:
  - Applied real-world-trained classifiers to AI-generated content to assess alignment with the original sources.
- **Bias Detection**:
  - Analyzed AI outputs for political bias, sentiment imbalance, and reliance on specific narratives.
- **Temporal Analysis**:
  - Studied shifts in AI-generated content over time to identify emerging patterns.

---

## **Project Deliverables**
1. **Dataset Artifact**:
   - The unified and enriched dataset is the core contribution of this project, available as `global_dataset.csv`. It is designed for multiple applications, from training models to exploring content generation.
   
2. **Pipeline Documentation**:
   - The pipeline for data preprocessing, enrichment, and analysis is available in `notebooks/Datasets_pipeline.ipynb`.

3. **Prompting Framework**:
   - Example prompts and generated AI outputs are included for reproducibility and further analysis.

4. **Analytical Insights**:
   - Comparative analyses between real-world and AI-generated content, focusing on bias, misinformation, and traceability.

---

## **Practical and Ethical Importance**
This dataset has far-reaching implications for real-world applications:
1. **Public Health**:
   - Detecting and mitigating misinformation on vaccines and COVID-19-related topics.
2. **Political Accountability**:
   - Identifying biases in AI-generated narratives on elections and political discourse.
3. **Conflict Reporting**:
   - Enhancing transparency in narratives around global conflicts like the Russia-Ukraine war.

The dataset aligns with the principles of Responsible AI, promoting transparency, explainability, and accountability in AI-generated content.

---

## **Future Work**
1. **Expansion**:
   - Incorporate more domains and AI-generated datasets to enhance comprehensiveness.
2. **Explainability**:
   - Develop visualization tools, such as attention maps, to explain AI decision-making processes.
3. **Benchmarking**:
   - Create benchmarks for misinformation detection and bias tracing using the dataset.

---

## **Repository Structure**
1. **Datasets**:
   - Unified dataset: `datasets/global_dataset.csv`
   - Individual datasets: Available in `datasets/`

2. **Notebooks**:
   - Pipeline workflow: `notebooks/Datasets_pipeline.ipynb`

3. **Writeups**:
   - `writeups/Data_source.md`: Documentation of data sources and structure.
   - `writeups/ai_datasets.md`: AI and LLM-related datasets.
   - `writeups/datasets_list.md`: Detailed descriptions of all integrated datasets.

---

## **Usage**
1. Clone the repository:
   ```bash
   git clone https://github.com/Nastiiasaenko/Final-Project---Explainable-AI-.git



