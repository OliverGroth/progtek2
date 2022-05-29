"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
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
        if len(l1) == 0 and len(l2) > 0:
            return l2
        elif len(l2) == 0 and len(l1) > 0:
            return l1
        else:
            return []


def bricklek(f, t, h, n): # Compulsory
    if n == 1:
        return [f + '->' + t]
    else:
        return bricklek(f, h, t, n - 1) + [f + '->' + t] + bricklek(h, t, f, n - 1)

def main():

    # 16
    # 50 brickor, 1 sek per flytt,
    # Från Exempel 12 ser vi att resultatet är 2^n -1 vilket är i storleksordningen 
    start = time.time()
    bricklek('f','t','h',25)
    end = time.time()
    print(end - start)

    

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
