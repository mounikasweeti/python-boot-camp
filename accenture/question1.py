#you are comprting in a basketball contest.In thiscontest the score for each successful shot depends on both the distance from the basket and the player position.the ball
#is shot N times successfully.you are given an array A containing the distance of a player from basket for N shots The index of array represents the position of the player 
#the score is calculated bu multiplying the position with the distance from the basket
#your task is to find and return an integer value,representing the maximum possible score you ca achieve by choosing a contigous subarray of size k from the array

#input of array
#str_arr=input().split("")
#arr = list(map(int,str_arr)) map is used to convert any datatype into integer
#print(arr)
#print(type(arr))
#n=int(input())
#k=int(input())
#
# * A subarray is a contiguous part of array.
#
# * Assume 1 based indexing.
#
# * The array contains both negative and positive values.
#
# * Assume the player is standing on a cartesian plane.
#
# Input Format
#
# - input1: An integer value N representing the number of shots made by the player
# - input2 : An integer K representing the size of subarray
# - input3 : An array of integers
#
# Sample Input
#
# N = 5
# K = 2
# distance values: 1 2 3 4 5
# index values:    1 2 3 4 5
# Samp
n=5
k=3
arr = [9,2,5,3,7]
ans=32
for i in range(n-k+1):
 sub_arr=arr[i:i+k]
 sum = 0
#arr=list(map(int, input().split(" ")))
for ind in range(1, k+1):
    sum+= sub_arr[ind-1] * ind
    if sum>ans:
       ans=sum
print(ans)