while True:
 m=eval(input("enter your maths number"))
 s=eval(input("enter your science number"))
 ss=eval(input("enter your social science number"))
 e=eval(input("enter your english number"))
 h=eval(input("enter your hindi number"))
 cs=eval(input("enter your computer science number"))
 tn=(m+s+ss+e+h)
 print("total number is",tn,"out of 600")
 p=(tn*100)/600
 print("percentage",p)
 if p>=90:
    print("the grade of student is A+")
 elif p>=80:
    print("the grade of student is A")
 elif p>=70:
    print("the grade of student is B")
 elif p>=60:
    print("the grade of student is C")
 else:
    print("the grade of student is D")
