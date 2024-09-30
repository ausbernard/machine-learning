# Table of Contents
1. [Fundamentals](#fundamentals)
   1. [Artificial Intelligence](#artificial-intelligence)
   1. [Large Language Models](#large-language-models)
   1. [Types of Intelligence](#types-of-intelligence)
      1. [General Intelligence](#general-intelligence)
      1. [Specialized Intelligence](#specialized-intelligence)
   1. [Machine Learning](#machine-learning)
      1. [Full Machine Learning Cycle](#full-machine-learning-cycle)
      1. [Finding the Balance](#finding-the-balance)
      1. [Bias Variance Tradeoff](#bias-variance-tradeoff)
      1. [Training Sets vs Validation Set vs Test Set](#training-sets-vs-validation-set-vs-test-set)
      1. [Metrics](#metrics)
          1. [Accuracy](#accuracy)
          1. [Precision](#precision)
          1. [Recall (Sensitivity)](#recall-sensitivity)
          1. [F1-Score](#f1-score)
          1. [Mean Squared Error (MSE)](#mean-squared-error-mse)
   1. [Importing CSV](#importing-csv)
      1. [Using Pandas](#using-pandas)
      1. [Built-in CSV Module](#built-in-csv-module)
      1. [Numpy](#numpy)
      1. [C](#c)
   1. [SQL](#sql)
   1. [Summary Table](#summary-table)

# Fundamentals
### Artificial Intelligence

a product that combines principles from computer science, data science, and statistics to create very specialized algorithms. Simple, can we train an AI application that can "learn" and grow more "intelligent"? We use this application to solve complex problems and ultimately gain more value to our company thus shareholders.

#### Main Problems to Solve
1. **Complex identification (classification)**: involves supplying data to a computer so that it can assign a label that data.
1. **Prediction (regression):** The method to make predictions about future events, in which analyzes historical data to make future predictions. Classification chooses a prediction for a label, regression will calculate a number within a range. For example, weather forecasting.
1. **Knowledge organization (clustering):** Is similar to the "human way" of organizational clustering where you have data points and the goal is to group similar data points together based on their characteristics and features. Now instead of the person organizing the data a computer would use a clustering algorithm to find the patterns, groups, and connections between the data points without a human specifying in advance what to look for.
    - (ML) example: music streaming services could use this to group similar users together to more accurately make recommendations.
1. **Computer vision:** Pretty simple, the main goal is to *see* what is in an image and extract useful information from it. It uses a combination of the concepts above to automate tasks that are achievable through the use of human vision

### Large Language Models

are a specific type of AI models that have been trained using huge volumes of text (often billions of words). They are designed to generate a text response to a prompt as realistically as if you were speaking to a human by predicting which words come next in a sentence. - ChatGPT and CoPilot are examples.

### Types of Intelligence
#### General intelligence
Competence in a wide variety of intellectual tasks
#### Specialized intelligence 
Competence in a specific intellectual task. This is the new wave of intelligence where the scope of the task is much smaller so that program can be extremely competent. And I want to be apart of that.

### Machine Learning
Consists of 4 types of learning:
- **Supervised Learning**: A type of machine learning where the model is trained on labeled data. The algorithm learns to map input data to the correct output based on the provided labels. Examples include classification and regression tasks.
    - **Common Metric Evaluations Used:**
        - **Classification Algorithms**
            1. Precision
            2. Accuracy
            3. Recall (sensitivity)
            4. F-1 Score
        - **Regression Algorithms (Predictive Methods)**
            - Mean Absolute Error (MAE)
            - Mean Squares Error (MSE)
            - Root Mean Squared Error (RMSE)
            - R-squared
    - **Linear Regression**: (Predictive) Use for predicting house prices based on features like size, location, etc. Used for predicting a continuous target variable based on one or more input features.
    - **Logistic Regression**: (Predictive) Use for spam detection in emails. Used for binary classification that predicts the probability of a binary outcome.
    - **Decision Trees**: Customer segmentation. A tree-like model used for both classification and regression tasks. It splits the data into subsets based on the value of input features.
    - [Random Forest](algorithms/random-forest.py): Used for predicting loans. Ensemble method that combines multiple decision trees to improve accuracy and reduce overfitting
    - **Support Vector Machines (SVM**): Use for image classification tasks. It finds the hyperplane that best separates the classes in the feature space.
    - [k-Nearest Neighbors (k-NN)](algorithms/k-nearest.py): Use for recommender systems. Non parametric method used for classification and regression. It predicts the target value based on the k-nearest neighbors in the feature space.
    - **Naive Bayes**: Use for text classification. Probabilistic classifier based on Bayes' theorem with the assumption of independence between features.
    - **Gradient Boosting Machines (GBM)**: Use for predicting customer churn. An ensemble method that builds models sequentially each correcting the errors of the previous one.
    - **Neural Networks**: Used for Image Recognition, natural language processing. Models inspired by human brains, used for complex tasks. They consist of layers of interconnected nodes (neurons). 
  
- **Unsupervised Learning**: A type of machine learning where the model is trained on unlabeled data. The algorithm tries to find hidden patterns or intrinsic structures in the input data. Examples include clustering and dimensionality reduction.
    - Common Metric evaluations for clustering algorithms: 
        - Silhouette Score - Measures how similar an object is to its own cluster compared to other clusters. The score ranges from -1 to 1, where a higher value indicates better-defined clusters. 
    - Clustering Algorithms
        - K-means Clustering: Use for customer segmentation, image compression. Partitions data into K clusters, where each data point belongs to the cluster with the nearest mean.
        - Dimensionality Reduction Algorithms
            - Principal Component Analysis (PCA): Reduces the dimensionality of the data by transforming it into a new set of variables (principal components) that are uncorrelated and capture the maximum variance.Use Case: Data visualization, noise reduction.

- **Reinforcement Learning**: A type of machine learning where an agent learns to make decisions by performing actions in an environment to maximize cumulative reward. The agent learns from the consequences of its actions through trial and error. Examples include game playing and robotic control.

- **Neural Networks**: A type of machine learning model inspired by the structure and function of the human brain. Neural networks consist of layers of interconnected nodes (neurons) that process input data to make predictions. They are used in various tasks such as image recognition, natural language processing, and more.

### Full Machine Learning Cycle

| Stage                    | Description                                                                                   |
|--------------------------|-----------------------------------------------------------------------------------------------|
| **Problem Definition**   | **Identity the Problem** <br>Clearly define the problem we want to solve <br> **Set Objectives** <br> Determine the goals and success criteria our the project.                                       |
| **Data Collection**      | **Gather Data** <br> Gather the data required for the problem. Some ways are relational databases, API's, legal web scraping, web traffic logs off http servers, etc. <br> **Store Data** <br>Store that collected data in a structured format, such as a database or data warehouse.                                                   |
| **Data Preparation**     | **Data Cleaning** <br> Establish a process to will clean our data. Each data set is different and will require a different cleansing program. Manual or automated process that generally includes: <br>• handling missing values <br> • removing duplicates <br>• correcting invalid data (outside of normal range) <br> • correcting format inconsistencies. <br> **Transform Data** <br> Normalize, scale, or encode data, as needed. <br> **Re-Visit Data** <br> (Optional), but clean data is so important and that is re-visiting the data source and the process to make sure our data input and output are clean for our models. <br> **Feature Engineering** <br> Create new features from existing data to improve model performance. <br> **Split Data** <br> Split the data into training, validation, and test sets. <br>We do not want to use all our data for training, this leads to overfitting the model. *Another way in which overfitting can be avoided is by splitting the training data and test data into different combinations of sets, to train several different models.*                                                        |
| **Exploratory Data Analysis (EDA)** | **Visualize Data**<br>Visualize the data with plots and charts to understand data distributions and relationships. <br> **Statistical Analysis**<br> Perform statistical tests to gain further insights into the data.                                                               |
| **Model Selection**      | **Choose Algorithm**<br>Choose the appropriate algorithms based on the problem type (classification or regression). <br> **Build Baseline Model**<br>Build the base - building the baseline model to compare against more complex models.                                                 |
| **Model Training**       | **Train Models**<br> In the data prep, the process of splitting the data is important for this step. Here is where we use our different data combination sets to train multiple models and find the most optimized model for our problem. <br>**Hyperparameter Tuning**<br> Use techniques like grid search or random search to optimize hyperparameters. Tweaking all the wheels and engines to make the care go faster. Finding the best combination to make it go fastest.                                                     |
| **Model Evaluation**     | **Evaluate Models**<br>Evaluate models using appropriate metrics. Such as accuracy, precision, recall, f1-score, or mean squared error. <br> **Cross-Validate**<br> Use cross-validation to ensure the model generalizes well to unseen data. Ensure our model works well with data it hasn't seen before.                                                   |
| **Model Selection**      | **Select Best Model**<br>Select the model that performs the best on our validation set during Model Evaluation. <br> **Ensemble Methods**<br> Where we consider combining multiples models if it will improve performance.                 |
| **Model Deployment**     | **Model Serialization** <br> Save the trained model using formats like Pickle or ONNX.<br> **Deploy Model**<br> Deploy the model to production using tools like Flask, FastAPI, or a cloud service such as Google AI Platform.                        |
| **Monitoring and Maintenance** | **Monitor Performance**<br> Continuously monitor the model's performance in production. <br> • Track key performance metrics(ie: accuracy, precision, and recall) on new data.<br> • Setup automated alerts via pager duty for significant drops in performance.<br>**Update Model**<br>Retrain and update the model as new data becomes available. <br> **Statistical Tests** <br> Use statistical tests like the *Kolmogorov-Smirnov test* or *Chi-Square test* to detect changes in the distribution of input features or target variable. <br> **Detect & Address Model Drift**<br> Detect and address model drift to maintain accuracy over time. Model drift occurs when the statistical properties of the target variable or the input features change over time, leading to a decrease in model performance. <br> • Retrain the model<br> •Incremental Learning - using algorithms that support incremental learning <br>  • Feature Engineering - updating new features to capture the newness in the data <br>  • Model Selection - consider using different models to ensemble methods that might be more robust<br>                                |

---
<br>

### Finding the Balance

- **High Bias**: Increase model complexity (e.g., add more nodes to a tree model).
- **High Variance**: Reduce model complexity or use techniques like cross-validation.

In neural network & tree models:
- **Underfitting**: Increase training time and complexity.
- **Overfitting**: Indicates the model has trained too long or is too complex, capturing noise in the training data rather than the underlying pattern.


### Bias Variance Tradeoff

The goal is to find a balance where the model captures the data distribution well without overfitting.
**Bias** = Difference between our expected value and where we are estimating (accuracy).

**Variance** = The spread of where you want to be.

**🎯 =** Low Bias and Low Variance

Unfortunately, in reality, this is something that is very hard to achieve and the aim is to find a trade off between bias and variance. This happens when you have a low in either bias or variance, the tradeoff comes into play.

We can look at this in terms of error (y) and complexity (x). Bias decreases as model complexity increases. For example, a tree model with only 3 nodes will have high error due to low complexity. Increasing the number of nodes to 800 reduces bias, but this comes at a cost. Higher complexity can lead to overfitting, where the model performs well on training data but poorly on test data. This is the bias-variance tradeoff.

Initially, with low complexity, the model has high bias and low variance. As complexity increases, bias decreases, but variance increases. The goal is to find a balance where the model captures the data distribution well without overfitting.

To correct high bias, you can increase model complexity (e.g., add more nodes  to our Tree Model). However, this may increase variance. In neural networks, underfitting can be addressed by increasing training time and complexity. Overfitting, on the other hand, indicates the model has trained too long or is too complex, capturing noise in the training data rather than the underlying pattern (sensitive to the training data).

*Method 1: Watch how our Model Learns*
```
One method to find the right balance, watch how our model learns. At first, errors will go down for both training and test data. But if the model learns too much from the training data (overfitting), errors on the test data will start to go up. Stop training just before this happens. This is called the sweet spot.
```

*Method 2: Split Data*
```
Another way to avoid overfitting is to split your data into different sets and train several models. Choose the one with the best accuracy. Don't use all your data for training; always keep some aside for testing. Using all data for training can lead to overfitting.
```
### Training Tests vs Validation Set vs Test Set
**Training Sets**: This is a set of data that is set aside for what your model trains on.

**Validation Sets**: Is the data used to determine if your model can learn further or if it is overfitting.

**Test Sets**: Is used to test the generalization errors. How good will our model perform on data it hasn't seen. 

### Metrics
#### Accuracy
The ratio of correctly predicting instances to the total instance.
- Formula: Accuracy = (True Positives + True Negatives) / Total Instances
- Use Case: Best used when the classes are balanced
- Tradeoff: High accuracy might hide the fact that the model is biased towards the majority class in imbalanced datasets.

#### Precision
The ratio of correctly predicted positive instances to the total predicted positive instances.
- Formula: Precision = True Positives / (True Positives + False Positives)
- Use Case: Important when the cost of False Positives is high
- Tradeoff: High precision can lead to high bias if the model is too conservative in predicting positives
- you’re picking apples from a tree. If you pick 5 apples and 4 of them are really good (that’s your true positives) but 1 apple is bad (that’s your false positive), precision helps us figure out how many of the apples you picked were actually good.

#### Recall (Sensitivity)
The ratio of correctly predicted positive instances to all actual positives.  
- Formula: Recall = True Positives / (True Positives + False Negatives).
- Use Case: Important when the cost of False Negatives is high.
- Tradeoff: High recall can lead to high variance if the model is too lenient in predicting positives.
- kid: If there are 10 lost animals (that's all the animals that need to be found) and the superhero finds 7 of them, recall helps us see how good the superhero is at their job.
#### F1-Score
The harmonic mean of precision and recall. In general, higher F1-Scores indicate better performance (ranges 0-1).

On average, a good F1-Score is typically around 0.7 to 0.8. Scores above 0.8 are considered very good, while scores below 0.5 might indicate poor performance. The acceptable range can vary depending on the specific application and context.
- Formula: F1-Score = 2 * (precision * recall) / (precision + recall)
- Use Case: Useful when you need to balance precision and recall.
- Tradeoff: Balances the tradeoff between precision and recall, but might not reflect the true performance if the classes are imbalanced.
#### Mean Squared Error (MSE)
The average of the squares of the errors between predicted and actual values. A good MSE is usually low, which means your throws are close to the target. If it’s high, it means you missed a lot. In machine learning, we use MSE to see how well a model is predicting things, like guessing the price of a toy based on its features!
- Formula: MSE = (1/n) * Σ (Predicted_i - Actual_i)²
- Use Case: Commonly used on regression tasks.
- Tradeoff: High MSE reflects a high variance, while a low MSE might indicate high bias if the model is too simple (High error, low complexity - Starting phase usually).

<br>

| Metric       | Definition                                                                                   | Tradeoff (Bias)                                                                 | Tradeoff (Variance)                                                             |
|--------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Accuracy** | Ratio of correctly predicted instances to total instances                                    | High bias if the model is too simple                                            | High variance if the model overfits the training data                           |
| **Precision**| Ratio of correctly predicted positives to total predicted positives                          | High bias if the model is too conservative in predicting positives              | High variance if the model predicts too many positives, including false positives|
| **Recall**   | Ratio of correctly predicted positives to all actual positives                               | High bias if the model misses many positives                                    | High variance if the model captures most positives but also many false positives |
| **F1-Score** | Harmonic mean of precision and recall                                                        | High bias if both precision and recall are low                                  | High variance if precision and recall are high on training data but not on test data|
| **MSE**      | Average of the squares of the errors between predicted and actual values                     | High bias if the model is too simple                                            | High variance if the model overfits the training data                           |
\

### Importing CSV
#### Using Pandas
Powerful and flexible data manipulation library that provides easy-to-use data structures and data analysis tools.

*with file*
```python
import pandas as pd

# Load CSV file into a DataFrame
df = pd.read_csv('file.csv')

# Display the first few rows of the DataFrame
print(df.head())
```
*with url*
```python
import pandas as pd

# Load CSV file from a URL into a DataFrame
url = 'https://example.com/file.csv'
df = pd.read_csv(url)

# Display the first few rows of the DataFrame
print(df.head())
```
#### Built-in CSV Module
```python
import csv

# Load CSV file into a list of dictionaries
with open('file.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

# Display the first few rows
print(data[:5])
```
csv module with `csv.reader`
```python
import csv

# Load CSV file into a list of lists
with open('file.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    data = [row for row in csv_reader]

# Display the first few rows
print(data[:5])
```
#### Numpy
library for numerical computing in Python, which can also be used to read CSV files.
```python
import numpy as np

# Load CSV file into a NumPy array
data = np.genfromtxt('file.csv', delimiter=',', dtype=None, names=True, encoding='utf-8')

# Display the first few rows
print(data[:5])
```
#### C
```c
<TBD>
```
### SQL

SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. Here are some fundamental concepts and commands in SQL:

*Creating a Table*
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);
```
*Inserting Data*
```sql
INSERT INTO employees (id, first_name, last_name, age, department)
VALUES (1, 'John', 'Doe', 30, 'Engineering');
```
*Selecting Data*
```sql
Select * FROM employees;
```
*Update Data*
```sql
UPDATE employees
SET age = 31
WHERE id = 1;
```
*Deleting Data*
```sql
DELETE FROM employees
WHERE id = 1;
```
*Filtering Data*
```sql
SELECT * FROM employees
WHERE department = 'Engineering';
```
*Sorting Data*
```sql
SELECT * FROM employees
ORDER BY last_name ASC;
```
*Joining Tables*
```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments (department_id, department_name)
VALUES (1, 'Engineering');
```
```sql
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
JOIN departments ON employees.department = departments.department_name;
```
*Aggregating Data*
```sql
SELECT department, COUNT(*) AS num_employees
FROM employees
GROUP BY department;
```

**Summary Table**

| Command        | Description                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| `CREATE DATABASE` | Creates a new database.                                                                     |
| `CREATE TABLE`    | Creates a new table with specified columns and data types.                                  |
| `INSERT INTO`     | Inserts new data into a table.                                                              |
| `SELECT`          | Retrieves data from a table.                                                                |
| `UPDATE`          | Updates existing data in a table.                                                           |
| `DELETE`          | Deletes data from a table.                                                                  |
| `WHERE`           | Filters data based on specified conditions.                                                 |
| `ORDER BY`        | Sorts data in ascending or descending order.                                                |
| `JOIN`            | Combines rows from two or more tables based on a related column.                            |
| `GROUP BY`        | Groups rows that have the same values in specified columns into summary rows.               |
<br>
<br>

| Category       | Details                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------|
| **Array List** |                                                                                                         |
| Pros/Cons      | **Pros**: How many elements we want to store. And don't plan or modifying the array. O(1) time space complexity<br>**Cons**: Problematic either in terms of time complexity (rebuilding the backing array as we need to grow it) or in terms of space complexity (allocating more space than we need just in case). |
| Scenario Time  | **find**: if the array sorted and used binary search worst case is O(log n)<br>**insert/remove**: are always O(n) because we will always have to iterate over the (n) list and do the operation |
| Algorithms     | **Sorting**:<br>- Bubble Sort<br>- Selection Sort<br>- Insertion Sort<br>- Merge Sort<br>- [Quick Sort](work-python/data_structures/array/quick_sort.py)<br>**Searching**:<br>- [Linear Search](work-python/data_structures/array/linear_search.py)<br>- [Binary Search](work-python/data_structures/array/binary_search.py)<br>**Other**:<br>- Two-Pointer Technique<br>- Sliding Window Technique<br>- Kadane's Algorithm<br>- Prefix Sum |