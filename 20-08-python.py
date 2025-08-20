# python progra to check if 3 lengths for a triangle

def greatest_of_3numbers(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
    

s1,s2,s3=5,4,3

if ( s1+s2 > s3 ) and ( s2 + s3 > s1 ) and ( s1 + s3 > s2 ):
    print("traingle can be formed")
else:
    print("traingle cannot be formed")

if ( s1 == s2 ) and ( s2 == s3 ) and ( s1 == s3):
    print("Equilateral triangle")
elif ( s1 == s2 ) or ( s2 == s3 ) or ( s1 == s3 ):
    print("isoscles triangle")
else:
    print("scalence tiangle")


# to check if it is a right angled traingle

hypo = greatest_of_3numbers(num1=s1,num2=s2,num3=s3)

if hypo**2 == s1**2 + s2**2 or hypo**2 == s1**2 + s3**2 or hypo**2 == s3**2 + s2**2:
    print("right angled triangle")
else:
    print("not a righ angled traingle")

