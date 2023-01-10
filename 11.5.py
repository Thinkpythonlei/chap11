string1 = "abcd"
string2 = "dcba"
def is_reverseword(string1,string2):
    list1 = list(string1)
    list1.reverse()
    string3 = ''.join(list1)
    if string3==string2:
         print("string1 and string2 is reverse word")
    else:
         print("string1 and string2 is not reverse word")
print(is_reverseword(string1,string2))


with open("C:\words.txt",encoding="utf-8") as fin:
    content=fin.readlines()
new=[]
for i in content:
    first=i.strip("\n")
    new.append(first)


def is_rotate(new,d):
    for word in new:
        if word in new:
            print(word,word[::-1])


# def rotate_word(txt):
#     fin = open(txt)
#     t = []
#     for word in fin:
#         t.append((word.strip())[::-1])
#     return t
#
#
# def read_file(txt):
#     fin = open(txt)
#     d = dict()
#     for word in fin:
#         d[word.strip()] = 1
#     return d
#
#
# def is_rotate(t, d):
#     print('rotational word is:')
#     for word in t:
#         if word in d:
#             print(word, word[::-1])
#
#
# txt = 'words.txt'
# is_rotate(rotate_word(txt), read_file(txt))





