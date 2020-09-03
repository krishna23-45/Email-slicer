
def email_slicer():
    email = input("enter you email address \n>>")
    username = email[:email.index("@")]
    domain_name = email[email.index("@") + 1:]
    print(f"your username is {username} and your domain name is {domain_name}.")
email_slicer()