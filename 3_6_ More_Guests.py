#3-6. More Guests: You just found a bigger dinner table, so now more space is
#available. Think of three more guests to invite to dinner.

#Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
#call to the end of your program informing people that you found a bigger
#dinner table.
#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list.

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



