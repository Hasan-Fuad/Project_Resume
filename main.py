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
    
    # 2nd section: User's own short story 
    print("\n--- Your Story in short---")
    print("Write a short intro, then a short description about yourself.(Type FINISH when you want to finish)")
    story_lines = []
    while True:
        line = input()
        if line.upper() == "FINISH":
            break
        story_lines.append(line)
    data['Story'] = "\n".join(story_lines)
    
    # 3rd section: Collection Educational information
    print("\n-- Educational Information --")
    print("\n enter your educational information according to the prompts, type FINISH to end")
    
    edu_entries = []
    while True:
        degree = get_user_info_input("Enter your degree (eg. BSc in CE): ")
        if degree.upper() == "FINISH":
            break
    university = get_user_info_input("Enter your university name: ")
    year = get_user_info_input("Enter the year of graduation (OPTIONAL): ")
    gpa = get_user_info_input("Enter your GPA: ")
    edu_entries.appened({
        'Degree': degree,
        'University': university,
        'Year': year,
        'GPA': gpa
    })
    data['Education'] = edu_entries        
        