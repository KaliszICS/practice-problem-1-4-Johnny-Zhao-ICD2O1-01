'''
    Practice Questions: Input and F strings
    Author: Johnny Zhao
    Date Created: Sept 19, 2024
    Date Last Modified: Spet 19, 2024
'''

def q1():
  word = input("Input a word: ")
  print(word)
  #asking the user to input a word, outputting the word back to them

def q2():
  nameQ2 = input("Input your first name: ")
  print("Hello " + nameQ2)
  #asking the user to input their first name, outputting "hello" then their first name

def q3():
  nameQ31 = input("Input your first name: ")
  nameQ32 = input("Input your last name: ")
  fullname = f"{nameQ32} {nameQ31}"
  print(fullname)
  #asking the use to input their first name then last name, outputting thme both using f string

def q4():
  nameQ41 = input("Input a student: ")
  nameQ42 = input("Input another student: ")
  students = f"Your students are {nameQ41} and {nameQ42}"
  print(students)
  #asking the user for two student names, then outputting the student names in a sentence using f strings

#Do not edit code below this comment

#q1()
#q2()
#q3()
#q4()