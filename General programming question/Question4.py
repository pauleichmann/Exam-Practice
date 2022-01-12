'''
GeneralProgramming.py



Functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 40 (notice that each exercise has its own weight)


1 * weight points -  The program works flawlessly and the appropriate ideas to solve it, have been used.

0.75 * weight points - The student has understood the logic and the program works for most inputs.
The code could use some improvement or it is very hard to read. The appropriate ideas to solve the problem have been used.

0.5 * weight points - The student has understood the logic but there is some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

0.25 * weight points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).




'''

# Write a function that takes a string as parameter, which will contain single digit numbers, 
# letters, and question marks, and check if there are exactly 3 question marks 
# between every pair of two numbers, whose sum is 10. 
# If so, then your program should return the string true, otherwise it should return the string false. 
# If there aren't any two numbers then your program should return false 
# as well.
# Example1: input = "sdfhdsl4??sfasdfga?1sdjkfhbdsjhfkb" output = False (the two numbers do not sum to 10)
# Example2: input = "sdfhdsl4??sfasdfga?6sdjkfhbdsjhfkb" output = True (the two numbers sum to 10)
# weight = 8

def question_mark(input):

    list1 = ["0","1","2","3","4","5","6","7","8","9"]
    elementList = list(input)

    numberList = []

    for element in elementList:
        if element in list1: 
            numberList.append(element)
        else:
            pass        

    a = numberList[0]
    b = numberList[1]
    print(a,b)

    if int(a) + int(b) == 10: 
        sumflag = True 
    else:
        sumflag = False

    stringSplitt = input.split(a)
    stringSplitt2 = stringSplitt[1]
    stringSplitt3 = stringSplitt2.split(b)

    finalString = stringSplitt3[0]
    

    count = 0
    for element in finalString: 
        if element == "?":
            count += 1 
        else: 
            pass
    
    

    if count == 3:
        questionflag = True 
    else: 
        questionflag = False 
    

    if sumflag == True and questionflag == True: 
        return True
    else: 
        return False 

input = "sdfhdsl4??sfasdfga?1sdjkfhbdsjhfkb"
input2 = "sdfhdsl4??sfasdfga?6sdjkfhbdsjhfkb"

print(question_mark(input2))

