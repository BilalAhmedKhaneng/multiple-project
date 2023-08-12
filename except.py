#we use for error if we have string and inejer adding
try:
   a=int(input("enter the numebr"))
   print(a+3)
except Exception as e:
   print("spme error ocuured",e)