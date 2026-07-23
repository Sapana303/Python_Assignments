n = int(input("Entern n : "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end="")
#     print("") # ye next line me le jayega
'''
*
**
***
****
*****
'''


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print("") # ye next line me le jayega
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print("") # ye next line me le jayega
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print("") # ye next line me le jayega
# for i in range(n,-1,-1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print("") # ye next line me le jayega

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''


# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print("") # ye next line me le jayega
# for i in range(n,-1,-1):
#     for j in range(1,i):    # i+1 to i taki do bar 1..5 ki line na aaye ek hi bar aaye
#         print(j, end=" ")
#     print("") # ye next line me le jayega

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 
1 2 
1 
'''

# for i in range(1,n+1):
#     spaces = " "*(n-i)
#     stars = "*"*(2*i-1)
#     print(spaces + stars)

'''
    *
   ***
  *****
 *******
*********
'''

# for i in range(1,n+1):
#     spaces = " "*(n-i)
#     stars = str(i)*(2*i-1)
#     print(spaces + stars)
'''
    1
   222
  33333
 4444444
555555555
'''

#    " ".join()  numbers ke bich space dene ke liye
# for i in range(1,n+1):
#     spaces = " "*(n-i)
#     stars = " ".join([str(i)]*(2*i-1))
#     print(spaces + stars)
'''
    1
   2 2 2
  3 3 3 3 3
 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
'''


# # Upper
# for i in range(1, n+1):
#     print(" "*(n-i), end="")

#     # Increasing numbers
#     for j in range(1, i+1):
#         print(j, end="")

#     # Decreasing numbers
#     for j in range(i-1, 0, -1):
#         print(j, end="")

#     print()

# # Lower
# for i in range(n-1, 0, -1):
#     print(" "*(n-i), end="")

#     for j in range(1, i+1):
#         print(j, end="")

#     for j in range(i-1, 0, -1):
#         print(j, end="")

#     print()

'''
  1
 121
12321
 121
  1
'''

# # Upper
# for i in range(1, n+1):
#     print(" "*(n-i), end="")

#     # Increasing numbers
#     for j in range(1, i+1):
#         print("*", end="")

#     # Decreasing numbers
#     for j in range(i-1, 0, -1):
#         print("*", end="")

#     print()

# # Lower
# for i in range(n-1, 0, -1):
#     print(" "*(n-i), end="")

#     for j in range(1, i+1):
#         print("*", end="")

#     for j in range(i-1, 0, -1):
#         print("*", end="")

#     print()

'''
  *
 ***
*****
 ***
  *
'''

# for i in range(1, n+1):
#     print(" "*(n-i), end="")

#     # Increasing numbers
#     for j in range(1, i+1):
#         print(j, end="")

#     # Decreasing numbers
#     for j in range(i-1, 0, -1):
#         print(j, end="")
    
#     print()

# l = [4,6,7,8,9]
# n = max(l)
# print(n)
# m = min(l)
# print(m)

# for i in range(1,n+1):
#     spaces = " "*(n-i+1)
#     stars = "*"*i
#     print(spaces + stars)
#     print("")

'''
    *

   **

  ***

 ****
'''


# for i in range(1,n+1):
#     spaces = " "*(n-i+1)
#     stars = "*"*i
#     print(spaces + stars)
# '''
#     *
#    **
#   ***
#  ****
# '''
# for i in range(1,n+1):
#     spaces = " "*(n-i+1)
#     stars = str(i)*i
#     print(spaces + stars)

#   '''
#      1
#     22
#    333
#   4444
#  55555
#   '''

# sep 
# a,b,c = 10,20,20
# print(a,b,c, sep='-')

# for i in range(0,n):
#     space = " "*i
#     stars = "*"*n
#     print(space+stars)
'''
****
 ****
  ****
   ****
'''  

# for i in range(n):
#     space = " "*i
#     stars = "*"*n
#     print(space+stars)
# for i in range(n-2,-1,-1):
#     space = " "*i
#     stars = "*"*n
#     print(space+stars)
'''
*****
 *****
  *****
   *****
    *****
   *****
  *****
 *****
*****
'''
#upper half
# for i in range(n):
#     left = " "*i
#     middle = " "*(2*(n-i-1))
#     print(left + "*"*n+middle+"*"*n)
# for i in range(n-2,-1,-1):
#     left = " "*i
#     middle = " "*(2*(n-i-1))
#     print(left+"*"*n+middle+"*"*n)



# for i in range(1,n+1):
#     space = " "*(n-i)
#     stars = "*"*n
#     print(space+stars)

'''
   ****
  ****
 ****
****
'''


# for i in range(0,n):
#     space = " "*i
#     stars = "*"*n
#     print(space+stars)
# for i in range(1,n+1):
#     space = " "*(2*n-i)
#     stars = "*"*n
#     print(space+stars)
'''
*****        *****
 *****      *****
  *****    *****
   *****  *****
    **********
   *****  *****
  *****    *****
 *****      *****
*****        *****
'''

# a = '1'
# b = "2"
# c = '"re"'
# d= "'re'"
# c = '''hi'''

# print(type(c))

# for i in range(n):
#   for j in range(n):
#     print("*",end=" ")
#   print()  

'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

# for i in range(n):
#     for j in range(n):
#       if i==0 or i==n-1 or j == 0 or j==n-1:
#         print("*",end=" ")
#       else:
#          print(" ",end=" ")
#     print()

'''
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''   
      
# Hollow butterfly
for i in range(1, n+1):
    for j in range(1, i+1):
        if j==1 or j==i:
            print('*',end="")
        else:
            print(" ",end='')

    for j in range(2*(n-i)):
        print(" ",end='')

    for j in range(1, i+1):
        if j==1 or j==i:
            print('*',end='')
        else:
            print(' ', end='')

    print()

for i in range(n,0,-1):
    for j in range(1, i+1):
        if j==1 or j==i:
            print('*',end='')
        else:
            print(' ',end='')

    for j in range(2*(n-i)):
        print(' ', end='')

    for j in range(1,i+1):
        if j==1 or j==i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
'''
*        *
**      **
* *    * *
*  *  *  *
*   **   *
*   **   *
*  *  *  *
* *    * *
**      **
*        *
'''

#

import turtle # turtle is a built-in graphics library used to create drawings, shapes, and simple animations on a virtual canvas. acts like a physical pen, drawing lines as it moves according to your code
import colorsys # Color System , It helps to convert between different ways of representing colors.

screen = turtle.Screen() # .Screen() - will create drawing window
screen.bgcolor('black')

pen = turtle.Turtle() # This creates the drawing pen, It remembers position, direction, pen color
pen.speed(10) # fastest possible speed
pen.width(2) # sets the line thichness
# pen.hideturtle() # hide icon only drawing appear
screen.tracer(0) # normaly turtle work like (move,draw,refresh->repeat) but we want like (move,move.. draw everything and then refresh)
angle = 0

while True: # Infinite loop
    pen.clear()
    hue=0

    for i in range(180):
        r,g,b = colorsys.hsv_to_rgb(hue,1,1)

        pen.pencolor(r,g,b)

        pen.circle(120)

        hue += 1/180

    angle += 0.5

    screen.update()
     