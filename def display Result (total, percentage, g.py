from unittest.util import _MAX_LENGTH


def displayresult (total, percentage, grade):      
print("Total Marks:", total)

print ("Percentage:", percentage)

print ("Grade:", grade)

def calcresult (ml,m2, m3,m4, m5):

total =_MAX_LENGTH + m2 + m3 + m4 + m5

percentage = (total /500)*100

if percentage >100: 
    grade = "Invalid Percentage"

elif percentage >=85:
      grade = "A Grade"

elif percentage >= 70:
      grade = " B Grade "

elif percentage >=55: 
    grade = "C Grade"

elif percentage >= 35:
      grade = "D Grade"
 else:

    grade = "FAIL"

return displayresult (total, percentage, grade)

def   getMarks():

eng= int (input ("Enter the marks of English: "))

math = int (input ("Enter the marks of Math: "))

hindi= int (input ("Enter the marks of Hindi: "))

sci = int (input ("Enter the marks of Science: "))

art = int(input ("Enter the marks of Arts: "))

return calcResult (eng, math,hindi,sci, art) 

getMarks ()