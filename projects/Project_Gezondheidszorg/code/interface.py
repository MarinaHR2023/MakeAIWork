"""Interface for health_app"""
# imports
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)
