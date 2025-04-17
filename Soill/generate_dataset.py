import pandas as pd

# Sample dataset creation (modify as needed)
data = {
    "SoilType": ["Clay", "Sandy", "Loam", "Clay", "Sandy"],
    "Crop": ["Wheat", "Rice", "Corn", "Barley", "Soybean"],
    "pH": [6.5, 5.8, 6.2, 6.8, 5.5],
    "Nitrogen": [30, 20, 25, 28, 18],
    "Phosphorus": [12, 10, 14, 11, 9],
    "Potassium": [45, 50, 48, 42, 55],
    "SoilHealth": [1, 0, 1, 1, 0]  # 1 = Healthy, 0 = Unhealthy
}

df = pd.DataFrame(data)

# Save dataset
df.to_csv("soil_data.csv", index=False)
print("Dataset 'soil_data.csv' created successfully!")
