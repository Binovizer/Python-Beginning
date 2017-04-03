import random
sentence = input("Enter the sentence: ")
word_list = sentence.split(" ")
for word in word_list:
    if(len(word) > 3):
        flag = ''
        if(word[-1] == '.'):
            word = ''.join(list(word[:-1]))
            flag = '.'
        char_list = list(word[1:-1])
        random.shuffle(char_list)
        shuffled = ''.join(char_list)
        final_word = word[0] + shuffled + word[-1] + flag
        print(final_word,end=" ")
    else:
            print(word,end=" ")