from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Load the famous Iris dataset
iris = datasets.load_iris()
X = iris.data  # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Target: species (0=setosa, 1=versicolor, 2=virginica)

print("Dataset Shape:", X.shape)
print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("\nFirst 5 samples:")
print(X[:5])
print("First 5 labels:", y[:5])

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nTraining set size: {len(X_train)}")
print(f"Testing set size: {len(X_test)}")

# Standardize features (important for many algorithms)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train a K-Nearest Neighbors classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# Make predictions
y_pred = knn.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.2%}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Example: Predict a new flower
new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])  # Measurements of a new iris
new_flower_scaled = scaler.transform(new_flower)
prediction = knn.predict(new_flower_scaled)
print(f"\nNew flower prediction: {iris.target_names[prediction[0]]}")
print(f"Prediction probabilities: {knn.predict_proba(new_flower_scaled)[0]}")
