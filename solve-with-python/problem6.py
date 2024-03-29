"""
problem 6 :

m = (1 + 2 + 3 + ... + 99 + 100)^2
n = 1^2 + 2^2 + 3^2 + ... + 99^2 + 100^2
answer = m - n 
"""

# ----------- m ----------- #
a = 0
for x in range(1,101):
    a += x
m = a ** 2

# ----------- n ----------- #
n = 0
for x in range(1,101):
    b = x ** 2
    n += b

# -------- answer -------- #
answer = m - n

print(f'(1 + 2 + 3 + ... + 99 + 100)^2 = {m}')
print(f'1^2 + 2^2 + 3^2 + ... + 99^2 + 100^2 = {n}')
print(f'answer = {answer} = {m} - {n}')
