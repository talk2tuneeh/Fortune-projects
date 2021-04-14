'''my_string = "hello this is onumabor frotune in the building"

def sortLexo(my_string):
    words = my_string.split()
    words.sort()
    for i in words:
        print(i)'''


'''def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)

print(lexicographi_sort('w3resource'))'''


'''from itertools import chain,  groupby

test_list = ['Greeks', '5', 'for', 'Geeks', '2', '3']

num_group = groupby(test_list, key = str.isalpha)
both_group = [[''.join(i)] if j else list(i) for j, i in num_group]

res = list(chain.from_iterable(both_group))

print("The joined adjacent word list : " + str(res))'''


'''from itertools import permutations

str = 'bdhagefopq'

def lexicographical_permutation(str):
    perm = sorted(''.join(chars) for chars in permutations(str))
    for x in perm:
        print(x)'''


#sentence = input("Type your statement: ")
sentence = "to be or not to be"
sentence = sentence.split()
sentence.sort()

result = []
#for word in range(len(2)): [be be not or to]
    #print(word)
for word1 in sentence:
    for word2 in sentence:
        result.append(word1 + " " + word2)
result = set(result)
result = list(result)
print(len(result))

for item in result:
    spl = item.split()
    if spl[0] == spl[1] and sentence.count(spl[0]) < 2:
        result.remove(item)
    spl = spl[1] + " " + spl[0]
    if spl in result:
        result.remove(spl)

   
print(len(result))
print(result)

'''from itertools import combinations

letters = "to be or not to be"
a = combinations(letters, 2)
y = [''.join(i) for i in a]

for word in y:
    print(word)'''

#print(y)