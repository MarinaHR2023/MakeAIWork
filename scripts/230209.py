# #Define the number eleven​
# number = 11
# #Define the devider
# devider = 3
# #As long as result is larger than zero:​
# while number > 0:
# #Ingesprongen: Subtract three​

#     number = number -3
# # Check if number is zero or not​

# if number == 0:
#     #Ingesprongen: print result​

#     print('Number is divisible by 3')
# else:
#     print('Number is NOT divisible by 3')


# print('We gaan kijken of een getal deelbaar is door een ander getal.')
# teller = int(input('Geef het getal op dat je wilt delen: '))
# noemer = int(input(' Geef het getal op waardoor het je eerder gegeven getal wilt delen: '))
# while teller > 0:
#     teller = teller - noemer
#     if teller%noemer == 0:
#             print (f"{teller} is deelbaar door {noemer}.")
#     else:
#     print(f'{teller} is NIET deelbaar door {noemer}.')


#TEL HOEVEEL KLINKERS IN EEN BEPAALD WOORD ZITTEN
# # Define the string “paard”
# word = input("Give a word: ")
# # Define counter
# counter = 0
# # Loop over each letter in string:
# for char in word:

# 	# Check if character is vowel:
# 	if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
# 		# If so then increment counter
#          counter = counter + 1
# # Print result
# print(f"The word {word} contains {counter} vowels" )

#Alarm: LAAT EEN WEKKER NA 5 SECONDEN AFGAAN
#Importeer een module die de tijd bijhoudt
import time 
# Define a counter and set to five
seconds = 5
# As long as counter is not zero:
while seconds > 0:
    print('Tick')
	# Decrement counter
    seconds = seconds -1
	# Sleep for one second
    time.sleep(1)
# Make beep sound
print ("Beep - Beep - Beep")
print ("\a")



