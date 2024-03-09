# Collinear point
# Given three points A(x1, y1), B(x2, y2) and C(x3, y3), we need to check if all the three points lie on the same line.

# Approach 1 : Using Slope
'''def isCollinearPoints(x1, x2, x3, y1, y2, y3):
    # If slope of AB is equal to slope of BC, then A, B, C are collinear.
    if (y2-y1) * (x3-x2) == (y3-y2) * (x2-x1):
        print("Yes")
    else:
        print("No")

# Driver Code
x1,x2,x3,y1,y2,y3 = 1,1,1,6,0,9
isCollinearPoints(x1,x2,x3,y1,y2,y3)'''

''' Time Complexity: O(1)
    Space Complexity: O(1)
'''

# Approach 2 : Using Area of Triangle

def isCollinearPoints(x1, x2, x3, y1, y2, y3):
    # If area of triangle formed by A, B, C is zero, then A, B, C are collinear.
    area = 0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if area == 0:
        print("Yes")
    else:
        print("No")
# Driver Code
x1,x2,x3,y1,y2,y3 = 1,1,1,6,0,9 
isCollinearPoints(x1,x2,x3,y1,y2,y3)

''' Time Complexity: O(1)
    Space Complexity: O(1)
'''