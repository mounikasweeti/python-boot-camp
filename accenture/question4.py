#max is plannning to take part in a diwali contest at a diwali party that will begin at 8pm and will run until midnight(12AM) 
#i.e for four hours.he also needs to travel to the party venye within this time which takes him p minutes The contest comprises
#of N problems that are arranged in order of difficulty with problems 1 being the simplest and problem N being the post diffficulty 
# with problem 1 being the simplest and problem N being the post difficult.
# Max is aware that he will require 5*i minutes to solve the ith problem.
#your task is to help max find and return an integer value representing the number of problems Max can solve and reach the party 
#venue within the given time frame of four hours
n=int(input())
travel_time = int(input())
time_remaining=240-travel_time
count=0
for i in range(1,n+1):
    solve_time=i*5
    if solve_time<time_remaining and time_remaining>0:
        count+=1
        time_remaining-=solve_time
    else:
        break
print(count)
