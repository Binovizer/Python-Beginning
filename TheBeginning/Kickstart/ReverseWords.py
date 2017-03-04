n = int(input())
for i  in range(n):
    list_of_words = [x for x in input().split(sep=" ")]
    no_of_words = len(list_of_words)
    print("Case #%d: " %(i+1), end="")
    for i in range(no_of_words):
        print(list_of_words[no_of_words-i-1], end=" ")
    print()