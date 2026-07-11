#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Grade Evaluator Program
# This program asks for a student's name and score,
# checks if the score is valid, assigns a grade,
# gives a remark, and displays the results.

# Ask for the student's name
name = input("Enter your name: ")

# Ask for the student's score
score = int(input("Enter your score: "))

print("\n========== RESULT ==========")

# Check if the score is valid
if score < 0 or score > 100:
    print("Invalid score! Please enter a score between 0 and 100.")

else:
    print("Student:", name)

    if score >= 80:
        grade = "A"
        remark = "Excellent"

    elif score >= 70:
        grade = "B"
        remark = "Very Good"

    elif score >= 60:
        grade = "C"
        remark = "Good"

    elif score >= 50:
        grade = "D"
        remark = "Needs Improvement"

    else:
        grade = "Fail"
        remark = "Work Hard"

    print("Score :", score)
    print("Grade :", grade)
    print("Remark:", remark)
    print("==========================")


# In[ ]:




