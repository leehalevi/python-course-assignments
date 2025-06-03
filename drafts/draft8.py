"""
Hi! I'm Lee!
My research is on a citation integrity tool, that will allow researchers and policy-makers
to view scientific papers in a more critical and verified manner!

I'm volunteering at Nucleate, a bio-centered accelerator for start-ups,
I'm a die-hard swiftie and I play the harp ;)
"""

def send_mail(From, To, Subject, Content, **header):
    print("To: ", To)
    print("From: ", From)

send_mail(To = "Lee",
          From = "You",
          Subject = "Me",
          Content = "Us")

# pylint -E duplication_add.py - what does it do?

def f(n):
    if int(n) != n or n<0:
        raise ValueError("Bad Parameter")

    if n == 0:
        return 1
    return n * f(n-1)

#print(f(0))

cache = {}
def fib(n):
    if int(n) != n or n <=0:
        raise ValueError("Bad parameter")

    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

#print(3, fib(3))

def fibs(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    for _ in range(2,n):
        fibs.append(fibs[:-1] + fibs[-2:])
    return

def recursion(n):
    print(f"In recursion {n}")
    recursion(n+1)

recursion(1)