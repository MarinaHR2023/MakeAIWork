"""Interface for health_app"""
# imports
import pickle
import logging


with open("reg.pkl", "rb") as f:
    reg = pickle.load(f)

# Ask for the values of all features
genetic = float(input('Vul de genetische leeftijd in: '))
length = float(input('Vul de lengte in centimeters in: ')) 
mass = float(input ("Vul het lichaamsgewicht in hele kilo's in: "))
alcohol = float(input("Vul het aantal glazen alcohol per dag in: "))
sugar = float(input("Vul het aantal suikerklontjes per dag in: "))
smoking = float(input("Vul het aantal sigaretten per dag in: "))
exercise = float(input("Vul het aantal uren beweging per dag in: "))

# Calculate bmi
divider = pow(length/100, 2) if length >0 else None
bmi = round(mass/divider)
logging.debug(f'bmi: {bmi}')


lifespan_predict = reg.predict([[genetic, length, mass, alcohol, sugar, smoking, exercise, bmi]])
print(f"The bmi of this patient is: {bmi}")
print(f"The predicted lifespan of this patient is: {lifespan_predict}")
