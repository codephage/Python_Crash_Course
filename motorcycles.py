#motorcycles=['honda','yamaha','suzuki']
#print(motorcycles)

#motorcycles.append('ducati')    
#print(motorcycles)

#motorcycles=[]
#motorcycles.append('honda')
#motorcycles.append('yamaha')
#motorcycles.append('suzuki')

#print(motorcycles)
# adding items with the method insert
#motorcycles=['honda','yamaha','suzuki']
#motorcycles.insert(0,"ducati")
#print(motorcycles)

#removing an item using the del statement

#motorcycles=['honda','yamaha','suzuki']
#print(motorcycles)

#del motorcycles[0]
#print (motorcycles)

#del motorcycles[1]
#print(motorcycles)
#---------------------------------------------------------
#Removing an item using the pop() method

#motorcycles=['honda','yamaha','suzuki']
#print(motorcycles)

#popped_motorcycle=motorcycles.pop()
#print(motorcycles)
#print(popped_motorcycle)

#motorcycles=['honda','yamaha','suzuki']
#last_owned=motorcycles.pop()
#print(f" The last motorcycle i owned was a {last_owned.title()}")
#------------------------------------------------------------------------

# Popping items from a position in a list

#motorcycles=['honda','yamaha','suzuki']
#first_owned=motorcycles.pop(0)
#print (f" The first motorcycle i owned was a {first_owned.title()}")
#------------------------------------------------------------------------
  # Removing an item by value

#motorcycles=['honda','yamaha','suzuki','ducati']
#print(motorcycles)

#motorcycles.remove("ducati")
#print(motorcycles)
#-------------------------------------------------------------------------

#You can also use the remove() method to work with a value that’s being
#removed from a list. Let’s remove the value 'ducati' and print a reason for
#removing it from the list:

motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")











