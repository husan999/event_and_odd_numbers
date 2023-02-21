#A four-digit integer is given. Find the sum of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Create a variable "sum_even" and assign it 0.

#Find the sum of the even digits in the variable "var_int".
var_int=7288
sum_even=0
a1=var_int%10
a2=var_int%100//10
a3=var_int//100%10
a4=var_int//1000
sum_even=(a1+1)%2*a1+(a2+1)%2*a2+(a3+1)%2*a3+(a4+1)%2*a4
print(sum_even)
