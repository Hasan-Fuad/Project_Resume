from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER

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
    data['github'] = get_user_info_input("GitHub Profile URL (optional): ")
    
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
    
    #4th section: Collecting user work experience
    print("\n-- Work Experience --")
    print("Enter your work experience according to the prompts, type FINISH to end")
    work_entries = []
    while True:
        tile = get_user_info_input("Enter your job title (eg. Software Engineer): ")
        if title.upper() == "FINISH":
            break
        company = get_user_info_input("Enter the company name: ")
        duration = get_user_info_input("Enter the duration of your employment (eg. 2 years): ")
        description = get_user_info_input("Enter a brief description of your role: ")
        print("Enter a description of your role, type FINISH to end")
        desc_lines = []
        while True:
            line = input()
            if line.upper() == "FINISH":
                break
            desc_lines.append(line)
        work_entries.append({
            'Title': title,
            'Company': company,
            'Duration': duration,
            'Description': "\n".join(desc_lines)
        })
    data['Work Experience'] = work_entries
    
    #5th section: Collecting user skills
    priint("/n-- Skills --")
    print("Enter you skills, seperated by commas(Eg. Python, Java, C++)")
    print("\n data collection is complete, thank you!")
    
    #After user input, now I try to to create the file itself
    
    def generate_resume(data, output_filepath = "interactive_resume.pdf"):
        
        doc = SimpleDocTemplate(output_filepath, pagesize = letter)
        styles = getSampleStyleSheet()
        
        #Making Custom styles
        name_style = ParagraphStyle(
            'Name',
            parent=styles['h1'],
            fontSize= 25,
            leading= 30,
            alignment= TA_CENTER,
            spaceAfter= 0.5 * inch,
        )
        contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontSize=10,
        leading=12,
        alignment=TA_CENTER,
        spaceAfter=0.15 * inch,
        )
        section_title_style = ParagraphStyle(
            'SectionTitle',
            parent = styles['h2'],
            fontSize = 14,
            leading= 16,
            spaceBefore= 0.2 * inch,
            spaceAfter= 0.1 * inch,
            fontName= 'Helvetica-Bold',
        )
        bold_text_style = ParagraphStyle(
        'BoldText',
        parent=styles['Normal'],
        fontSize=11,
        leading=13,
        fontName='Helvetica-Bold',
        spaceAfter=0.03 * inch
        )
        normal_text_style = ParagraphStyle(
            'NormalText',
            parent=styles['Normal'],
            fontSize=10,
            leading=12,
            spaceAfter=0.05 * inch,
        )
        bullet_style = ParagraphStyle(
            'Bullet',
            parent=normal_text_style,
            leftIndent=0.25 * inch,
            firstLineIndent=-0.15 * inch, 
            bulletIndent=0.0 * inch,
            bulletText='•',
            fontSize=10,
            leading=12,
            spaceAfter=0.03 * inch
        )
        
        
        
                      