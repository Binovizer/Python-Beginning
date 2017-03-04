def getNoOfUniqueChars(person):
    person = ("".join(sorted(person))).strip()
    prev = person[0];
    count = 1;
    for ch in person:
        if(ch == " "):
            continue
        if(ch != prev):
            prev = ch;
            count += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    persons = {}
    for j in range(n):
        person = input()
        no_of_unique_chars = getNoOfUniqueChars(person)
        persons.__setitem__(person, no_of_unique_chars)
    #print(persons)
    list_of_persons = [v[0] for v in sorted(persons.items(), key=lambda kv: (-kv[1], kv[0]))]
    #sorted_persons = sorted(persons.items(), key=operator.itemgetter(1), reverse = True)
    #print(sorted_persons)
    print("Case #%d: %s" % (i+1, list_of_persons[0]))