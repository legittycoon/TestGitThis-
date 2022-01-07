Temp= eval(input( 'please enter a temperature: '))

temp= input(' is the unit of the value in celsius or Farenheit? ')

if temp== 'celsius':
     	Farenheit= 9*Temp/5+32
     	print(Farenheit)
elif temp== 'Farenheit' or temp=='farenheit':
 	    Celsius= 5*(Temp - 32) /9
 	    print(Celsius)