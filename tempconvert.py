# Converting from fahrenheit to celsius

FH = float(input("Enter degrees in fahrenheit:"))
CL = (FH-32.0) * (5.0/9.0)
print ("\n" + str(FH) + " degrees in fahrenheit is equal to " + str(CL) + " degress in celsius.") 
 
# Converting from celsius to fahrenheit

CL2 = float(input("\n" "Enter degrees in celsius:"))
FH2 = CL2 * (9.0/5.0) + 32
print ("\n" +  str(CL2) + " degrees in celsius is equal to " + str(FH2) + " degrees in fahrenheit.")

# Coverting from fahrenheight to celcius using def

#def FtoC (F):

#	C = (F-32.0)*(5.0/9.0)
#	return C 

#for i in range (32, 213):
#	print i , FtoC (i)
