# Fundamentals
**Artificial Intelligence** is a product that combines principles from computer science, data science, and statistics to create very specialized algorithms. Simple, can we train an AI application that can "learn" and grow more "intelligent"? We use this application to solve complex problems and ultimately gain more value to our company thus shareholders.

**Large Language Models** are a specific type of AI models that have been trained using huge volumes of text (often billions of words). They are designed to generate a text response to a prompt as realistically as if you were speaking to a human by predicting which words come next in a sentence. - ChatGPT and CoPilot are examples.

**General intelligence —** Competence in a wide variety of intellectual tasks
**Specialized intelligence —** Competence in a specific intellectual task. This is the new wave of intelligence where the scope of the task is much smaller so that program can be extremely competent. And I want to be apart of that.

**Machine Learning** consists of 4 types of learning:
- supervised learning
- unsupervised learning
- reinforcement learning
- neural networks

**Full Cycle of Building a Machine Learning Application/Model from Conception to Production Deployment & Monitoring/Maintenance**

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

Formula: 

\[
\text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Instances}}
\]


#### Precision
#### Recall (Sensitivity)
#### F1-Score
#### Mean Squared Error (MSE)

<br>

| Metric       | Definition                                                                                   | Tradeoff (Bias)                                                                 | Tradeoff (Variance)                                                             |
|--------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **Accuracy** | Ratio of correctly predicted instances to total instances                                    | High bias if the model is too simple                                            | High variance if the model overfits the training data                           |
| **Precision**| Ratio of correctly predicted positives to total predicted positives                          | High bias if the model is too conservative in predicting positives              | High variance if the model predicts too many positives, including false positives|
| **Recall**   | Ratio of correctly predicted positives to all actual positives                               | High bias if the model misses many positives                                    | High variance if the model captures most positives but also many false positives |
| **F1-Score** | Harmonic mean of precision and recall                                                        | High bias if both precision and recall are low                                  | High variance if precision and recall are high on training data but not on test data|
| **MSE**      | Average of the squares of the errors between predicted and actual values                     | High bias if the model is too simple                                            | High variance if the model overfits the training data                           |
\
### SQL

SQL (Structured Query Language) is a standard language for managing and manipulating relational databases. Here are some fundamental concepts and commands in SQL:

*Creating a Table*
```
CREATE TABLE employees (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);
```
*Inserting Data*
```
INSERT INTO employees (id, first_name, last_name, age, department)
VALUES (1, 'John', 'Doe', 30, 'Engineering');
```
*Selecting Data*
```
Select * FROM employees;
```
*Update Data*
```
UPDATE employees
SET age = 31
WHERE id = 1;
```
*Deleting Data*
```
DELETE FROM employees
WHERE id = 1;
```
*Filtering Data*
```
SELECT * FROM employees
WHERE department = 'Engineering';
```
*Sorting Data*
```
SELECT * FROM employees
ORDER BY last_name ASC;
```
*Joining Tables*
```
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

INSERT INTO departments (department_id, department_name)
VALUES (1, 'Engineering');
```
```
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
JOIN departments ON employees.department = departments.department_name;
```
*Aggregating Data*
```
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