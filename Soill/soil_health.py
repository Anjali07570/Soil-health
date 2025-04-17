import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import pickle

# Load dataset
df = pd.read_csv("soil_data.csv")

# Handle missing values
df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    df.loc[:, col] = df[col].fillna(df[col].mode()[0])

# Encode categorical variables
df = pd.get_dummies(df)

# Split dataset into features (X) and target variable (y)
X = df.drop(columns=["SoilHealth"])  # Assuming 'SoilHealth' is the target column
y = df["SoilHealth"]

# Save feature names
joblib.dump(X.columns, "model_features.pkl")  # ✅ Save feature names

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Machine Learning Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
joblib.dump(model, "soil_health_model.pkl")
print("Model saved as soil_health_model.pkl ✅")

# Save the trained model using pickle
with open("soil_health_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("Model saved successfully!")

# ✅ Save the feature names separately
joblib.dump(X.columns.tolist(), "model_features.pkl")
print("Feature names saved as model_features.pkl ✅")
