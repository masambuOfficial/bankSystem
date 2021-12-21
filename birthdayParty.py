# Write a python script that enables someone register for a birthday  party. we need name, gift, gender, phone number, date of birth. and all information should be stored and the guests should be able to have a printout on this. And all guests should be able to be  printed out. Use functions, loops and dictionaries. This assignment should be ready by Tuesday 21st December 2021.




print("\t\tWelcome to the Bithday Party\t\t")
print("\tTo register please enter the following details\t")

def birthdayParty():
    name = input("Enter your name: ")
    gift = input("Enter the type of gift you are bring with you: ")
    gender = input("Please enter your prefered gender: ")    
    phone_number = input("What is your number: ")
    birthdate = input("Enter your Date of Birth: ")
    print("\n Thank you for registering for our Birthday your information will be store confidently to properly serve!")
    print("Name: " + name+ '\n', "Gift: " + gift + '\n' ,  "Gender: " + gender + '\n' , "Phone: " + phone_number +'\n', "Birthday: " + birthdate)
birthdayParty()

registerdetails = {

}
for i in birthdayParty():

