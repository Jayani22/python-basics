# python is case-sensitive i.e., 'a' and 'A' are different
ennvironment = input("Enter your environment: ")
change_ticket = False

ennvironment = ennvironment.casefold()
if ennvironment == "prod":
    change_ticket = True
    print("Please provide a change ticket")
elif ennvironment == "staging":
    print("Welcome to staging environment")
else:
    print("Please login using your credentials")
 