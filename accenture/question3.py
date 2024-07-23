#you are given an integer array of size N,representing jars of chocolates.
# Three students A<B<C respectively will pick hocolates one by one from each chocolate jar,till the jar is empty
#and then repeat the same with rest of the jars. your task is to fine and return an integer value representing the total 
#number of chocolates that student A will have after all the chocolates have been picked from all the jars
n=3
arr=[10,20,30]
total_cho_a=0
for box in arr:
    total_cho_a +=(box//3)
    if box%3!=0:
        total_cho_a+=1
print(total_cho_a)