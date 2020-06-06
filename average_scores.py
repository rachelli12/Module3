"""
Program: average_scores.py
Author: Rachel Li
Last date modified: 06/06/2020

The purpose of this program is to read in one person's name, first and last, age and three scores out of 100.
The program wants to find the average of the three scores.
"""
def average(score1, score2, score3):
    average_scores = (score1 + score2 + score3) / 3
    print('average: ', (score1 + score2 + score3) / 3)
    # declare variables. use score1, score2, score3 in calculation
    return average_scores

if __name__ == '__main__':
    #Get input for scores
    score1 = int(input('score 1: '))
    score2 = int(input('score 2: '))
    score3 = int(input('score 3: '))

    #Calculate average scores
    average_scores = average(score1, score2, score3)


    #User will input last name and first name here
    last_name = input("Last name: ")
    first_name = input("First name: ")

    #User will input age here
    age = input("age: ")

    #Print output
    #lastname, firstname age:? average grade: with .2precision
    print(f'{last_name}, {first_name} age: {age} average grade: {average_scores:.2f}')

#example output: Roriguez, Linda age: 21 average grade: 92.50
#Program output: Li, Rachel age: 19 average grade: 93.33


