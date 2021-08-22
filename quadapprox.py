from io import StringIO 
from sympy import Symbol, Derivative
from sympy.core import sympify

# defines Stringbuilder class
class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Add(self, str):
        self._file_str.write(str)

    def __str__(self):
        return self._file_str.getvalue()

# defining symbols x and y to use library
x= Symbol('x')
y= Symbol('y')

print("Welcome to Quadratic Approximation Calculator")
print(" ")
function = input("Enter your function: ")
rawpoint=input("Enter your point: ")
coordinates=rawpoint.split(",",2)
# defines x point and y point variable as the correct parts of the input 
xpoint=coordinates[0]
ypoint=coordinates[1]

# calculates the partial derivative in regards to x and evaluates that at the point
partialderivx= Derivative(function, x)
partialx=partialderivx.doit()
ptpartialx=partialx.subs([(x,xpoint),(y,ypoint)])



# calculates the partial derivative in regards to y and evaluates that at the point
partialderivy= Derivative(function, y)
partialy=partialderivy.doit()
ptpartialy=partialy.subs([(x,xpoint),(y,ypoint)])

# calculates the partial derivative in regards to xx and evaluates that at the point
partialderivxx= Derivative(partialx, x) 
partialxx=partialderivxx.doit()
ptpartialxx=partialxx.subs([(x,xpoint),(y,ypoint)])

# calculates the partial derivative in regards to xy and evaluates that at the point
partialderivxy=Derivative(partialx, y) 
partialxy=partialderivxy.doit()
ptpartialxy=partialxy.subs([(x,xpoint),(y,ypoint)])

# calculates the partial derivative in regards to yy and evaluates that at the point
partialderivyy=Derivative(partialy, y) 
partialyy=partialderivyy.doit() 
ptpartialyy=partialyy.subs([(x,xpoint),(y,ypoint)])


#evaluates the original function at the point for linear approximation part of formula
fofp=sympify(function).subs([(x,xpoint),(y,ypoint)])

# initiates stringbuilder to build equation
string_builder = StringBuilder()

# builds stringquadratic approximation equation using calculations
string_builder.Add(str(fofp)+" + ")
string_builder.Add(str(ptpartialx))
string_builder.Add("(x-"+ str(xpoint)+ ") + ")
string_builder.Add(str(ptpartialy))
string_builder.Add("(y-"+ str(ypoint)+ ") + ")
string_builder.Add(str(ptpartialxx/2))
string_builder.Add("(x-"+str(xpoint)+")^2 + ")
string_builder.Add(str(ptpartialxy))
string_builder.Add("(x-"+str(xpoint)+")(y-"+ str(ypoint)+ ") + ")
string_builder.Add(str(ptpartialyy/2))
string_builder.Add("(y-"+str(ypoint)+")^2 ")

#prints individual calculations and then whole equation
print("Function at pt: " + str(fofp))
print("Partial x: " + (str(ptpartialx)))
print("Partial y: " + (str(ptpartialy)))
print("Partial xx: " + (str(ptpartialxx)))
print("Partial xy: " + (str(ptpartialxy)))
print("Partial yy: " + (str(ptpartialyy)))
print("\nQuadratic approximation equation:  " )
print(string_builder)
