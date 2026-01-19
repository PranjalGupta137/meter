import pickle
import numpy as np
import os

print("⚡ Smart Meter ML System")

# Check model file
model_path = "meter_model.pkl"

if not os.path.exists(model_path):
    print("❌ ERROR: meter_model.pkl file not found")
    exit()

# Load model safely
with open(model_path, "rb") as f:
    model = pickle.load(f)

units = float(input("Enter electricity units: "))

units_array = np.array([[units]])
prediction = model.predict(units_array)

print("Estimated Bill Amount: ₹", int(prediction[0]))
