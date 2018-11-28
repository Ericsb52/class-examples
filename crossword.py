attempts=0

print("Python terms")
puzzle = ("fjvfloatdyyopxedninsmspfycnnalxeaeeukgeislufryprlcabeeiagco"+
          "ibuclqttbongojlivxobgadmyahgerjstringwvrs")
def display_puzzle():
    print("  0123456789")
    print("0 "+puzzle[0:10])
    print("1 "+puzzle[10:20])
    print("2 "+puzzle[20:30])
    print("3 "+puzzle[30:40])
    print("4 "+puzzle[40:50])
    print("5 "+puzzle[50:60])
    print("6 "+puzzle[60:70])
    print("7 "+puzzle[70:80])
    print("8 "+puzzle[80:90])
    print("9 "+puzzle[90:])
    print()
    
print()

#display the puzle
display_puzzle()

print("word list")
word_list="float, while, if, boolean, double, operators, string, slicing, index"
print (word_list)
print()

#geting the lengths of the words
word1_length=len("float")
word2_length=len("while")
word3_length=len("if")
word4_length=len("boolean")
word5_length=len("double")
word6_length=len("operators")
word7_length=len("string")
word8_length=len("slicing")
word9_length=len("index")
#geting player answer
x=0
while x==0:
    word1= input("enter the index positions of float")
    attempts+=1
    i=0
    foundword=""
    while i < word2_length:
        index=word1[i]
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=1
    if foundword == "float":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")



display_puzzle()
x=0
while x==0:
    word2= input("enter the index positions of while")
    attempts+=1
    i=0
    foundword=""
    while i < word2_length*2:
        index1=word2[i]
        index2=word2[i+1]
        index=index1+index2
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=2
    if foundword == "while":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")

display_puzzle()
x=0
while x==0:
    word3= input("enter the index positions of if")
    attempts+=1
    i=0
    foundword=""
    while i < word3_length*2:
        index1=word3[i]
        index2=word3[i+1]
        index=index1+index2
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=2
    if foundword == "if":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")

display_puzzle()
x=0
while x==0:
    word4= input("enter the index positions of boolean")
    attempts+=1
    i=0
    foundword=""
    while i < word4_length*2:
        index1=word4[i]
        index2=word4[i+1]
        index=index1+index2
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=2
    if foundword == "boolean":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")

display_puzzle()
x=0
while x==0:
    word5= input("enter the index positions of double")
    attempts+=1
    i=0
    foundword=""
    while i < word5_length*2:
        index1=word5[i]
        index2=word5[i+1]
        index=index1+index2
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=2
    if foundword == "double":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")

display_puzzle()
x=0
while x==0:
    word6= input("enter the index positions of operators")
    attempts+=1
    i=0
    foundword=""
    while i < word6_length*2:
        index1=word6[i]
        index2=word6[i+1]
        index=index1+index2
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=2
    if foundword == "operators":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")

display_puzzle()
x=0
while x==0:
    word7= input("enter the index positions of string")
    attempts+=1
    i=0
    foundword=""
    while i < word7_length*2:
        index1=word7[i]
        index2=word7[i+1]
        index=index1+index2
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=2
    if foundword == "string":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")

display_puzzle()
x=0
while x==0:
    word8= input("enter the index positions of slicing")
    attempts+=1
    i=0
    foundword=""
    while i < word8_length*2:
        index1=word8[i]
        index2=word8[i+1]
        index=index1+index2
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=2
    if foundword == "slicing":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")

display_puzzle()
x=0
while x==0:
    word9= input("enter the index positions of index")
    attempts+=1
    i=0
    foundword=""
    while i < word9_length*2:
        index1=word9[i]
        index2=word9[i+1]
        index=index1+index2
        index=int(index)
        foundword =foundword+puzzle[index]
        i+=2
    if foundword == "index":
        print(foundword)
        print("great job")
        x=1
    else:
        print("thats not right try again")

print("you got them all great job and it onley took you "+ str(attempts)+" attempts" )
input("press enter to exit")
