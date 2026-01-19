import pickle
import numpy as np

print("⚡ Smart Meter ML System")

# Load trained ML model
with open("meter_model.pkl", "rb") as f:
    model = pickle.load(f)

# Take user input
units = float(input("Enter electricity units: "))

# Convert input for ML model
units_array = np.array([[units]])

# Predict bill
predicted_bill = model.predict(units_array)

print("Estimated Bill Amount: ₹", int(predicted_bill[0]))
