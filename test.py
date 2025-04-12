#!/usr/local/bin/python3


print('Hello world')

text = "Marcin Jarota"

print (text)
print (len(text))

mylist = ["AaBbCc","45655","xx",99,99.9]
print ("Lenght of myList: ", len(mylist))
print ("Lenght of myList[0]: ",len(mylist[0]))
print ("Lenght of myList[1]: ",len(mylist[1]))
print ("Lenght of myList[2]: ",len(mylist[2]))

print(type(text))

for x in mylist:
  print(x, "|", type(x), "|", x.upper(), "|", x.lower())
  if x == "xx":
    break
  
print ("|---- END -------|")

print(text)
text = text.replace('Jarota', 'C++')
print(text)
text = text.upper()
print(text)
text = text.lower()
print(text)
