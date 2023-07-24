#!/usr/bin/env python
# coding: utf-8

# Q.1- Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25
# Ans> the keyword used to create a function in Paython is "def". Here's the code to create a function that return a list of odd numbers in the range of 1 to 25:

# In[10]:


def odd_numbers():
    odd_list = []
    for i in range(1,26):
        if i % 2 !=0:
             odd_list.append(i)
    return  odd_list
odd_numbers()           


#  Q.2- Why args and kwargs is used in some functions? create a function each for keyword and args and **kwargs to 
#      demonstrate their use.
# args and kwargs are used in functions to allow them to accept a varying number of arguments. *args is used to send a 
# non-keyworded variable length argument list to the function. it allows you to pass a variable number of arguments to a function which will be received as a tuple. kwarge is used to pass keyworded variable length of arguments to a function, which will be 
# received as a dictionary. Here's an example of how you can use args and *kwargs in a function:

# In[12]:


def print_args(*args):
    print("arguments passed as *args:",args)
    
def print_kwargs(*kwargs):
    print("arguments passed as **kwargs:",kwargs)
    

 Q.3-What  is an iterator in paython? Name the method used to initialise the iterator the object and the method used for             iteration. Use these methods to print the first five elements of the given list [2,4,6,8,10,12,14,16,18,20]
 
    An iterator in paython is an object that implements the iterator protocol, which consists of two methods: iter()
    and next().the iter() method is used to initialize the iterator object, and the next() method is used for iteration.
    
# In[21]:


numbers=[2,4,6,8,10,12,14,16,18,20]

class TopNumbers:
    def __init__(self,limit):
        self.limit = limit
        self.counter=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            number= numbers[self.counter]
            self.counter += 1
            return number
        else:
            raise StopIteration
            
print("the first 5 numbers:")
for number in TopNumbers(5):
    print(number)
    


# Q.4-What is a generator function in paython? Why yeild keyword is used? Give an example of a generator function.
# 
# Ans> A Generator function in a paython is a function that returns a generator. the yeild keyword is used to return a value 
#      from a generator function and pause the function's execution. When the generator function is called again, it resumes
#      execution from where it left off, using the saved state from the last call to yeild.

# In[24]:


def fibonacci_sequence(limit):
    a,b=0,1
    while a < limit:
        yield a
        a,b=b,a+b
    
fib=fibonacci_sequence(20)

print("fibonacci sequence:")
for number in fib:
    print(number)


# Q.5- Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

# In[25]:


def prime_numbers():
    yield 2
    primes=[2]
    candidate=3
    while candidate < 1000:
        is_prime=True
        for prime in primes:
            if candidate % prime==0:
                is_prime=False
                break
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate+=2
        
primes=prime_numbers()

print("the first 20 prime numbers:")
for i in range(20):
    print(next(primes))


# Q.6- Write a paython program to print the first 10 Fibonacci numbers using a whileloop. 

# In[27]:


a,b=0,1 
count=0
while count<10:
    print(a)
    a,b=b,a+b
    count+=1

Q.7- Write a list comprehension to iterator through the given string: 'pwskills'. Expected output:['p','w','s','k','i','l','l','s'] .
# In[28]:


string="pwskills"
characters=[char for char in string]
print(characters)


# Q.8- Write a paython program to check whether a given number is pailndrome or not using a while loop.

# In[29]:


def is_pailndrime(num):
    original=num
    reverse=0
    while num >0:
        digit=num%10
        reverse=reverse*10+digit
        num=num//10
    return original==reverse

number=int(input("enter a number:"))
if is_pailndrime(number):
    print(f"{number} is a pailndrome.")
else:
    print(f"{number} is not a pailndrome.")



# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension

# In[1]:


lst = [ele  for ele in range(1,101)]
lst_odd = [ele for ele in lst if ele&1]
print(lst_odd)


# In[ ]:




