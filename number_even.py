#A four-digit integer is given. Find the number of even digits in it.
#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int=5687
a1=var_int%10
a2=var_int%100//10
a3=var_int//100%10
a4=var_int//1000
print(1-a4%2+1-a3%2+1-a2%2+1-a1%2)