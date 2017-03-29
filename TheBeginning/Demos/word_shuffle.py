import random
import itertools
word = input("Enter any word : ")
char_list = list(word[1:-1])
random.shuffle(char_list)
shuffled = ''.join(char_list)
final_word = word[0] + shuffled + word[-1]
print(final_word)
 
print("All combinations: ")
unique_words = set()

for w in itertools.permutations(char_list, len(char_list)):
    unique_words.add(''.join(w))

for uword in unique_words:
    print(word[0]+uword+word[-1])
    
print("Total : ",len(unique_words))