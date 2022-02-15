# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
#print(student_scores)
#print(type(student_scores))

#count = 0
#for x in student_scores:
#  count = count + 1

#for n in range(0, count-1):
  #student_scores[n] = int(student_scores[n])
 # student_scores[n] = int(student_scores[count-1])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#This code is for highest scores
#highest_score = 0
#for score in student_scores:
#  if score > highest_score:
#    highest_score = score
#print(f"The highest score in the class is {highest_score}")
  

#highest_score = lowest_score

  #else:
   # print(min(student_scores)

# This portion of code is doing the same task as min function
lowest_score = student_scores[0]
for score in student_scores:
  if score < lowest_score:
    lowest_score = score 
  
   # and score < highest_score:
print(f"The lowest score in the class is {lowest_score}")


  #else:
   # print("Keep")

# max_value > value 
#print(max_value)

# Max function 

#print(max(student_scores))

#Min function 
#print(min(student_scores))


#lowest_score = 0
#for score in student_scores:
 # if lowest_score < score:
  #   score = lowest_score
#print(f"The lowest score in the class is {lowest_score}")
