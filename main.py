#Trying to get user input 

def get_user_info_input(prompt):
    return input(prompt).strip()

#Trying to differenctiate the different sections of user input

def data_collection():
    print("\n--- Why not share your data with the Ogre? ---")
    print("Lets start! Just folllow the instructions and provide the info")
    
    data = {}
    
    # 1st section: Collecting contact information
    print("\n ---Contact Information---")
    data['Name'] = get_user_info_input("Enter your Full name, eg. Hasan Fuad: ")
    data['Email'] = get_user_info_input("Enter your Email address: ")
    data['Phone Number'] = get_user_info_input("Enter your phone number, with country code: ")
    data['Address'] = get_user_info_input("Enter your current address: ")
    