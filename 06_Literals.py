#Base - N Literal
a= 0b1010 #binary literals
b= 100    #Decimal Literal
c= 0o310  # Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal 
float_1= 10.5
float_2=1.5e2
float_3=1.5e-3

#Complex Literal
s= 34+42j

print (a,b,c,d)
print(float_1,float_2,float_3)
print(s,s.imag,s.real)

#String Literals
str_1='this is python'
str_2="This is also Python"
Multiline_str=""" This is multiline str with more than one line code"""
unicode=u"\U0001f600\U0001f606\U0001F923"#smile and emoji
raw_str=r"raw \n string"

print (str_1)
print(str_2)
print(Multiline_str)
print(unicode)
print(raw_str)

#Boolean Literals

a=True +4 #1+4=5
b=False +4 #0+4=4
print(a-b)
print(a*b)

#None Literals
a= None
print(a)

#in python to use the variable we cannot declare it first without using  like " k "