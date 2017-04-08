from random import randint
nouns = ['cat','dog','fish','eagle','student','ninja','soldier']
adjectives = ['Good','New','First','Last','Long','great','little','own','other'
              ,'old','right','big','high','different','small','large','next'
              ,'early','young','important','few','public','bad','same','able'
              ,'adorable','beautiful','handsome','magnificent','sparkling'
              ,'gifted','clever','brave','mysterious','obnoxious','gigantic'
              ,'sweet','hot']

print("Here is your code name: ")
f = True
while(f):
    index = index = randint(0,len(adjectives)-1)
    print(adjectives[index], end=" ")
    index = randint(0,len(nouns)-1)
    print(nouns[index])
    choice = input("You Liked It? 'Y' or 'N'")
    if(choice == 'Y' or choice == 'y'):
        f = False
    print("No worries :) Here Is Another: ")