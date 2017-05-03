from random import randint

def printList(guessed_word_list, spacing=''):
    for c in guessed_word_list:
        print(c,end=spacing)
    print()

words = ['dracula','dragon','different', 'whale', 'Fjord', 'Gazebo'
         ,'flower','new','Awkward','Bagpipes','Banjo','Bungler'
         ,'Croquet','Crypt','Dwarves','Fervid','Fishhook', 'Gypsy'
         ,'Haiku','Haphazard','Hyphen','Ivory','Jazzy', 'Jiffy'
         ,'Jinx','Jukebox','Kayak','Kiosk', 'Klutz','Memento'
         ,'Mystify', 'Numbskull','Ostracize', 'Oxygen','Pajama'
         ,'Phelgm', 'Pixel', 'Quad', 'Quip', 'Rogue', 'Toady']

word = words[randint(0, len(words)-1)].lower();
word_list = list(word)
print("Lets Play Hangman...")
guess_count = 7
try:
    guess_count = int(input("How many guesses you want for your game: "))
    if(guess_count >= 10):
        print("na munna na...10 se jada guesses nahi milege...")
        guess_count = 10
    print("You have %d guesses." %guess_count)
except Exception:
    print("Abe no dalna tha dhakkan.")
    print("Le ab %d se kam chala : "%guess_count)
    print()

print("Try to guess the following word: ")
coded_word_list = []
for i in range(len(word_list)):
    coded_word_list.append('-')
printList(coded_word_list);
guessed_word_list = []
while(guess_count > 0 and '-' in coded_word_list):
    guess = ''
    guess = input("\n\nEnter single character: ").lower()
    count = 0
    while len(guess) != 1:
        count += 1
        if(count > 2):
            print("Abe dhakkan samajh ni aata kya ek dal ek.")
            guess = input('dal ab :').lower()
        else:
            guess = input('Please Enter one character at a time :').lower()
    
    if(guess in word_list):
        while(guess in word_list):
            index = word_list.index(guess)
            coded_word_list[index] = guess
            word_list[index] = '0'
        
        printList(coded_word_list)
        print("You have %d guesses left." %guess_count)
    elif(guess in guessed_word_list):
        print("You already made that guess. Try another Character.")
        printList(coded_word_list)
        print("You have %d guesses left." %guess_count)
        continue
    else:
        print("Sorry! Wrong Guess.")
        guess_count -= 1
        printList(coded_word_list)
        print("You have %d guesses left." %guess_count)
    guessed_word_list.append(guess)
    if('-' not in coded_word_list):
        print("Yipeee! You guessed it Right. You won!")
    if(guess_count == 0):
        print("Sorry! Not the word we wanted.")
        print("Correct Word Was : ",word)
    print("Guessed Characters : ", end='')
    printList(guessed_word_list, spacing=' ')