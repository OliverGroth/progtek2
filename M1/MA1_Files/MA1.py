"""
Solutions to module 1
Student: Oliver
Mail: oliver.groth.7974@student.uu.se
Reviewed by: Sorry forgot but it was by both in Datasal 4102
Reviewed date: 1st of April
"""

import random
import time


def power(x, n):         # Optional
    if n == 0:
        return 1
    elif n > 0:
        return x * power(x, (n - 1))
    elif n < 0:
        return power(x, (n + 1)) / x

def multiply(m, n):      # Compulsory
    if n == 0:
        return 0
    elif n > 0:
        return m + multiply(m, (n - 1))


def divide(t, n):        # Optional
    pass


def harmonic(n):         # Compulsory
    if n == 0:
        return 0
    elif n > 0:
        return 1 / n + harmonic(n - 1)



def digit_sum(x):        # Optional
    pass


def get_binary(x):       # Optional
    pass


def reverse(s):          # Optional
    pass


def largest(a):          # Compulsory
    if len(a) == 1:
        return a[0]
    else:
        if a[-1] <= a[-2]:
            return largest(a[0:-1])
        else:
            return largest(a[0:-2]+a[-1:])

#def count(x, s):         # Compulsory
#    if len(s) == 0:
#        return 0
#    else:
#        if s[0] == x:
#            return 1 + count(x, s[1:])
#        else:
#            return 0 + count(x, s[1:])

def count(x, s):         # Compulsory
    if len(s) == 0:
        return 0
    else:
        if type(s[0]) == list:
            if s[0] == x:
                return 1 + count(x,s[1:])
            else:
                return count(x, s[1:]) + count(x, s[0])
        else:
            if s[0] == x:
                return 1 + count(x, s[1:])
            else:
                return 0 + count(x, s[1:])



def zippa(l1, l2):       # Compulsory 
    if len(l1) >= 1 and len(l2) >= 1:
        return [l1[0]] + [l2[0]] + zippa(l1[1:], l2[1:])
    else:
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1


def bricklek(f, t, h, n): # Compulsory
    if n == 1:
        return [f + '->' + t]
    else:
        return bricklek(f, h, t, n - 1) + [f + '->' + t] + bricklek(h, t, f, n - 1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():

    # 16
    # 50 brickor, 1 sek per flytt,
    # Från Exempel 12 ser vi att resultatet är 2^n -1 vilket är i storleksordningen 10^15, lång tid, 35,7 Mår


    # 17
    for n in [1, 5, 10, 15, 20, 25, 30, 35, 40]:
        start = time.perf_counter()
        fib(n)
        end = time.perf_counter()
        print("Time for n = " + str(n) + "is: " + str(start - end))
    # ska såklart ha end - start egentligen menmen
    #Time for n = 1is: -6.43995008431375e-07
    #Time for n = 5is: -2.9080110834911466e-06
    #Time for n = 10is: -2.148799831047654e-05
    #Time for n = 15is: -0.00026374800654593855
    #Time for n = 20is: -0.002619339997181669
    #Time for n = 25is: -0.028410793005605228
    #Time for n = 30is: -0.30600535799749196
    #Time for n = 35is: -3.382382376003079
    #Time for n = 40is: -37.71176326600835

    # To verify we calculate time for n = 40 / time for n = 35 equals to 11.15 s, if we compare that to 1.618 ^ (40-35) it is 11.09, very
    # close

    # Stämmer

    # Time(n) = 1.618 ^(n - 40) * Time(n = 40)

    # Uppskattad tid för n = 50, 72 minuter
    # Uppskattad tid för n = 100, 4,1 Mår

    # 20

    # Instick - n^2
    # Merge - n log n


    # Same time for n = 1000, time = 1 s
    # For Instick we have Time(n) = Time(n = 1000) * (n)^2/(10^3)^2
    # For Merge we have Time(n) = Time(n = 1000) * (n)* log n / (1000 * log 1000)

    # Instick Time(10^6) = 11,6 dagar
    # Instick Time(10^9) = 31,7 Tusen år
    # Merge Time(10^6) = 0.55 timmar
    # Merge Time(10^6) = 34,7 dagar

    # 21
    # Two algorithms, A and B
    # A solves problem with n elements in n seconds
    # Time for B is c*n*log(n) where c is a constant
    # Test run of B finds that Time is 1 s when n = 10
    # How large does n have to be for A to be quicker than B?

    # We find c by 1 / (n * log(n)) which for 10 is 1 / (10*log(10)) = 1 / 10
    # So time for B is (1/10) * n * log(n)
    # If we equal time for B and time for A
    # n = 1/10 * n * log(n)
    # log(n) = 10
    # n = 10 ^ 10
    # So answer is n = 10 ^ 10



    

if __name__ == "__main__":
    main()
    
####################################################    
    
"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  
  
  
  
  
  Exercise 17: Time for Fibonacci:
  
  
  
  
  
  Exercise 20: Comparison sorting methods:
  
  
  
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  
  
  
  
  
  





"""
