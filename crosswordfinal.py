import random
#global variables
points=0
#creating questions
floatq="real numbers and are written with a decimal point dividing the integer and fractional parts. "
whileq = "a looping structure that will loop untill a condition is true"
ifq = "this structure allows us to to check if a condition is true or false"
booleanq = "this data type only returns true or false"
doubleq = "a larger form of the float data type"
operatorsq = "theses are required to do mathmatic operations" 
stringq = "a list a characters concatinated together"
slicingq = "this is used to creat a substring form a given starting point to end point of a string" 
indexq = "the position of a charicter in a string is its what?"
#lists for questions and answers
answer = ""
question_list = [floatq,whileq,ifq,booleanq,doubleq,operatorsq,stringq,slicingq,indexq ]
answer_list = ["float","while","if","boolean","double","operators","string","slicing","index"]
#creating my puzzle
puzzle = ("fjvfloatdyyopxedninsmspfycnnalxeaeeukgeislufryprlcabeeiagco"+
          "ibuclqttbongojlivxobgadmyahgerjstringwvrs")
#functions

####################################################  
#display puzzle function
def display_puzzle(puzzle):
    line1="0 | "
    line2="1 | "
    line3="2 | "
    line4="3 | "
    line5="4 | "
    line6="5 | "
    line7="6 | "
    line8="7 | "
    line9="8 | "
    line10="9 | "
    for i in  range(len(puzzle)):
        if i<10:
            line1 += puzzle[i]+" | "
        elif i<20:
            line2 += puzzle[i]+" | "
        elif i<30:
            line3 += puzzle[i]+" | "
        elif i<40:
            line4 += puzzle[i]+" | "
        elif i<50:
            line5 += puzzle[i]+" | "
        elif i<60:
            line6 += puzzle[i]+" | "
        elif i<70:
            line7 += puzzle[i]+" | "
        elif i<80:
            line8 += puzzle[i]+" | "
        elif i<90:
            line9 += puzzle[i]+" | "
        else:
            line10 += puzzle[i]+" | "
    print("  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
    print("-------------------------------------------")
    print(line1)
    print("-------------------------------------------")
    print(line2)
    print("-------------------------------------------")
    print(line3)
    print("-------------------------------------------")
    print(line4)
    print("-------------------------------------------")
    print(line5)
    print("-------------------------------------------")
    print(line6)
    print("-------------------------------------------")
    print(line7)
    print("-------------------------------------------")
    print(line8)
    print("-------------------------------------------")
    print(line9)
    print("-------------------------------------------")
    print(line10)
    print("-------------------------------------------")

####################################################        
#ask question function
def question(question_list,answer_list ):
    attempts=10
    global points
# gets a random question and the answer to match
    x= random.randrange(len(question_list))
    question = question_list[x]
    answer = answer_list[x]
    while True:
#get the users answer check to see if its corect and removes question from list if correct
        responce = input(question)
        if responce == answer:
            print("thats correct")
            del question_list[x]
            del answer_list[x]
            score=1*attempts
            points+=score
            return answer
        else:
            attempts-=1
            print("thats not right try again")

####################################################            
#find word function
def findword(answer, puzzle):
    attempts=10
    global points
    while True:
        display_puzzle(puzzle)
        index_pos =""
        found_word =""
        positions = input("enter the letters positions for "+answer+" seperated by a , and end the list of positions with a ,")
#creats the index positions to build the new word
        for i in (positions):
            if i ==",":
                x=int(index_pos)
                found_word = found_word + puzzle[x]
                index_pos = ""
                continue
            index_pos = index_pos+i
#check to make sure you found the correct word
        if found_word == answer:
            score=1*attempts
            points+=score
            print ("thats correct")
            break
        else:
            attempts-=1
            print("try again")
            
####################################################          
#main function       
def main( question_list,answer_list, answer, puzzle):
    global points
    print("Python terms trivia word search game")
    while len(question_list) >0:
        print("Score: ",points)
        x = question(question_list,answer_list, )
        answer = x
        findword(answer, puzzle)
    print("great job you found them all")
#################################################### 
#start game
main(question_list,answer_list, answer, puzzle)
