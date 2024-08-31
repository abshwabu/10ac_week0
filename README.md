

# **10 Academy Week 0 Project: News Analysis and Event Modeling**


## **Table of Contents**

- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Contributing](#contributing)


## **Project Overview**

This project is part of the Week 0 challenge for the 10 Academy training program. The goal is to analyze news data, extract meaningful insights, and model events using various machine learning and natural language processing (NLP) techniques. The project involves keyword extraction, topic modeling, and event clustering to understand trends in news reporting and the relationships between different news sources.

## **Features**

- **Keyword Extraction**: Identify important keywords in news articles using TF-IDF and KeyBERT.
- **Topic Modeling**: Apply Latent Dirichlet Allocation (LDA) to categorize articles into topics and analyze trends over time.
- **Event Clustering**: Group news articles into clusters representing different events using K-Means clustering.
- **Visualization**: Interactive visualizations using Streamlit to explore the data and results.
- **Data Preprocessing**: Clean and preprocess large datasets to prepare them for analysis.

## **Dataset**

The datasets used in this project include:

- **News Data**: Contains articles, including metadata such as source name, title, full content, publication date, etc.
- **Metadata**: Provides additional information about the news sources, including location and country.

## **Installation**

To get started with the project, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/abshwabu/10ac_week0.git
   cd 10ac_week0
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Download the Dataset:**
   - Ensure you have the dataset files in the `data/` directory. You may need to preprocess the data if it’s large.

## **Usage**

To run the Streamlit dashboard:

```bash
streamlit run src/app.py
```

This will launch the interactive dashboard where you can explore the data, extract keywords, model topics, and visualize event clusters.

## **Project Structure**

```
10ac_week0/
│
├── data/                     # Folder containing the datasets
│   ├── data.csv
│   └── metadata.csv
│
├── src/                      # Source code for the project
│   ├── app.py                # Main Streamlit app
│   ├── EDA_and_stats.ipynb   
│   ├── db.ipynb
│   └── Modeling.ipynb
├── README.md                 # Project README file
├── requirements.txt          # Python dependencies
└── LICENSE                   # License for the project
```

## **Results**

### **Keyword Extraction**
- Identified top keywords for each article and compared similarities between titles and full content.

### **Topic Modeling**
- Discovered dominant topics in the news articles and analyzed trends over time.

### **Event Clustering**
- Grouped articles into event clusters and identified the earliest reporting sources.

### **Visualizations**
- Developed interactive visualizations in the Streamlit dashboard to explore and analyze the results.

## **Contributing**

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



 
Project Link: [https://github.com/abshwabu/10ac_week0](https://github.com/abshwabu/10ac_week0)

