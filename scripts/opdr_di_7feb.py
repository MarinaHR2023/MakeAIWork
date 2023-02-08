""" Opdrachten dinsdag 7 februari 2023"""
#Write a program that computes and prints the result of the following expression. 
# It is roughly .1017. 
#print((512-282)/((47*48+5)))B

#Ask the user to enter a number. Print out the square of the number, 
# but use the sep optional argument to print it out in a full sentence that ends in a period. 
#getal = int(input('Geef een getal: '))
#print(f'Het kwatdraat van {getal} is {getal*getal}.')

#Write a program that generates a random number, x, between 1 and 50, 
# a random number y between 2 and 5, and computes xy.
#import random
#x = random.randrange(1, 51)
#y = random.randrange(1, 51)
#print(f'X heeft de waarde {x} en Y heeft de waarde {y}. X * Y = {x*y}')

#Write a program that asks the user to enter two numbers, x and y, and computes |x-y|/(x+y).
#getal1= int(input('Geef een eerste getal: '))
#getal2= int(input('Geef tweede getal: '))
#print('|x-y|/(x+y) = ', abs(getal1-getal2)/(getal1+getal2))

#Write a program that asks the user to enter a string. The program should then print the following:
#The total number of characters in the string 
word = (input('Geef een woord: '))
print(f'Het woord {word} bevat {len(word)} lettertekens.')
#The string repeated 10 times 
print (f'{word} ' *10)
#The first character of the string (remember that string indices start at 0)
print(f'De eerste letter van {word} is: {word[0]}')
#The first three characters of the string
print(f'De eerste 3 letters van {word} zijn: {word[0:3]}')
#The last three characters of the string
print(f'De laatste 3 letters van {word} zijn: {word[-3:]}')
#The string backwards
print(f'Het woord {word} achterstevoren gespeld is: {word[::-1]}')
#The seventh character of the string if the string is long enough and a message otherwise
if len(word)>=7:
    print(f'De zevende letter van het woord {word} is {word[6]}')
else: 
    print(f'Het woord {word} is niet lang genoeg om de zevende letter te kunnen printen.')
#The string with its first and last characters removed
print(f'Het woord {word} zonder de eerste en laatste letter luidt: {word[1:-1]}')
#The string in all caps
print(f'Het woord {word} in hoofdletters:  {word.upper()}')
#The string with every a replaced with an e

print(f'Het woord {word} waarin elke a wordt vervangen wordt voor een e: ', word.replace('a','e'))

#The string with every letter replaced by a space

word1 = word.lower()
word2 = ""
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in word1:
    if i in abc:
        word2 += " "

    else:
        word2 = word2 + i
print( 'x',word2,'x')


word1 = word.lower()
word2 = ""
for i in word1:
    if i.isalpha():
        word2 += " "
    else:
        word2 = word2 + i
print( 'x',word2,'x')

word6 = word
for i in word6:
    if i.isalpha():
        word6.replace(i," " )
print( 'x',word6,'x')
