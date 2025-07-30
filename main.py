from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
import re

# Trying to get user input

def get_user_info_input(prompt):
    return input(prompt).strip()

# Trying to differentiate the different sections of user input

def data_collection():
    print("\n--- Why not share your data with the Ogre? ---")
    print("Let's start! Just follow the instructions and provide the info")

    data = {}

    # 1st section: Collecting contact information
    print("\n ---Contact Information---")
    data['Name'] = get_user_info_input("Enter your Full name, eg. Hasan Fuad: ")
    data['Email'] = get_user_info_input("Enter your Email address: ")
    data['Phone Number'] = get_user_info_input("Enter your phone number, with country code (optional): ") 
    data['Address'] = get_user_info_input("Enter your current address (optional): ") 
    data['github'] = get_user_info_input("GitHub Profile URL (optional): ")

    # 2nd section: User's own short story
    print("\n--- Your Story in short---")
    print("Write a short intro, then a short description about yourself. (Type 'FINISH' on a new line when done)")
    story_lines = []
    while True:
        line = input()
        if line.upper() == "FINISH":
            break
        story_lines.append(line)
    data['Story'] = "\n".join(story_lines)

    # 3rd section: Collection Educational information
    print("\n-- Educational Information --")
    print("Enter your educational information according to the prompts.")

    edu_entries = [] # An empty list to store education entries
    degree = get_user_info_input("Enter your degree (eg. BSc in CS):")
    university = get_user_info_input("Enter your university name: ")
    year = get_user_info_input("Enter the year of graduation (OPTIONAL): ")
    gpa = get_user_info_input("Enter your GPA (optional): ")
    edu_entries.append({ 
        'Degree': degree,
        'University': university,
        'Year': year,
        'GPA': gpa
        })
    data['Education'] = edu_entries

    #4th section: Collecting user work experience
    print("\n-- Work Experience --")
    print("Enter your work experience according to the prompts. Type 'FINISH' for Job Title to end.")
    work_entries = []
    while True:
        title = get_user_info_input("Enter your job title (eg. Software Engineer) (or 'FINISH' to end): ")
        if title.upper() == "FINISH":
            break 

        company = get_user_info_input("Enter the company name: ")
        duration = get_user_info_input("Enter the duration of your employment (eg. 2 years): ")
        print("Enter a brief description of your role (Type 'FINISH' on a new line when done):")
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
    print("\n-- Skills --") 
    data['Skills'] = get_user_info_input("Enter your skills, separated by commas (Eg. Python, Java, C++): ")

    print("\nData collection is complete, thank you!") 
    return data

# After user input, now I try to to create the file itself

def generate_resume(data, output_filepath="interactive_resume.pdf"):
    doc = SimpleDocTemplate(output_filepath, pagesize=letter)
    styles = getSampleStyleSheet()

    # Making Custom styles
    name_style = ParagraphStyle(
        'Name',
        parent=styles['h1'],
        fontSize=25,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=0.5 * inch,
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
        parent=styles['h2'],
        fontSize=14,
        leading=16,
        spaceBefore=0.2 * inch,
        spaceAfter=0.08 * inch,
        fontName='Helvetica-Bold',
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
        bulletIndent=0,
        bulletText='•',
        fontSize=10,
        leading=12,
        spaceAfter=0.03 * inch
    )

    # Now this part tries to put it all together and tries to create the PDF file

    elements = []

    # Name section
    if data.get('Name'):
        elements.append(Paragraph(data['Name'], name_style))
        elements.append(Spacer(1, 0.2 * inch))

    # Contact info section
    contact_info = []
    if data.get('Email'):
        contact_info.append(data['Email'])
    if data.get('Phone Number'):
        contact_info.append(data['Phone Number'])
    if data.get('Address'):
        contact_info.append(data['Address'])
    if data.get('github'):
        contact_info.append(data['github'])
    if contact_info:
        elements.append(Paragraph(" | ".join(contact_info), contact_style))
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Paragraph("_" * 65, styles['Normal']))
        elements.append(Spacer(1, 0.2 * inch))
    # Short story section
    if data.get('Story'):
        elements.append(Paragraph("Your Story:", section_title_style))
        for line in data['Story'].split('\n'):
            if line.strip():
                elements.append(Paragraph(line.strip(), normal_text_style))
        elements.append(Spacer(1, 0.2 * inch))
    # Educational section
    if data.get('Education'):
        elements.append(Paragraph("Education:", section_title_style))
        for edu in data['Education']:
            if edu.get('Degree'):
                elements.append(Paragraph(f"{edu['Degree']}", bold_text_style))
            if edu.get('University'):
                elements.append(Paragraph(f"{edu['University']}", normal_text_style))
            if edu.get('Year'):
                elements.append(Paragraph(f"Year: {edu['Year']}", normal_text_style))
            if edu.get('GPA'):
                elements.append(Paragraph(f"GPA: {edu['GPA']}", normal_text_style))
            elements.append(Spacer(1, 0.1 * inch))
    # Work experience section
    if data.get('Work Experience'):
        elements.append(Paragraph("Work Experience:", section_title_style))
        for work in data['Work Experience']:
            if work.get('Title'):
                elements.append(Paragraph(f"{work['Title']}", bold_text_style))
            if work.get('Company'):
                elements.append(Paragraph(f"{work['Company']}", normal_text_style))
            if work.get('Duration'):
                elements.append(Paragraph(f"Duration: {work['Duration']}", normal_text_style))
            description = work.get('Description', '')
            for des in description.split('\n'):
                if des.strip(): 
                    elements.append(Paragraph(des.strip(), bullet_style))
            elements.append(Spacer(1, 0.1 * inch))
    # Skills section
    if data.get('Skills'): 
        elements.append(Paragraph("Your Skills:", section_title_style))
        
        skills_list = [s.strip() for s in data['Skills'].split(',') if s.strip()]
        for skill in skills_list:
            elements.append(Paragraph(skill, bullet_style)) 
        elements.append(Spacer(1, 0.2 * inch))
    try:
        doc.build(elements)
        print(f"\nPDF resume successfully created at {output_filepath}")
    except Exception as e:
        print(f"An error occurred when making the pdf: {e}") 

# Main function to run the script
if __name__ == "__main__":
    resume_data = data_collection()
    generate_resume(resume_data, "my_interactive_resume.pdf")
