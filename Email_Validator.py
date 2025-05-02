# 3. Email Validator Program

class EmailFormatError(Exception):
    def __init__(self, email_id, msg):
        self.email_id = email_id
        self.msg = msg
        super().__init__(self.msg)

    def __str__(self):
        return self.msg

def Email_Validator(limit):
    email_adresses =[]
    try:
        for _ in range(limit):
            email_id = input("Enter email address:")
            if '@' not in email_id or '.' not in email_id:
                raise EmailFormatError(email_id, "Must contain '@' and '.' in your email")
            if email_id.startswith("@"):
                raise EmailFormatError(email_id, "Must have atleast one character before '@'")
            email_adresses.append(email_id)
        email_adresses.sort()
    except EmailFormatError as e:
        print(f"An error occured: {e}.")
    
    return email_adresses


lim = int(input("How many email adresses you want to enter?:"))
print(f"The list of {lim} email addresses: {Email_Validator(lim)}")