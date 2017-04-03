import random
import re
sentence = input("Enter the sentence: ")
word_list = sentence.split(" ")
for word in word_list:
    if(re.search("'", word)):
        index = word.find("'");
        if(len(word) > 5):
            new_str = ''.join(list(word[1:-1]))
            splitted_list = list(new_str.split("'"))
            new_word = splitted_list[0] + splitted_list[-1]
            new_list = list(new_word)
            random.shuffle(new_list)
            new_list.insert(index-1, splitted_list[1]);
            final_word = ''.join(new_list)
            print(word[0] + final_word + word[-1], end=" ")
        else:
            print(word,end=" ")
    else:
        if(len(word) > 3):
            char_list = list(word[1:-1])
            random.shuffle(char_list)
            shuffled = ''.join(char_list)
            final_word = word[0] + shuffled + word[-1]
            print(final_word,end=" ")
        else:
            print(word,end=" ")