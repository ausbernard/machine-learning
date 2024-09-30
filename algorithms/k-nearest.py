# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Comments Only
'''
# Load the Iris dataset

# Split the dataset into training and testing sets
# 80% of the data will be used for training, and 20% for testing

# Initialize the k-NN classifier with k=3
# k is the number of nearest neighbors to consider

# Train the k-NN classifier on the training data

# Predict the labels for the test data

# Calculate the accuracy of the model

# Print the accuracy

# Example of predicting the class of a new sample

# Print the predicted class for the new sample
'''


# Function to calculate the Euclidean distance between two points
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# k-NN classifier class
class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = [self._predict(x) for x in X_test]
        return np.array(predictions)

    def _predict(self, x):
        # Calculate distances between x and all examples in the training set
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Sort by distance and return indices of the first k neighbors
        k_indices = np.argsort(distances)[:self.k]
        # Extract the labels of the k nearest neighbor training samples
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # Return the most common class label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
# 80% of the data will be used for training, and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the k-NN classifier with k=3
# k is the number of nearest neighbors to consider
knn = KNeighborsClassifier(n_neighbors=3)
knn = KNNClassifier(n_neighbors=3)

# Train the k-NN classifier on the training data
knn.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = knn.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print(f"Accuracy: {accuracy:.2f}")

# Example of predicting the class of a new sample
new_sample = np.array([[5.0, 3.6, 1.4, 0.2]])
predicted_class = knn.predict(new_sample)

# Print the predicted class for the new sample
print(f"Predicted class for the new sample: {predicted_class[0]}")