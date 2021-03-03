# bounce.py
#
# Exercise 1.5
height = 100
fraction = 3.0/5
bounce = 1
while bounce != 11:
    height = fraction*height
    print(bounce, round(height,4))
    bounce +=1

