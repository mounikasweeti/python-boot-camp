# Prime factors of a positive integer are the prime numbers that divide that integer exactly.
# Given an array arr of n integers and a positive integer num.
# Let's suppose prime factorization of num is:  pa x qb x rc x .... x zf   ,where p,q,r...z are prime numbers.
# Sum of numbers in array arr at indices of prime factors of number num is: a x arr[p] + b x arr[q] + c x arr[r] +...... + f x arr[z].
# Sum of numbers in array arr at indices of prime factors of number num is: a x arr[p] + b x arr[q] + c x arr[r] +...... + f x arr[z].
# You are given an array arr of size n and a positive integer num. You are required to calculate the sum of numbers in arr as mentioned above, and print the same.
# Note:
# If arr is empty, print -1.
# If prime factor of num not found as indices, print 0.
# Input Format:
# The input consists of three lines:
#
# The first line contains an integer, i.e. n.
# The second line contains an array arr of length of n.
# The third line contains an integer num
# The input will be read from the STDIN by the candidates.
# Output Format:
# Print the sum that was mentioned in the problem statement.
def solution(arr, num):
    primes = []
    if len(arr) == 0:
        return -1
    for i in range(2,num+1):
        while num%i == 0:
            primes.append(i)
            num = num//i
    if num > 2:
        primes.append(num)
    ans= 0
    for i in primes:
        if i < len(arr):
            ans += arr[i]
        else:
            return 0
    return ans

#arr = [11,21,32,45,1,23]
#num = 21

#ans = solution(arr, num)
#print("Answer is:",ans)