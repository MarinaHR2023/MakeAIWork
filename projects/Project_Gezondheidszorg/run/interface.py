"""Interface for health_app"""
# imports
import pickle
import logging

"""Opens pickle file"""
with open("reg.pkl", "rb") as f:
    reg = pickle.load(f)

"""Asks for input and controls this proces"""
def input_digit(message, acceptableRange):
    inputStr = str()
    withinRange = False
    numberOfTries = 3
    i = 0

    while not (inputStr.isdigit() and withinRange) and i < numberOfTries:
        inputStr = input(message)

        if inputStr.isdigit():
            inputNum = float(inputStr)


            if inputNum in acceptableRange:
                return inputNum

        i += 1
        if i < 3:
            print("Ongeldige invoer. \n",
                  f"U kunt het nog {3-i} keer proberen voordat het programma stopt.")
        else:
            print('Uw invoer wordt niet geaccepteerd. Het programma stopt.')

# -------------------

"""Prints Welcome message"""
def welcome():
    print('Welkom bij de lifespan calculator. \n',
          'deze calculator berekent na invoer van gegevens: \n',
          '- de verwachte levensduur van de patient, \n',
          '- de bmi van de patient, \n',
          '- de premiefactor van en het kortingspercentage voor de patient.\n',
          'LET OP: deze calculator beoogt slechts een indicatie te geven van \n',
          'de levensverwachting en biedt geen zekerheden daaromtrent. \n')

# -------------------

""" Calculates bmi """
def calc_bmi(leng, mas):
    divider = pow(leng/100, 2)
    bmi22 = round(mas/divider)
    logging.debug(f'bmi: {bmi22}')
    return bmi22

# -------------------

""" Predicts lifespan """
def lifespan_predict(gen1, leng1, mas1, ex1, smok1, alc1, sug1, res_bmi):
    lifespan_pred = reg.predict([[gen1, leng1, mas1, ex1, smok1, alc1, sug1, res_bmi]])
    lifespan_pred = round(lifespan_pred[0])
    print(f"De voorspelde levensduur van deze patient is: {lifespan_pred} jaar")
    print('')
    return lifespan_pred

# -------------------

""" Checks in which bmi-range patients bmi is """
def bmi_check (real_age1, result_bmi1):
    if real_age1  < 70 and result_bmi < 18.5:
        print(f"Gelet op leeftijd ({real_age1}) en bmi ({result_bmi1}): \n",
              "patient heeft ondergewicht.")
    elif real_age1  < 70 and result_bmi1 <= 25.0:
        print(f"Gelet op leeftijd  ({real_age1}) en bmi ({result_bmi1}): \n",
              "patient heeft een gezond gewicht.")
    elif real_age1  >= 70 and result_bmi1 < 22:
        print(f"Gelet op leeftijd ({real_age1}) en bmi ({result_bmi1}): \n",
              "patient heeft ondergewicht.")
    elif real_age1  >= 70 and result_bmi1 < 28:
        print(f"Gelet op leeftijd  ({real_age1}) en bmi ({result_bmi1}): \n",
              "patient heeft een gezond gewicht.")
    elif result_bmi1 <=30.0:
        print(f"De bmi is {result_bmi1}: patient heeft overgewicht.")
    else:
        print(f"De bmi is {result_bmi1}: patient heeft ernstig overgewicht.")
    return None

# ---------
""" Calculates PremiumFactor and DiscountPercentage """
def calc_premiumfactor(gen1, lifesp1):
    pf = round(gen1 / lifesp1, 2)
    discPerc = round(1 - pf,2)*100
    print(f"De PremieFactor is: {pf}.")
    if discPerc > 0:
        print(f"Het discountpercentage is {discPerc}%. U krijgt korting.")
    else:
        print(f"Het discountpercentage is {discPerc}%.")
        discPerc = abs(discPerc)
        print(f"De verzekeringspremie stijgt met {discPerc}%.")
    return None

# ++++++++ ///// ++++++++ ///// ++++++++ ///// ++++++++ ///// ++++++++ /////+++++++

#=============Output: welcome
welcome()
print('')
#=============Asking for input + converts minutes to hours (exercise)

# acceptableRange realAge
acceptableRangerealAge = range(18, 116)
realAge = int(input_digit("Wat is de leeftijd in hele jaren (tussen 18 - 115): ", acceptableRangerealAge))
# acceptableRange genetic
acceptableRangeGen = range(64, 102)
genetic = int(input_digit("Wat is de genetische leeftijd in hele jaren (tussen 64 - 101)? ", acceptableRangeGen))
# acceptableRange length
acceptableRangeLen = range(154, 215)
length = int(input_digit("Wat is de lichaamslengte in centimeters (tussen 154 - 214)? ", acceptableRangeLen))
# acceptableRange mass
acceptableRangeMass = range(50, 165)
mass = int(input_digit("Wat is het lichaamsgewicht in hele kilo's (tussen 50 - 164)? ", acceptableRangeMass))
# acceptableRange exercise
acceptableRangeEx = range(0, 331)
exercise1 = int(input_digit("Hoeveel minuten beweging per dag (tussen 0 - 330)? ", acceptableRangeEx))
exercise = exercise1/60
# acceptableRange smoking
acceptableRangeSmok = range(0, 24)
smoking = int(input_digit("Hoeveel sigaretten per dag (tussen 0 - 23)? ", acceptableRangeSmok))
# acceptableRange alcohol
acceptableRangeAlc = range(0, 7) 
alcohol = int(input_digit("Hoeveel glazen alcohol per dag (tussen 0 - 6)? ", acceptableRangeAlc))
# acceptableRange sugar
acceptableRangeSug = range(0, 15) 
sugar = int(input_digit("Hoeveel suikerklontjes per dag (tussen 0 - 14)? ", acceptableRangeSug))

#============= calculating bmi_result
result_bmi = calc_bmi(length, mass)
print('')
#============= predicting lifespan

pred_lifespan = lifespan_predict(genetic, length, mass, exercise, smoking, alcohol, sugar, result_bmi)

#============= Output: bmi-communication
bmi_check(realAge, result_bmi)
print('')
print("LET OP!! De bmi is minder geschikt voor: \n",
    "* heel gespierde personen, \n",
     "* zwangere vrouwen, \n",
     "* vrouwen die borstvoeding geven, of \n",
     "* mensen van Aziatische afkomst.\n",
      "(BRON: Voedingscentrum) \n",
     "")
print('')
#=============Output: PremiumFactor & Discount communication

print("Hieronder volgen de PremieFactor en het Discountpercentage. \n",
       "Een negatief Discountpercentage leidt tot een premieverhoging.")
calc_premiumfactor(genetic, pred_lifespan)
print('')


