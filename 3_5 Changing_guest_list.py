#3-5. Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.

#Start with your program from Exercise 3-4. Add a print() call at the end
#of your program stating the name of the guest who can’t make it.
#Modify your list, replacing the name of the guest who can’t make it with
#the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still
#in your list.

guest_list=['Albert einstein','jaque fresco','Jordan Peterson']

print(f'\nHello {guest_list[0]} i would like to talk with you about the universe\n')
print (f'Hello {guest_list[1]} I would like to talk with you about getting through life\n')
print(f'Hello {guest_list[2]} I would like to talk with you about having a good life\n')

print(f'\n{guest_list[0]} cannot come to  the dinner\n')
guest_list[0]='Michael Jordan'

print(f'\nHello {guest_list[0]} i would like to talk with you about the sports\n')
print (f'Hello {guest_list[1]} I would like to talk with you about getting through life\n')
print(f'Hello {guest_list[2]} I would like to talk with you about having a good life\n')