# Bloom-Box
This project is designed to demonstrate the fundamental workflow of a Classification task in Machine Learning. It covers data loading, model training, performance evaluation, and interactive user inference.
Key Features:
Built-in Dataset: Uses scikit-learn's Iris dataset (no external CSV required).
Predictive Logic: Implements a Decision Tree algorithm for clear, rule-based classification.
Live User Input: Features an interactive command-line interface where users can input their own flower measurements.
Performance Metrics: Automatically calculates and displays model accuracy upon execution.
🛠️ Tech Stack
Language: Python 3.x
Libraries: * scikit-learn: For model training and data splitting.
pandas: For data structure representation.
📊 How It Works
The application follows a 4-step Machine Learning workflow:
Data Splitting: The data is divided into a Training Set (80%) to teach the model and a Testing Set (20%) to validate its accuracy.
Training: The DecisionTreeClassifier analyzes the training data to find patterns (e.g., "If petal width < 0.8cm, it is always a Setosa").
Validation: The model makes predictions on the test set, comparing its guesses against the actual labels to calculate accuracy.
Inference: The script pauses to allow user input, feeding those custom values back into the trained model for a real-time result.


📈 Example Result
Plaintext


-----------------------------------------
ML Model Trained. Accuracy: 100.00%
Target Species: setosa, versicolor, virginica
-----------------------------------------

--- Predict a Flower Species ---
1. Enter Sepal Length: 5.1
2. Enter Sepal Width: 3.5
3. Enter Petal Length: 1.4
4. Enter Petal Width: 0.2

>>> RESULT: This flower is likely a SETOSA!







