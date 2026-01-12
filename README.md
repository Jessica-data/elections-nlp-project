# Rhetoric vs. Reality: The Structural Break in U.S. Voting Behavior (2000-2024)

## 1. Abstract
Welcome to this repository ! 

This project investigates the predictive determinants of United States Presidential Elections from 2000 to 2024. It employs a **hybrid analytical approach** that integrates two distinct levels of data:
1.  **Micro-Level:** County-specific socio-economic and demographic indicators.
2.  **Macro-Level:** Rhetorical analysis of national campaign discourse (Nomination Acceptance Speeches and Party Manifestos) using Natural Language Processing (NLP).

The primary objective is to quantify the extent to which rhetorical sentiment interacts with local economic realities to influence voting behavior, with a specific focus on the structural break observed in the American electorate post-2016.

## 2. Research Questions

The analysis addresses the following core questions:
* **RQ1:** How accurately does the model predict county vote shares when based **only** on socio-economic and demographic indicators?
* **RQ2:** How does the predictive performance change when combining these socio-economic variables with **NLP-derived data** (sentiment and subjectivity) from party manifestos and convention speeches?
* **RQ3:** Does the model's predictive behavior exhibit a **structural shift after 2016** (following Donald Trump's first candidacy), indicating a change in the weight of specific variables?


## 3. Methodology & Workflow

The repository is structured sequentially to ensure reproducibility. The analysis pipeline consists of seven distinct phases:

### Phase I: Data Acquisition & Preprocessing
* **`01_data_collection.ipynb`**: Initialization of the project environment and directory architecture.
* **`02_cleaning.ipynb`**: County-level election returns from the MIT Election Data Lab were harmonized with socio-economic and demographic data from the U.S. Census Bureau. The process included standardization of FIPS codes to ensure consistent geographic matching, systematic treatment of missing values, and the selection of relevant explanatory variables.

### Phase II: Corpus Construction
* **`02b_cleaning_speeches.ipynb`**: Processing of Nomination Acceptance Speeches. Removal of non-verbal transcriptions (e.g., audience applause), stop-word filtering, and tokenization.
* **`02c_cleaning_manifestos.ipynb`**: Extraction and cleaning of Party Platforms (Manifestos) to ensure a comprehensive representation of political ideology beyond oral rhetoric.

### Phase III: Exploratory Data Analysis (EDA)
* **`03_descriptive.ipynb`**: Statistical profiling of US counties. Implementation of **K-Means Clustering** to identify distinct socio-economic archetypes (e.g., "Urban/Educated" vs. "Rural/Industrial").

### Phase IV: Baseline Predictive Modeling
* **`04_ml.ipynb`**: Development of baseline supervised learning models (Logistic Regression, Random Forest) using exclusively socio-economic features.
    * (County-level binary classification: Democrat vs. Republican).

### Phase V: NLP Feature Extraction
* **`05_nlp.ipynb`**: Application of **TextBlob** to compute `Sentiment` (-1 to +1) and `Subjectivity` (0 to 1) scores for the constructed corpus. Aggregation of scores by party and election cycle.

### Phase VI: Data Integration
* **`06_final_merge.ipynb`**: Merging of Micro and Macro datasets. Engineering of **interaction terms** (e.g., `Unemployment_Rate * Sentiment_Differential`) to model the conditional effects of rhetoric.

### Phase VII: Advanced Modeling & Inference
* **`07_advanced_combine_model.ipynb`**:
    * GridSearch optimization of hyperparameters.
    * Feature Importance analysis (SHAP/Gini importance).
    * **Structural Break Analysis:** Comparison of feature weights Pre-2016 vs. Post-2016.



## 4. Key Findings


1.   Models based solely on county-level socio-economic and demographic variables exhibit strong predictive performance, confirming that U.S. voting behavior is largely structured by persistent local characteristics (e.g. population density, education, racial composition).

2.   The inclusion of NLP-derived sentiment and subjectivity measures yields limited improvements in aggregate predictive accuracy. However, interaction terms suggest that rhetorical tone may condition voting behavior in specific contexts, particularly in economically vulnerable counties.

3.  Model comparisons indicate a shift in the relative importance of explanatory variables after 2016. Traditional economic indicators lose weight, while education and demographic composition become more dominant predictors, consistent with a broader cultural and identity-based realignment of the electorate.

## 5. Technical Requirements

To replicate this analysis, the following Python libraries are required:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn textblob plotly
```

## 6. Author

**Jessica Bourdouxhe and Xavier Foidart**
* **Context:** Submitted as part of DataManagement class at HEC Liège.
* **Date:** 14 January 2026
* **Contact:** Jessica.Bourdouxhe@student.uliege.be  |  Xfoidart@student.uliege.be 
