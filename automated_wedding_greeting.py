guest_names = []
number_of_guests = 0


# repeated loop for people signing in
while True:                                                         # forever repeated loop till stop command
    print("Please add your first, and last name to the registry!")
    person = input('Name: ')                                        # person inputs their name
    print("Thank you for coming, " + person + '!')                  # thank you response is given
    if person == "exit":                                            # if name typed is "exit" (stop command)
        break                                                       # stops the loop
    guest_names.append(person)                                      # names that were entered input into a list
    number_of_guests += 1                                           # adds count guest counter w/ each name entered

print(guest_names)
print(number_of_guests)
