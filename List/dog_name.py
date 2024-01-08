dog_name=[]
while True:
  print("enter the name of dog "+ str(len(dog_name)+1) + " or enter nothing to stop")
  name=input()
  if(name==""):
    break
  dog_name=dog_name+[name]
  
print("The names of the dogs are: ")
for name in dog_name:
  print(" "+name)