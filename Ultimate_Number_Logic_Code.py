                                #ULTIMATE NUMBER LOGIC CODE

#Function to check whether the number is odd or even.
#Note-: An odd number is not divisible by 2. An even number is divisible by 2.
def is_odd_even(num):
    if num % 2 == 0:
        return(f"{num} is even")
    else:
        return(f"{num} is odd")

#Function to check whether the number is prime or composite.
#Note-: Prime number is a whole number greater than 1 that cannot be exactly 
#divided by any whole number other than itself and 1.
#Composite numbers are whole numbers that have more than two factors.
def is_prime_composite(num):
    if num == 0 or num == 1:
        return(f"{num} is neither prime nor composite")
    elif num == 2:
        return(f"{num} is prime")
    else:
        for i in range(2, num):
            if num % i == 0:
                return(f"{num} is composite")
                break
            else:
                return(f"{num} is prime")

#Function to check whether the number is abundant or not.
#Note-: An abundant number or excessive number is a positive integer for which 
#the sum of its proper divisors is greater than the number.
def is_abundant(num):
    sum = 0
    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            sum += i
        
    if sum > num:
        return(f"{num} is abundant")
    else:
        return(f"{num} is not abundant")

#Function to check whether the number is automorphic or not.
#Note-: An automorphic number is an integer whose square ends with the given integer.
def is_automorphic(num):
    temp = num
    digits = 0
    a = 1
    sq = num * num
    while temp > 0:
        temp = temp//10
        digits += 1
    
    for i in range(1, digits + 1):
        a = a * 10
    
    if sq % a == num:
        return(f"{num} is automorphic")
    else:
        return(f"{num} is not automorphic")

#Function to check whether the number is disarium or not.
#Note-: A number is said to be the Disarium number when the sum of its digit 
#raised to the power of their respective positions is equal to the number itself.
def is_disarium(num):
    num_len = len(str(num))
    temp = num
    sum = 0
    rem = 0
    while temp > 0:
        rem = temp % 10
        sum += int(rem ** num_len)
        temp = temp//10
        num_len -= 1
    
    if sum == num:
        return(f"{num} is disarium")
    else:
        return(f"{num} is not disarium")

#Function to check whether the number is neon or not.
#Note-: A positive integer whose sum of digits of its square is equal to the number itself.
def is_neon(num):
    sq = num * num
    sum = 0
    while sq > 0:
        sum += sq % 10
        sq = sq//10
    
    if sum == num:
        return(f"{num} is neon")
    else:
        return(f"{num} is not neon")

#Function to check whether the number is palindrome or not.
#Note-: A palindrome number is a number that remains the same when digits are reversed.
def is_palindrome(num):
    temp = num
    reverse = 0
    while temp > 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp//10
    
    if reverse == num:
        return(f"{num} is palindrome")
    else:
        return(f"{num} is not palindrome")

#Function to check whether the number is perfect square or not.
#Note-: Perfect square is an integer that is the square of an integer.
def is_perfect_square(num):
    for i in range(1, int(num/2) + 1):
        if i * i == num:
            return(f"{num} is a perfect square")
            flag = 1
            break
        else:
            flag = 0
    
    if flag == 0:
        return(f"{num} is not a perfect square")

#Function to check whether the number is pronic or not.
#Note-: A pronic number is a number which is the product of two consecutive integers.
#It is in the form of n*(n+1).
def is_pronic(num):
    for i in range(1, num + 1):
        if i * (i + 1) == num:
            return(f"{num} is pronic")
            flag = 1
            break
        else:
            flag = 0
    
    if flag == 0:
        return(f"{num} is not pronic")

#Main Function Code
num = int(input("Enter the number: "))
check_odd_even = is_odd_even(num)
check_prime_composite = is_prime_composite(num)
check_abundant = is_abundant(num)
check_automorphic = is_automorphic(num)
check_disarium = is_disarium(num)
check_neon = is_neon(num)
check_palindrome = is_palindrome(num)
check_perfect_square = is_perfect_square(num)
check_pronic = is_pronic(num)
print(check_odd_even)
print(check_prime_composite)
print(check_abundant)
print(check_automorphic)
print(check_disarium)
print(check_neon)
print(check_palindrome)
print(check_perfect_square)
print(check_pronic)