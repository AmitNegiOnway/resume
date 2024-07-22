import streamlit as st
def load_home_page():

    col1, col2 = st.columns(2)

    with col1:
        st.title("Amit Negi")
        st.write("Aspiring Data Scientist")
        st.subheader("About Me")
        st.write("""
        I recently completed a data science course and am passionate about leveraging data to drive impactful insights and solutions.
        """)
        # Download Resume button
        with open("resume1 (2).pdf", "rb") as file:
            resume_data = file.read()

        # Provide the download button
        st.download_button(
            label="Download Resume",
            data=resume_data,
            file_name="resume.pdf",
            mime="application/pdf"
        )


    with col2:
        st.image('amit negi photo.jpg')

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("[Git Hub](https://github.com/AmitNegiOnway)")


    # Experience
    st.subheader("Recent Experience")
    st.write("""
                <div style="margin-left: 20px;">
                    <span style="color: green;">💠</span>
                    BSc Graduate in Maths, Statistics, and Computer Science 
                </div><br>
                """, unsafe_allow_html=True)
    st.write("""
                                <div style="margin-left: 80px;">
                                    <span style="color: green;">🔸</span>
                                    <span style="color: SpringGreen;">Data Analysis:  </span> 
                                      Proficient in analyzing data to extract meaningful insights and inform decision-making processes.
                                </div><br>
                                """, unsafe_allow_html=True)

    st.write("""
                                    <div style="margin-left: 80px;">
                                        <span style="color: green;">🔸</span>
                                        <span style="color: SpringGreen;">Statistics Concepts:  </span> 
                                          Strong understanding of statistical theories and methods, including hypothesis testing, regression analysis, and probability
                                    </div><br>
                                    """, unsafe_allow_html=True)

    st.write("""
                                        <div style="margin-left: 80px;">
                                            <span style="color: green;">🔸</span>
                                            <span style="color: SpringGreen;"> Project Development:  </span> 
                                              Completed several course projects involving the application of mathematical, statistical, and computational techniques to solve real-world problems.


                                        </div><br>
                                        """, unsafe_allow_html=True)

    st.write("""
                                        <div style="margin-left: 80px;">
                                            <span style="color: green;">🔸</span>
                                            <span style="color: SpringGreen;"> Programming Skills:  </span> 
                                              Experienced in using Python for data manipulation, analysis, and visualization. Familiar with tools like MySQL , Power BI and Tableau.
                                        </div><br>
                                        """, unsafe_allow_html=True)

    st.write("""
                                            <div style="margin-left: 80px;">
                                                <span style="color: green;">🔸</span>
                                                <span style="color: SpringGreen;">  Knowledge Sharing:  </span> 
                                                  Actively participated in study groups and presentations to share knowledge on the latest developments in data science and ML with peers.
                                            </div><br>
                                            """, unsafe_allow_html=True)


    st.header("Contact")
    st.write("amitnegionway@gmail.com")





def load_pp_page():
    st.title('personal project')

    st.write("""
            <div style="font-size: xx-large;">
            Data Analysis Project: Leveraging Data Scraping and Visualization for Insights in the Hospitality Industry 
            </div><hr><br><br>
            """, unsafe_allow_html=True)



    st.markdown("https://hotel-jobs-analysis.streamlit.app/")
    st.write("""
        <div>
            <span style="color: green;">🔸</span>
            <span style="color: OrangeRed;"> Keywords:</span> 
            Data scraping, web automation, data cleaning, data visualization, hospitality industry
        </div><br>
        """, unsafe_allow_html=True)

    st.subheader('Project Overview:')
    st.write('Our project embarks on the journey of digital transformation by leveraging advanced data scraping and analysis techniques to derive meaningful insights from the Hosco website. Hosco, a prominent platform in the hospitality industry, provides a wealth of information that can be harnessed to understand trends, patterns, and opportunities within the sector.')
    st.subheader('Project Components:')

    st.write("""
        <div style="margin-left: 20px;">
            <span style="color: green;">💠</span>
            <span style="color: OrangeRed;">Part 1: </span> 
            Data Acquisition and Parsing
        </div><br>
        """, unsafe_allow_html=True)

    st.write("""
            <div style="margin-left: 80px;">
                <span style="color: green;">🔸</span>
                <span style="color: SpringGreen;">Web Scraping with Selenium: </span> 
                 Utilize Selenium to automate the process of extracting data from the Hosco website. Selenium's robust automation capabilities enable efficient navigation of the website, ensuring comprehensive data collection.
            </div><br>
            """, unsafe_allow_html=True)



    st.write("""
                <div style="margin-left: 80px;">
                    <span style="color: green;">🔸</span>
                    <span style="color: SpringGreen;">Data Parsing with Beautiful Soup: </span> 
                      Employ Beautiful Soup to parse the HTML content, extracting relevant data encapsulated within the web pages.
                </div><br>
                """, unsafe_allow_html=True)

    st.write("""
            <div style="margin-left: 20px;">
                <span style="color: green;">💠</span>
                <span style="color: OrangeRed;">Part 2: </span> 
                Data Cleaning and Preparation
            </div><br>
            """, unsafe_allow_html=True)

    st.write("""
                    <div style="margin-left: 80px;">
                        <span style="color: green;">🔸</span>
                        <span style="color: SpringGreen;">Data Cleaning: </span> 
                          Conduct meticulous processing to remove inconsistencies, handle missing values, and standardize the dataset. This step ensures the dataset's readiness for analysis.
                    </div><br>
                    """, unsafe_allow_html=True)

    st.write("""
                        <div style="margin-left: 80px;">
                            <span style="color: green;">🔸</span>
                            <span style="color: SpringGreen;">Data Preparation with Pandas: </span> 
                              Leverage the powerful functionalities of the Pandas library to conduct a thorough examination and manipulation of the data, preparing it for subsequent analytical procedures.
                        </div><br>
                        """, unsafe_allow_html=True)

    st.write("""
            <div style="margin-left: 20px;">
                <span style="color: green;">💠</span>
                <span style="color: OrangeRed;">Part 3: </span> 
                Data Analysis and Visualization
            </div><br>
            """, unsafe_allow_html=True)
    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Visualization with Plotly and Seaborn: </span> 
                                  Utilize Plotly's interactive visualizations and Seaborn's statistical plotting capabilities to facilitate an in-depth exploration of the dataset. Identify trends, outliers, and significant patterns through these visualizations.
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                <div style="margin-left: 20px;">
                    <span style="color: green;">💠</span>
                    <span style="color: OrangeRed;">Part 4: </span> 
                    Presentation and Interaction
                </div><br>
                """, unsafe_allow_html=True)

    st.write("""<div style="margin-left: 80px;">
                    <span style="color: green;">🔸</span>
                    <span style="color: SpringGreen;">Interactive Presentation with Streamlit: </span> 
                        Use Streamlit, an open-source app framework, to create an intuitive and interactive web application. This dynamic interface presents the data analysis project in a user-friendly manner, enabling stakeholders to interact with the data and fostering a deeper engagement with the analysis.
                    </div><br>
                    """, unsafe_allow_html=True)

    st.write("""<div >
                    <span style="color: OrangeRed;">Technologies Used: </span> 
                    Selenium, Beautiful Soup, Pandas, Plotly, Seaborn, Streamlit
                    </div><br>
                    """, unsafe_allow_html=True)

    st.write("""<div >
                    <span style="color: green;">💡</span>
                    <span style="color: OrangeRed;">Goal: </span> 
                    The aim is to gain insights from the data collected from the Hosco website, identifying trends, patterns, and opportunities within the hospitality industry, and presenting these findings through an interactive web application.
                        </div>
                        <hr><br><br><br>
                        """, unsafe_allow_html=True)





    st.write("""
            <div style="font-size: xx-large;">
            Data Analysis Project: Leveraging Data Scraping and Visualization for Insights in the Hospitality Industry 
            </div><hr>
            """, unsafe_allow_html=True)
    st.markdown('https://goa-resort-analysis.streamlit.app/')

    st.write("""
        <div>
            <span style="color: green;">🔸</span>
            <span style="color: OrangeRed;"> Keywords:</span> 
            Data scraping, web automation, data cleaning, data visualization, hospitality industry
        </div><br>
        """, unsafe_allow_html=True)

    st.subheader('Project Overview:')
    st.write('In the age of digital transformation, data analysis has become a pivotal tool for making informed decisions across various domains. Our project embarks on this journey by leveraging advanced data scraping and analysis techniques to derive meaningful insights from the Booking.com website. Booking.com, a prominent platform in the hospitality industry,')

    st.subheader('Project Components:')

    st.write("""
        <div style="margin-left: 20px;">
            <span style="color: green;">💠</span>
            <span style="color: OrangeRed;">Part 1: </span> 
            Data Acquisition and Parsing
        </div><br>
        """, unsafe_allow_html=True)

    st.write("""
            <div style="margin-left: 80px;">
                <span style="color: green;">🔸</span>
                <span style="color: SpringGreen;">Web Scraping with Selenium: </span> 
                 Utilize Selenium to automate the process of extracting data from the Booking.com website. Selenium's robust automation capabilities enable efficient navigation of the website, ensuring comprehensive data collection.
            </div><br>
            """, unsafe_allow_html=True)

    st.write("""
                <div style="margin-left: 80px;">
                    <span style="color: green;">🔸</span>
                    <span style="color: SpringGreen;">Data Parsing with Beautiful Soup: </span> 
                      Employ Beautiful Soup to parse the HTML content, extracting relevant data encapsulated within the web pages.
                </div><br>
                """, unsafe_allow_html=True)

    st.write("""
            <div style="margin-left: 20px;">
                <span style="color: green;">💠</span>
                <span style="color: OrangeRed;">Part 2: </span> 
                Data Cleaning and Preparation
            </div><br>
            """, unsafe_allow_html=True)

    st.write("""
                    <div style="margin-left: 80px;">
                        <span style="color: green;">🔸</span>
                        <span style="color: SpringGreen;">Data Cleaning: </span> 
                          Conduct meticulous processing to remove inconsistencies, handle missing values, and standardize the dataset. This step ensures the dataset's readiness for analysis.
                    </div><br>
                    """, unsafe_allow_html=True)

    st.write("""
                        <div style="margin-left: 80px;">
                            <span style="color: green;">🔸</span>
                            <span style="color: SpringGreen;">Data Preparation with Pandas: </span> 
                              Leverage the powerful functionalities of the Pandas library to conduct a thorough examination and manipulation of the data, preparing it for subsequent analytical procedures.
                        </div><br>
                        """, unsafe_allow_html=True)

    st.write("""
            <div style="margin-left: 20px;">
                <span style="color: green;">💠</span>
                <span style="color: OrangeRed;">Part 3: </span> 
                Data Analysis and Visualization
            </div><br>
            """, unsafe_allow_html=True)

    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Country-Wise Analysis: </span> 
                                  Analyze data based on the country of origin of the reviewers.
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Rating-Wise Analysis: </span> 
                                  Explore trends and patterns based on the ratings given by reviewers.
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Room-Types Analysis: </span> 
                                  Examine differences in reviews based on different room types offered by the hotels.
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Traveller-Types Analysis: </span> 
                                  Segment reviews according to the types of travelers (e.g., solo travelers, families, couples).
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Booked-Wise Analysis: </span> 
                                  Analyze reviews based on types of bookings (e.g., direct bookings, through third-party websites).
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Reviewed-Wise Analysis: </span> 
                                  Explore reviews based on the length and content of the reviews.
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Nightly-Stay Analysis: </span> 
                                  Analyze trends based on the duration of stay (e.g., one-night stays, longer stays).
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                            <div style="margin-left: 80px;">
                                <span style="color: green;">🔸</span>
                                <span style="color: SpringGreen;">Visualization with Plotly and Seaborn: </span> 
                                  Utilize Plotly's interactive visualizations and Seaborn's statistical plotting capabilities to facilitate an in-depth exploration of the dataset. Identify trends, outliers, and significant patterns through these visualizations.
                            </div><br>
                            """, unsafe_allow_html=True)

    st.write("""
                <div style="margin-left: 20px;">
                    <span style="color: green;">💠</span>
                    <span style="color: OrangeRed;">Part 4: </span> 
                    Presentation and Interaction
                </div><br>
                """, unsafe_allow_html=True)

    st.write("""<div style="margin-left: 80px;">
                    <span style="color: green;">🔸</span>
                    <span style="color: SpringGreen;">Interactive Presentation with Streamlit: </span> 
                        Use Streamlit, an open-source app framework, to create an intuitive and interactive web application. This dynamic interface presents the data analysis project in a user-friendly manner, enabling stakeholders to interact with the data and fostering a deeper engagement with the analysis.
                    </div><br>
                    """, unsafe_allow_html=True)

    st.write("""<div >
                    <span style="color: OrangeRed;">Technologies Used: </span> 
                    Selenium, Beautiful Soup, Pandas, Plotly, Seaborn, Streamlit
                    </div><br>
                    """, unsafe_allow_html=True)

    st.write("""<div >
                    <span style="color: green;">💡</span>
                    <span style="color: OrangeRed;">Goal: </span> 
                    The aim is to gain insights from the Booking.com review data for the two hotels (Seashell Suites and Villas in Candolim Goa, and Taj Fort Aguada Resort & Spa, Goa), identifying trends, patterns, and opportunities within the hospitality industry, and presenting these findings through an interactive web application.
                        </div>
                        <hr>
                        """, unsafe_allow_html=True)




def load_certificates_page():
    import streamlit as st

    st.title('CERTIFICATE')

    import streamlit as st

    # Function to display course information with left margin
    def display_course(course_title, course_details, image_path):
        st.subheader(course_title)

        for detail in course_details:
            st.markdown(detail, unsafe_allow_html=True)

        with st.expander("View Image"):
            st.image(image_path)



    # Data Science Mentorship Program section
    st.subheader("Data Science Mentorship Program")

    # Description (if any)

    # Additional Info
    mentorship_details = [
        """<div style="margin-left: 40px;">
            <span style="color: green;">✔</span>
            <span style="color: red;">Foundations of Data Science:</span> 
            Understanding the basics of data manipulation, statistical analysis, and data visualization.
        </div>""",

        """<div style="margin-left: 40px;">
            <span style="color: green;">✔</span>
            <span style="color: red;">Machine Learning:</span> 
            Learning various machine learning algorithms, model evaluation, and optimization techniques.
        </div>""",

        """<div style="margin-left: 40px;">
            <span style="color: green;">✔</span>
            <span style="color: red;">Practical Projects:</span> 
            Working on real-world projects to apply theoretical knowledge and build a portfolio.
        </div>"""
    ]

    # Display Data Science Mentorship Program section
    for detail in mentorship_details:
        st.markdown(detail, unsafe_allow_html=True)

    with st.expander("View Image"):
        st.image('WhatsApp Image 2024-07-05 at 11.51.20_feba6b4a.jpg')

    # Course details
    courses = [
        {
            "title": "The Fundamental Of Hotel Distribution",
            "details": [
                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Overview of the Hospitality Industry:</span> 
                    Understanding the scope and scale of the hospitality sector, including hotels, restaurants, and travel services.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Management Principles:</span> 
                    Basics of managing a hotel, including leadership, human resources, financial management, and marketing.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Industry Trends:</span> 
                    Current trends and future directions in the hospitality industry.
                </div>"""
            ],
            "image_path": 'WhatsApp Image 2024-07-05 at 12.24.12_fafd9167.jpg'
        },
        {
            "title": "Cost and Economics In Price Strategy",
            "details": [
                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Pricing Fundamentals:</span> 
                    Learn the basic principles of pricing and how costs influence pricing decisions.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Pricing Strategies:</span> 
                    Study different pricing models and strategies used in various industries.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Cost Analysis:</span> 
                    Explore various cost concepts and their implications for pricing.
                </div>"""
            ],
            "image_path": 'Coursera Z6TB73ZRZAAN.jpg'
        },
        {
            "title": "The Fundamental Of Revenue Management",
            "details": [
                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Introduction to Revenue Management:</span> 
                    Understand the basics of revenue management and its importance in driving profitability.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Demand Forecasting:</span> 
                    Techniques and tools for predicting customer demand to make informed pricing decisions.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Technology in Revenue Management:</span> 
                    The role of software and technology in implementing revenue management strategies.
                </div>"""
            ],
            "image_path": 'Coursera 4LU2TGB8ZVSV.jpg'
        },
        {
            "title": "Demand Management",
            "details": [
                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Introduction to Demand Management:</span> 
                    Understanding the fundamentals of demand management and its significance in modern businesses.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Demand Forecasting:</span> 
                    Tools and methods for accurate demand forecasting and planning.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Technology in Demand Management:</span> 
                    The role of integrated systems and technologies in enhancing demand management practices.
                </div>"""
            ],
            "image_path": 'Coursera WX2Q7FLWVYAL.jpg'
        },
        {
            "title": "Sustainable Tourism: Promoting Environment and Public Health",
            "details": [
                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Introduction to Sustainable Tourism:</span> 
                    Understanding the concepts and importance of sustainability in the tourism industry.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Environmental Impact:</span> 
                    Strategies for minimizing the negative environmental impacts of tourism and promoting conservation.
                </div>""",

                """<div style="margin-left: 40px;">
                    <span style="color: green;">✔</span>
                    <span style="color: red;">Eco-friendly Practices:</span> 
                    Implementing eco-friendly practices in tourism operations, such as reducing waste, conserving water, and using renewable energy.
                </div>"""
            ],
            "image_path": 'Coursera ZWZABG4ESEVG.jpg'
        }
    ]

    # Display each course
    for course in courses:
        display_course(course["title"], course["details"], course["image_path"])


def load_academic_background_page():
    st.title('Academic Background')

    col1, col2 = st.columns(2)



    with col1:
        st.image('ssj.png')
    with col2:
        
        st.write('My academic journey has always been shaped by my passion for mathematics and coding. Starting from my BSc in Mathematical Sciences, I immersed myself in a diverse range of subjects, including mathematics, statistics, and computer science. These disciplines not only ignited my curiosity but also honed my analytical and computational skills')

    st.subheader('My Journey 🚩')
    st.write('📜 Bachelors in Maths | SSJ University')
    st.write('1/06/2021 - 1/6/2024')

    st.write("""
    <div style="margin-left: 40px;">
        <span style="color: green;">🔸</span>
        <span style="color: pink;">Relevant Courses:</span> 
        Maths, Statistics, Python, SQL, Hypothesis Testing, Numerical Analysis.
    </div>
    """, unsafe_allow_html=True)

    st.write("""
        <div style="margin-left: 40px;">
            <span style="color: green;">🔸</span>
            <span style="color: pink;"> Motivation for Bachelors :</span> 
            Deepening of machine learning & Statistical theoretical foundations and honing my data science & analyst skills.
        </div>
        """, unsafe_allow_html=True)

    st.write("""
            <div style="margin-left: 40px;">
                <span style="color: green;">🔸</span>
                <span style="color: pink;"> Difficulties :</span> 
                Adjusting to the level of knowledge and skill required in internship and job interviews.
            </div>
            """, unsafe_allow_html=True)

    st.write("""
                <div style="margin-left: 40px;">
                    <span style="color: green;">🔸</span>
                    <span style="color: pink;"> What I learned :</span> 
                     The best way to learn is to enjoy the process of going from 0 to 1 and not be frustrated at 0.5.
                </div>
                """, unsafe_allow_html=True)

    st.image('books photo.jpg')













select=st.sidebar.selectbox('select:' , ['🏡 home','🧪 Personal Project','🥇 Certificates','🏫 Academic Background'])

if select=='🏡 home':
    load_home_page()

elif select=='🧪 Personal Project':
    load_pp_page()

elif select=='🥇 Certificates':
    load_certificates_page()

else:
    load_academic_background_page()

















