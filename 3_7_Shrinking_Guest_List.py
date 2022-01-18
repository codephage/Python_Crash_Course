#3-7. Shrinking Guest List: You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.

#Start with your program from Exercise 3-6. Add a new line that prints a
#message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two
#names remain in your list. Each time you pop a name from your list, print
#a message to that person letting them know you’re sorry you can’t invite
#them to dinner.
#Print a message to each of the two people still on your list, letting them
#know they’re still invited.
#Use del to remove the last two names from your list, so you have an empty
#list. Print your list to make sure you actually have an empty list at the end
#of your program.

guest_list=['Albert einstein','jaque fresco','Jordan Peterson']



guest_list.insert(0,'President Einsenhower')
guest_list.insert(1,'Winston Churchill')
guest_list.append('Ava Lovelace')
print(guest_list)
print(f'\nHello {guest_list[0]} i would like to talk with you about politics\n')
print (f'Hello {guest_list[1]} I would like to talk with you about governance\n')
print(f'Hello {guest_list[2]} I would like to talk with you about the universe\n')
print(f'Hello {guest_list[3]} I would like to talk with you about having a good life\n')
print(f'Hello {guest_list[4]} I would like to talk with you about being a better man\n')
print(f'Hello {guest_list[5]} I would like to talk with you about computer science\n')

print('Due to problems in the table we can invite only two guests')

popped_invited_removed= guest_list.pop()
print(f'\nWe are very sorry to uninvite you {popped_invited_removed}')
popped_invited_removed= guest_list.pop()
print(f'\nWe are very sorry to uninvite you {popped_invited_removed}')
popped_invited_removed= guest_list.pop()
print(f'\nWe are very sorry to uninvite you {popped_invited_removed}')
popped_invited_removed= guest_list.pop()
print(f'\nWe are very sorry to uninvite you {popped_invited_removed}')

print(f'\nHello president {guest_list[0]}, you are still invited')
print(f'\nHello president {guest_list[1]},you are still invited')

del guest_list[0]
print (guest_list)
del guest_list[0]
print (guest_list)






