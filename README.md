# CLassification_logistics_regression
<br>
Author : Kanta Chaudhary
<br>

Iris flower Classification using logistic reression
<br>
# Project Overview
<br>
This project demonstrates a machine learning classification task using the Iris Flower dataset. The objective is to classify iris flowers into one of three species Setosa, Versicolor or Virginica based on four flower measurements : sepal length, sepal width, petal length and petal width.
<br>
The project follows a complete machine learning workflow, including data loading, preprocessing, feature scaling, model training, prediction, evalution and comparison with other classification algorithms.
<br>

# objective
o Load and explore this iris dataset.<br>
o Perform basic data preprocessing.<br>
o Split the dataset into training and testing sets.<br>
o Standardize numerical features.<br>
o Train a Logistic Regression classifier.<br>
o Evaluation the model using multiple performance metrics.<br>
o Compare the performance with Random Forest and Support Vector Machine(SVM).<br>
<br>
# Dataset
<br>
Dataset : Iris Dataset <br>
Features : <br>
o Sepal Length<br>
o Sepal Width<br>
o Petal Length<br>
o Petal Width<br>
<br>
Target Variables :<br>
o Species<br>
Classes : <br>
o Setosa<br>
o Versicolor<br>
o virginica<br>
Technologies Used <br>
o Python<br>
o Pandas<br>
o Matplotlib<br> 
o Scikit-learn<br>
<br>
Machine Learning Workflow <br>
1. Import the required libraries.<br>
2. Load the Iris dataset using Pandas.<br>
3. Explore the dataset structure.<br>
4. Check for missing values.<br>
5. Separate features (X) and target (Y).<br>
6. Split the dataset into training and testing sets.<br>
7. Standardize the features using StandarScaler.<br>
8. Train a Logistic Regression model.<br>
9. Predict species for the test dataset.<br>
10. Evaluate the model using : <br>
    o Accuracy<br>
    o Precision<br>
    o Confusion Matrix<br>
    o Classification Report<br>
11. Compare Logistic Regression with : <br>
    o Random Forest Classifier<br>
    o Support Vector Machine (SVM)<br>
Evaluation Metrics <br>
The project evaluates the classification model using : <br>
o Accuracy : Overall percentage of correct predictions.<br>
o Precision : Measures how many predicted instances are actually correct.<br>
o Recall : Measures how many actual instances are correctly identified.<br>
o Confusion Matrix : Display the number of correct and incorrect predictions for each class.<br>
o Classification Report : Provides Precision, Recall, F1-Score, and Support for each class.<br>
<br>
# Models Compared <br>
Model                          Purpose <br>
Logistic Regression             Primary classification model<br>
Random Forest                   Performance comparison<br>
Support Vector Machine          Performance comparison<br>
<br>
# Project Structure <br>
Vlassification_With_Logistics/<br>
|<br>
|- iris.csv <br>
|- main.py <br>
|_ README.md <br>
<br>
Results <br>
The Logistic Regression model successfully classification iris flowers with high accuracy. The project also compared its performance against Random Forest and SVM classifier, demonstrating how different machine learning algorithms perform on the same dataset.<br>

# Learning Outcomes <br>
Through this project, I learned : <br>
o Data Loading and exploration using Pandas.<br>
o Data preprocessing technoques.<br>
o Train-Test data splitting.<br>
o Feature scaling using StandardScaler.<br>
o Building a Logistic Regression Classifier.<br>
o Evaluating Classification models using multiple metrics.<br>
o Comparing Different machine learning algorithms.<br>
o Applying a complete machine learning workflow in python.<br>
<br>
# Future Improvements <br>
o Add data visualization using Seaborn and Matplotlib.<br>
o Perform hyperparameter tuning.<br>
o Save the Trained model using Joblib or Pickle.<br>
o Build a simple web interface for real-time predications.<br>
o Test the model on additional datasets.<br>
<br>
#Conclusion<br>
The project demonstrates a complete implementation of a classification problem using Logistic Regression. It covers the essential stages of a machine learning pipeline, form preprocessing to model evaluation, while also comparing the results with Random Forest and Support Vector Machine classifiers to better understand model performance.
