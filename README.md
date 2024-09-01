 # **Real Estate Price Prediction ,Analysis and Recommendation System**

## **Overview**

This project is a comprehensive solution for analyzing and predicting property prices in Gurgaon, India. The application is built using various machine learning models and is deployed as an interactive web application using Streamlit. The key features include data collection via web scraping, extensive data preprocessing, feature engineering, model building and evaluation, visualization, and deployment of an analytics page, a recommendation system, and a price prediction tool.

[Watch the Streamlit UI walkthrough video](https://github.com/user-attachments/assets/88b268aa-00cc-46a1-af9a-93fbc64f2717)

## **Project Structure**

- **Data Collection**: Web scraping techniques were used to gather data on flats, houses, and apartments in Gurgaon.
- **Data Preprocessing**: The collected data was cleaned and preprocessed using various techniques like outlier detection, missing value imputation, and feature selection.
- **Feature Engineering**: Additional features were created to enhance model performance and accuracy.
- **Model Building**: Multiple machine learning algorithms were employed, including:
  - Linear Regression
  - Support Vector Regression (SVR)
  - Ridge and Lasso Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - Extra Trees Regressor
  - Gradient Boosting Regressor
  - AdaBoost Regressor
  - MLP Regressor
  - XGBoost Regressor
- **Model Evaluation**: The models were evaluated using various metrics, with XGBoost achieving the highest accuracy of 90.10% after hyperparameter tuning.
- **Visualization**: Used Plotly and Seaborn to create insightful visualizations for data analysis.
- **Deployment**: The final application was deployed using Streamlit, featuring three main components:
  1. **Analytics Page**: Provides insights and plots various charts for data analysis.
  2. **Recommendation System**: Recommends properties based on similarity scores.
  3. **Price Prediction**: Predicts property prices based on user inputs.

## **Installation**

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/real-estate-project.git
   cd real-estate-project
   ```

2. **Create a Virtual Environment**:
   ```bash
   conda create --name estate python=3.8
   conda activate estate
   ```

3. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

## **Usage**

### **1. Analytics Page**
   - **Description**: Explore various insights and visualizations about the real estate data.
   - **Features**:
     - Sector-wise price per square foot geomap.
     - Word cloud of property features.
     - Area vs. Price scatter plots.
     - BHK distribution pie charts.
     - Side-by-side price comparisons and distribution plots.

### **2. Recommendation System**
   - **Description**: Recommends similar properties based on selected criteria using a combination of cosine similarity matrices.
   - **Usage**: 
     - Select a location and radius to search for nearby properties.
     - Recommend similar apartments based on the selected apartment name.

### **3. Price Prediction**
   - **Description**: Predicts property prices based on user inputs using trained machine learning models.
   - **Usage**:
     - Input details like property type, sector, number of bedrooms, bathrooms, and more.
     - Get an estimated price range for the property.

## **Project Highlights**

- **Data Collection**: Web scraping from real estate websites.
- **Advanced Preprocessing**: Outlier detection, missing value imputation, and feature selection.
- **Machine Learning Models**: Utilized a variety of regression models with hyperparameter tuning.
- **Interactive Visualizations**: Created with Plotly and Seaborn.
- **Streamlit Deployment**: Seamless deployment with user-friendly interface.

## **Contributing**

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## **Contact**

If you have any questions or feedback, feel free to contact me at [pradeepdubey8446@gmail.com](mailto:pradeepdubey8446@gmail.com).

---

Feel free to customize the content to better suit your project and preferences!




Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
