petname=[]

while True:
  print('Enter the name of the pet '+ str(len(petname)+1)+" or enter nothing to stop : ")
  name=input()
  if name=="":
    break
  petname=petname + [name]
print("The pet names are : ") 
for name in petname:
  print (" "+name)