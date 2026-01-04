# ==========================================
# 1. SETUP: Import necessary libraries
# ==========================================
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ==========================================
# 2. DATA: Load and Prepare
# ==========================================
# Load the famous Iris dataset
iris = load_iris()
X = iris.data    # Features (Measurements)
y = iris.target  # Labels (Flower Species)

# Split into 80% Training and 20% Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# 3. TRAINING: Build the Model
# ==========================================
# We use a Decision Tree - it creates logical rules based on the measurements
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Calculate accuracy based on the test set
predictions = model.predict(X_test)
acc = accuracy_score(y_test, predictions)

print("-----------------------------------------")
print(f"ML Model Trained. Accuracy: {acc * 100:.2f}%")
print("Target Species: setosa, versicolor, virginica")
print("-----------------------------------------")

# ==========================================
# 4. INTERACTIVE: User Input for Prediction
# ==========================================
def get_user_prediction():
    print("\n--- Predict a Flower Species ---")
    try:
        # Collecting inputs from the user
        sl = float(input("1. Enter Sepal Length (e.g. 5.1): "))
        sw = float(input("2. Enter Sepal Width (e.g. 3.5): "))
        pl = float(input("3. Enter Petal Length (e.g. 1.4): "))
        pw = float(input("4. Enter Petal Width (e.g. 0.2): "))

        # Format the data for the model
        user_features = [[sl, sw, pl, pw]]
        
        # Make the prediction
        result_index = model.predict(user_features)[0]
        species_name = iris.target_names[result_index]

        print(f"\n>>> RESULT: This flower is likely a {species_name.upper()}!")
        
    except ValueError:
        print("\n[Error] Please enter numerical values (e.g., 5.1).")

# Run the input function
if __name__ == "__main__":
    get_user_prediction()