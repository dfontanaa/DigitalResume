import os
import streamlit as st
from PIL import Image

# set paths
curr_dir = os.getcwd()
css_file = os.path.join(curr_dir, 'styles', 'main.css')
template_folder = os.path.join(curr_dir, 'templates')
cv_file = os.path.join(template_folder, 'CV.pdf')
prof_pic_file = os.path.join(template_folder, 'profile_picture.png')

# set general features
name = 'Danilo Fontana'
page_title = 'Digital CV | %s'%name
page_icon = ':airplane:'
email = 'danilofontanaa@gmail.com'
socials = {
    'LinkedIn':'https://www.linkedin.com/in/danilofontanaa/',
    #'GitHub':'https://github.com/dfontanaa'
    }
description = 'Senior Flight Controls System - Flight Control Laws Engineer'
PROJECTS = {
    'Data Scientist with Python':'https://www.datacamp.com/statement-of-accomplishment/track/dd41c8473747310e5bb3ca712e4b79b5b42d68d8',
    'Data Analyst with Python': 'https://www.datacamp.com/statement-of-accomplishment/track/e3eb3ebe8f337273a16632c82a4a4977c4ab7a4d',
    'Machine Learning Scientist': 'https://www.datacamp.com/statement-of-accomplishment/course/475ca36781281799182f93f17dee2d4747b25498',
    'Scrum Foundation Professional Certificate': 'https://www.credly.com/badges/de3f208b-1516-4a80-9382-95e59589167b?source=linked_in_profile',
}



st.set_page_config(page_title=page_title, page_icon=page_icon)

# load external files
with open(css_file) as fid:
    st.markdown("<style>{}</style>".format(fid.read()), unsafe_allow_html=True)

with open(cv_file, "rb") as pdf_file:
    pdf = pdf_file.read()
profile_pic = Image.open(prof_pic_file)

# create column
c1, c2 = st.columns(2, gap='small')
with c1:
    st.image(profile_pic, width=250)

with c2:
    st.title(name)
    st.write(description)
    st.download_button(label=" 📄 Download Resume", data = pdf, file_name=os.path.basename(cv_file), mime='application/octet-stream')
    st.write("📫", email)
    for index, (platform, link) in enumerate(socials.items()):
        st.write(f"[{platform}]({link})")
    
    
# --- EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 10 Years expereince with Flight Control System Fly-By-Wire Control Laws
- ✔️ Strong hands on experience and knowledge in complex safety critical system design
- ✔️ Responsible for Safety of Flight campaigns
- ✔️ Experience in leading multicultural teams in Japan and Germany
"""
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Matlab and Python
- 📊 Standards: ARP-4754A, ARP-4761, DO-178C, DO-331
- 📚 Modeling: Monitors, State Machines, State Logics, actuator modeling
- 🗄️ V&V: HW/SW in the loop, test benches, Iron Bird, test automation
"""
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write('🚧', "**Systems Development Engineer | AES** :de:")
st.write("2021 - Present")
st.write(
    """
- ► Leading development of systems requirements including system performance, system interfaces, architecture, and algorithms
- ► Strong background and experience in application of classical control theory to aircraft or other complex dynamic systems
- ► Development of algorithms, models, and simulation for aircraft control systems

"""
)

# --- JOB 2
st.write("🚧 ", "**Flight Control Laws Engineer, MRJ90 | MITAC** :jp:")
st.write("2019 - 2021")
st.write(
    """
- ► Led the requirements validation for the MRJ90 control laws
- ► Preparation of requirement-based tests for system level verification in the Iron Bird
- ► Development of several solutions to show compliance with IPs/CRIs
"""
)

# --- JOB 3
st.write("🚧 ", "**Flight Control Laws Engineer, 190/195 E2 | Embraer** :flag-br:")
st.write("2015 - 2019")
st.write(
    """
- ► Sub-team leader of the control laws simulation, validation and verification group.
- ► Automated the test process with desktop model-based simulations, test bench execution (hardware and software in the loop), and test report generation for the system and software verification campaign.
- ► Scrum master and the responsible for the verification package.
"""
)

# --- JOB 4
st.write("🚧 ", "**Flight Control Laws Engineer, Legacy 450/500 | Embraer** :flag-br:")
st.write("2013 - 2015")
st.write(
    """
- ► Flight control laws responsible for simulation, validation, and verification
- ► I received an innovation prize for my contributions to the new SOF process, where we were capable of identifying problems in the software and hardware testing before the supplier delivered the red-label versions, resulting in a 500,000.00 USD cost reduction per year in the SOF campaigns
- ► Development of air vehicle flight control laws, flight director, navigation, guidance, and autonomous systems control algorithms
- ► Development of hydraulic actuator model using model-based design techniques
"""
)

# --- JOB 5
st.write("🚧 ", "**Systems Engineer Trainee, (PEE) | Embraer** :flag-br:")
st.write("2012 - 2013")
st.write(
    """
- ► Systems engineering training program
"""
)

# --- JOB 6
st.write("🚧 ", "**Intern | Embraer** :flag-br:")
st.write("2011 - 2012")
st.write(
    """
- ► Development of tools and devices for the Iron Bird
- ► Preparation of detailed test procedures 
- ► Support test execution and post processing 
"""
)

# --- Projects & Accomplishments ---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")