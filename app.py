# Simple Meter Bill Prediction (No ML library)

print("⚡ Simple Meter System")

# Take input
units = float(input("Enter electricity units: "))

# Simple logic (₹5 per unit)
rate_per_unit = 5
bill = units * rate_per_unit

print("Estimated Bill Amount: ₹", int(bill))