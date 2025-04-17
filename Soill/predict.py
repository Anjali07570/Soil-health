import joblib
import pandas as pd

# Load trained model
model = joblib.load("soil_health_model.pkl")
feature_names = joblib.load("model_features.pkl")  # Load feature names used during training

# Function to take user input
def get_user_input():
    print("\nEnter Soil Parameters for Prediction:\n")
    pH = float(input("Enter pH value: "))
    Nitrogen = int(input("Enter Nitrogen level: "))
    Phosphorus = int(input("Enter Phosphorus level: "))
    Potassium = int(input("Enter Potassium level: "))

    # Soil type selection
    soil_types = ["Clay", "Loam", "Sandy"]
    print("\nSelect Soil Type:")
    for i, soil in enumerate(soil_types, 1):
        print(f"{i}. {soil}")

    soil_choice = int(input("Enter Soil Type (1/2/3): "))
    soil_features = {"SoilType_Clay": 0, "SoilType_Loam": 0, "SoilType_Sandy": 0}
    soil_features[f"SoilType_{soil_types[soil_choice - 1]}"] = 1  # Set selected soil type to 1

    # Crop selection
    crop_types = ["Barley", "Corn", "Rice", "Soybean", "Wheat"]
    print("\nSelect Crop Type:")
    for i, crop in enumerate(crop_types, 1):
        print(f"{i}. {crop}")

    crop_choice = int(input("Enter Crop Type (1/2/3/4/5): "))
    crop_features = {"Crop_Barley": 0, "Crop_Corn": 0, "Crop_Rice": 0, "Crop_Soybean": 0, "Crop_Wheat": 0}
    crop_features[f"Crop_{crop_types[crop_choice - 1]}"] = 1  # Set selected crop to 1

    # Combine all inputs
    user_input = {
        "pH": [pH],
        "Nitrogen": [Nitrogen],
        "Phosphorus": [Phosphorus],
        "Potassium": [Potassium],
    }
    user_input.update(soil_features)
    user_input.update(crop_features)

    return pd.DataFrame(user_input)

# Get user input
df_input = get_user_input()

# Ensure input matches model feature names
df_input = df_input.reindex(columns=feature_names, fill_value=0)

# Make prediction
prediction = model.predict(df_input)[0]

# Display result
print("\n🔍 **Prediction Result:**")
print(f"🟢 Soil Health Status: {'Healthy' if prediction == 1 else 'Unhealthy'}\n")
