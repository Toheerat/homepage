import streamlit as st
import csv

# Function to display recommendations based on user answers
def show_recommendations():


    # Recommendations based on user answers
    st.subheader("Data:")
    st.write("1. If the answer to 'What is the state of your organisational data and content?' is poor or fair, the organisation should focus on improving its data management strategies and processes. This can be done by investing in data quality tools and technologies and establishing clear data governance policies.")
    st.write("2. If there are key concerns related to data management strategies that make information secure and shareable, the organisation should prioritize data security and privacy. This can be achieved by implementing robust data security measures and ensuring compliance with data protection regulations.")
    
    st.subheader("Technical Infrastructure:")
    st.write("3. If the answer to 'Does your organisation have the vision, support, and drive to enable successful AI solutions?' is negative, the organisation should focus on building a strong AI vision and gaining leadership support. This can be done by educating the leadership team on the potential benefits of AI and how it can help the organisation achieve its business objectives.")
    st.write("4. If the answer to 'Is your organisation ready to consider AI-related initiatives?' is negative, the organisation should focus on building awareness and understanding of AI and its potential benefits. This can be done by organising training sessions and workshops for employees and stakeholders.")
    
    st.subheader("Talent and Skills:")
    st.write("5. If the answer to 'What is your organisation's AI maturity level?' is novice or intermediate, the organisation should focus on building its AI capabilities and expertise. This can be done by investing in AI training and education programs for employees and hiring AI experts.")
    
    st.subheader("Problem-Solving:")
    st.write("6. If the answer to 'What is your organisation's first AI initiative?' is any specific AI initiative, the organisation should evaluate the potential impact of the initiative on the business and ensure that it aligns with its overall AI strategy. The organisation should also ensure that it has the necessary resources and expertise to implement the initiative successfully.")
    st.write("7. If the answer to 'What are the success criteria for your target AI initiatives?' is any specific criteria, the organisation should define the success criteria for its AI initiatives and measure their impact on the business. This can be done by establishing clear KPIs and metrics that align with the organisation's overall AI strategy.")
    st.write("8. If the answer to 'What are the potential business values that could be realized once the target state is achieved?' is any specific values, the organisation should identify the potential benefits of AI adoption and prioritize its initiatives accordingly. This can be done by conducting a cost-benefit analysis and evaluating the potential ROI of each AI initiative.")
    st.write("9. If the answer to 'What are the ethical implications of AI adoption in your organisation?' is any specific implications, the organisation should be aware of the ethical implications of AI adoption and develop clear policies and guidelines to address them. This can be done by establishing an AI ethics committee and conducting regular audits of AI systems to ensure compliance with ethical standards.")

# Dictionary to store user answers
user_answers = {}

# Context for each question
context = [
    "CONTEXT: We are interested in understanding the level of alignment within your organization towards adopting AI solutions. This question assesses whether there is a clear vision and support from leadership to implement AI initiatives and the overall drive within the organization to embrace AI technologies.",
    "CONTEXT: This question aims to gauge your organization's current readiness to explore AI-related initiatives. We want to know how open and prepared your organization is to venture into AI-driven projects.",
    "CONTEXT: Understanding the quality and state of your organizational data and content is crucial for assessing AI readiness. This question helps us identify the existing condition of your data and content, which is essential for successful AI implementation.",
    "CONTEXT: We are interested in understanding your organization's level of AI maturity. This question assesses the extent to which your organization has already adopted and integrated AI technologies into its operations.",
    "CONTEXT: Identifying your organization's initial AI initiative allows us to gain insights into the specific AI projects you are considering or have already implemented.",
    "CONTEXT: This question aims to evaluate the level of AI adoption within your organization. We want to know to what extent AI technologies have been integrated into various aspects of your company's operations.",
    "CONTEXT: Understanding your organization's AI readiness level helps us assess how prepared you are to embrace and implement AI solutions.",
    "CONTEXT: This question aims to identify the areas where your organization excels in adopting AI technologies and where there may be room for improvement.",
    "CONTEXT: Assessing your organization's readiness to implement an AI project is crucial for understanding the feasibility and potential success of AI initiatives.",
    "CONTEXT: We are interested in understanding the specific outcomes your organization aims to achieve with the implementation of AI initiatives.",
    "CONTEXT: This question aims to identify the potential benefits your organization envisions from successfully adopting AI technologies.",
    "CONTEXT: Understanding the ethical implications of AI adoption helps us assess your organization's consideration of ethical concerns in the implementation of AI technologies.",
    "CONTEXT: This question focuses on identifying the primary concerns your organization has regarding data management strategies to ensure data security and shareability.",
    "CONTEXT: This question aims to understand your organization's understanding and consideration of various aspects that contribute to AI readiness, such as strategy, people and processes, data, technology and platforms, and ethical implications."
    ]

# Questions and options
questions = [
    {
        "question": "1. Does your organisation have the vision, support, and drive to enable successful AI solutions?",
        "options": [
            "Strongly disagree",
            "Disagree",
            "Somewhat disagree",
            "Neutral",
            "Somewhat agree",
            "Agree",
            "Strongly agree"
        ],
    },
    {
        "question": "2. Is your organisation ready to consider AI-related initiatives?",
        "options": [
            "Not at all ready",
            "Not very ready",
            "Somewhat ready",
            "Moderately ready",
            "Very ready",
            "Extremely ready"
        ],
    },
    {
        "question": "3. What is the state of your organisational data and content?",
        "options": [
            "Poor",
            "Fair",
            "Good",
            "Very good",
            "Excellent"
        ],
    },
    {
        "question": "4. What is your organisation's AI maturity level?",
        "options": [
            "Novice",
            "Intermediate",
            "Advanced",
            "Expert"
        ],
    },
    {
        "question": "5. What is your organisation's first AI initiative?",
        "options": [
            "Chatbots",
            "Predictive maintenance",
            "Fraud detection",
            "Customer service automation",
            "Other"
        ],
    },
    {
        "question": "6. How well adopted is AI-tech within your company?",
        "options": [
            "Not at all adopted",
            "Not very adopted",
            "Somewhat adopted",
            "Moderately adopted",
            "Very adopted",
            "Extremely adopted"
        ],
    },
    {
        "question": "7. What is your organisation's AI readiness level?",
        "options": [
            "Not at all ready",
            "Not very ready",
            "Somewhat ready",
            "Moderately ready",
            "Very ready",
            "Extremely ready"
        ],
    },
    {
        "question": "8. What are your organisation's strengths and weaknesses in terms of AI adoption?",
        "options": [
            "Strengths: Data management, technology capabilities, governance, change management",
            "Weaknesses: Data management, technology capabilities, governance, change management"
        ],
    },
    {
        "question": "9. What is your organisation's readiness to implement an AI project?",
        "options": [
            "Not at all ready",
            "Not very ready",
            "Somewhat ready",
            "Moderately ready",
            "Very ready",
            "Extremely ready"
        ],
    },
    {
        "question": "10. What are the success criteria for your target AI initiatives?",
        "options": [
            "Improved efficiency",
            "Increased revenue",
            "Improved customer experience",
            "Improved decision-making",
            "Other"
        ],
    },
    {
        "question": "11. What are the potential business values that could be realised once the target state is achieved?",
        "options": [
            "Cost savings",
            "Increased revenue",
            "Improved customer experience",
            "Improved decision-making",
            "Other"
        ],
    },
    {
        "question": "12. What are the ethical implications of AI adoption in your organisation?",
        "options": [
            "Bias",
            "Privacy",
            "Security",
            "Transparency",
            "Other"
        ],
    },
    {
        "question": "13. What are the key concerns related to data management strategies that make information secure and shareable?",
        "options": [
            "Data privacy",
            "Data security",
            "Data quality",
            "Data governance"
        ],
    },
    {
        "question": "14. What are the distinct but interdependent areas in which to assess AI readiness, including strategy, people and processes, data, technology and platforms, and ethical implications?",
        "options": [
            "Strategy",
            "People and processes",
            "Data",
            "Technology and platforms",
            "Ethical implications"
        ],
    },
]





# Function to respond to user input for the chatbot
def get_chatbot_response(user_input):
    if user_input in faq_data:
        return faq_data[user_input]
    else:
        return "I'm sorry, I don't have the answer to that question. Please contact our support team for further assistance."

# Sidebar Pages
st.sidebar.title("Pages")
pages = ["Home", "AI Readiness Quiz", "Industry-based AI Recommendation", "Learn More Resources", "Chatbot", "AI Adoption Benchmarking", "Feedback Form"]
selected_page = st.sidebar.radio("", pages)

# Home page
if selected_page == "Home":
    st.title("Adopting AI and Machine Learning for your Business")
    st.markdown("""This free online tool provides guidance and resources to help your small and medium enterprise assess readiness and adopt AI/ML technologies in a responsible and effective manner. By answering a few short questions, you'll receive a customised AI readiness score and recommendations to get started on your AI journey.""")
    st.markdown("""Assess your AI readiness in 5 minutes""")
  


# AI Readiness Quiz page
elif selected_page == "AI Readiness Quiz":
    st.title("AI and Machine Learning Readiness Quiz")
    for index, question in enumerate(questions):
        st.subheader(f"{question['question']}\n{context[index]}")
        key = question["question"]  # Use the question as the key
        selected_option = st.radio(key, options=question["options"])
        user_answers[question["question"]] = selected_option


    st.subheader("Thank you for answering the questions!")
    # Show recommendations button
    st.write("Click the button below to show the recommendations:")
    if st.button("SHOW RECOMMENDATION"):
        show_recommendations()
# Industry-based AI Recommendation page
elif selected_page == "Industry-based AI Recommendation":
    st.title("Industry-based AI Recommendation")

    # Function to display recommendations based on the selected industry
    def display_recommendation(industry):
        # ... (Recommendation dictionary goes here)
        recommendations = {
        "Information Technology (IT)": "Implement autonomous machine learning tools for IT infrastructure management and cybersecurity. These tools can continuously analyze data to detect anomalies, identify potential threats, and automate responses to security incidents, thereby enhancing the overall security posture of the organization.",
        "Finance and Banking": "Utilize autonomous machine learning tools for fraud detection and risk assessment in financial transactions. These tools can analyze vast amounts of data to identify fraudulent patterns and potential risks, helping SMEs safeguard their financial operations.",
        "E-commerce": "Adopt autonomous machine learning tools for personalized product recommendations and customer segmentation. These tools can analyze customer behavior and preferences to offer tailored product recommendations and enhance the overall shopping experience, leading to increased customer satisfaction and sales.",
        "Automotive": "Implement autonomous machine learning tools for predictive maintenance and vehicle diagnostics. These tools can monitor vehicle data in real-time and proactively predict maintenance needs, reducing downtime and improving vehicle performance.",
        "Education": "Integrate autonomous machine learning tools for personalized learning and student performance analysis. These tools can assess individual student progress, identify areas of improvement, and suggest customized learning paths, ultimately enhancing learning outcomes.",
        "Travel and Tourism": "Deploy autonomous machine learning tools for dynamic pricing and customer experience optimization. These tools can analyze market trends, customer preferences, and competitor pricing to optimize pricing strategies and improve the overall travel experience for customers.",
        "Entertainment": "Utilize autonomous machine learning tools for content recommendation and audience engagement. These tools can analyze user behavior and content preferences to recommend personalized entertainment options, increasing user engagement and retention.",
        "Real Estate": "Implement autonomous machine learning tools for property price prediction and market analysis. These tools can analyze real estate market data and property attributes to predict property prices and provide valuable insights for informed decision-making in the real estate industry.",
        "Healthcare": "Implement autonomous machine learning for medical image analysis to assist radiologists in detecting and diagnosing diseases from X-rays, CT scans, and MRI images with greater accuracy and efficiency.\nUse autonomous AI-powered virtual health assistants to provide personalized healthcare information, reminders for medication, and support for patients with chronic conditions.\nAdopt autonomous machine learning for predictive analytics in healthcare to identify high-risk patients and optimize treatment plans for better patient outcomes.\nUtilize autonomous AI-driven chatbots for healthcare customer support to address patient queries, provide appointment scheduling, and offer basic medical advice.",
        "Aerodynamics": "Implement autonomous machine learning for aerodynamic simulations and analysis to optimize aircraft design, reduce drag, and improve fuel efficiency.\nUse autonomous AI-powered drones for aerial inspections and data collection in the aerospace industry, such as inspecting aircraft structures, monitoring infrastructure, and conducting environmental surveys.\nAdopt autonomous machine learning for predictive maintenance of aircraft to identify potential issues in engine performance and other critical components, reducing maintenance costs and improving safety.\nUtilize autonomous AI-based flight control systems to enhance aircraft navigation, stability, and response to various flight conditions."
    }

        return recommendations.get(industry, "No recommendation available for the selected industry.")


    industries = [
        "Information Technology (IT)",
        "Finance and Banking",
        "E-commerce",
        "Automotive",
        "Education",
        "Travel and Tourism",
        "Entertainment",
        "Real Estate",
        "Healthcare",
        "Aerodynamics"
        ]

    selected_industry = st.radio("Select an Industry:", industries)

    # Display recommendation based on the selected industry
    if st.button("Show Recommendation"):
        recommendation = display_recommendation(selected_industry)
        st.subheader("Recommendation:")
        st.write(recommendation)

# Learn More Resources page
elif selected_page == "Learn More Resources":
    st.header('Learn More Resources')
    st.markdown("Here are some educational materials such as articles, videos, and ebooks on the adoption of AI")

    # Case Studies
    st.header("Case Studies")
    st.markdown("[Microsoft AI Customer Stories](https://www.microsoft.com/en-us/ai/customer-stories)")
    st.markdown("[Google Cloud AI Solutions](https://cloud.google.com/solutions/ai)")
    st.markdown("[IBM Watson Success Stories](https://www.ibm.com/watson/customer-stories)") 

    # Success Stories section
    st.header("Success Stories")
    st.markdown("[Microsoft AI Customer Stories](https://www.microsoft.com/en-us/ai/customer-stories)")
    st.markdown("[Google Cloud AI Solutions](https://cloud.google.com/solutions/ai)")
    st.markdown("[IBM Watson Success Stories](https://www.ibm.com/watson/customer-stories)")


    # Best Practices and Guides
    st.header("Best Practices and Guides")
    st.markdown("[AI/ML Adoption Playbook by Accenture](https://www.accenture.com/us-en/insights/artificial-intelligence/ai-adoption-playbook)")
    st.markdown("[Machine Learning Engineering Best Practices by Google](https://developers.google.com/machine-learning/guides/rules-of-ml)")
    st.markdown("[AI Adoption and Ethics Toolkit by The Alan Turing Institute](https://www.turing.ac.uk/research/research-programmes/ai-adoption-and-ethics)")

    # Research Papers and Reports
    st.header("Research Papers and Reports")
    st.markdown("[McKinsey Global Institute: Artificial Intelligence: The Next Digital Frontier](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/artificial-intelligence-the-next-digital-frontier)")
    st.markdown("[Deloitte Insights: State of AI in the Enterprise](https://www2.deloitte.com/insights/us/en/focus/cognitive-technologies/state-of-ai-and-intelligent-automation-in-business-survey.html)")
    st.markdown("[Gartner: Hype Cycle for Artificial Intelligence](https://www.gartner.com/en/documents/3983831/hype-cycle-for-artificial-intelligence-2021)")

    # Online Courses and Tutorials
    st.header("Online Courses and Tutorials")
    st.markdown("[Coursera: AI for Everyone by deeplearning.ai](https://www.coursera.org/learn/ai-for-everyone)")
    st.markdown("[edX: Introduction to Artificial Intelligence (AI) by IBM](https://www.edx.org/professional-certificate/ibm-introduction-to-artificial-intelligence)")
    st.markdown("[Fast.ai: Practical courses on deep learning](https://www.fast.ai/)")

    # Industry Blogs and Publications
    st.header("Industry Blogs and Publications")
    st.markdown("[Towards Data Science](https://towardsdatascience.com/)")
    st.markdown("[KDnuggets](https://www.kdnuggets.com/)")
    st.markdown("[O'Reilly AI](https://www.oreilly.com/ai/)")



# Chatbot page
elif selected_page == "Chatbot":
    st.header("Chatbot")

    # Hardcoded FAQ data
    faq_data = {
        "What is AI?": "Artificial Intelligence (AI) is the field of study that focuses on creating intelligent machines that can perform tasks requiring human-like intelligence.",
        "What is machine learning?": "Machine Learning (ML) is a subset of AI that enables systems to learn and make predictions or decisions without being explicitly programmed.",
        "How can I adopt AI in my business?": "To adopt AI in your business, start by identifying potential use cases, collecting relevant data, and implementing appropriate machine learning models or algorithms.",
        "How can I adopt AI in my business?": "To adopt AI in your business, start by identifying potential use cases, collecting relevant data, and implementing appropriate machine learning models or algorithms.",
        "What are the different types of Machine Learning?": "There are three main types of Machine Learning: supervised learning (labeled data), unsupervised learning (unlabeled data), and reinforcement learning (learning through trial and error with rewards or penalties).",
        "are some real-life applications of AI and Machine Learning?": "AI and Machine Learning are used in various fields, such as healthcare (diagnosis, drug discovery), finance (fraud detection, risk assessment), transportation (autonomous vehicles), and customer service (chatbots).",
        "What are Neural Networks?": "Neural Networks are a type of machine learning model inspired by the structure of the human brain. They consist of interconnected layers of artificial neurons that process and analyze data to make predictions.",
        "What is Deep Learning?" : "Deep Learning is a subfield of Machine Learning that focuses on training large-scale neural networks with multiple layers. It has achieved remarkable success in tasks such as image recognition and natural language processing.",
        "What is the role of data in Machine Learning": "Data plays a crucial role in Machine Learning. High-quality, diverse, and well-labeled data is used to train models. The more data available, the better the model's performance and generalization.",
        "What are the ethical considerations in AI and Machine Learning?": "Ethical considerations in AI and Machine Learning involve issues such as privacy, bias, transparency, accountability, and the impact of automation on jobs. It is essential to develop and use AI responsibly and ethically.",
        "Can machines become more intelligent than humans?": "The concept of machines surpassing human intelligence, known as artificial general intelligence (AGI), is still hypothetical. While AI systems can excel in specific tasks, replicating the complexity and breadth of human intelligence remains a significant challenge.",
        "What is the AI Readiness Toolkit?": "The AI Readiness Toolkit is a comprehensive resource that focuses on six main dimensions of readiness: defining real-world problems that AI can address, leveraging the right technologies and best practices, optimizing operations and developing a strong team, generating and processing the right data, and providing granular recommendations for improvement on each dimension.",
        "How can the AI Readiness Toolkit help my small or medium enterprise?": "The AI Readiness Toolkit provides guidance and resources to help your organization assess its readiness and adopt AI/ML technologies in a responsible and effective manner. It offers recommendations, hyperlinked external resources, and a quantitative assessment to track improvements over time.",
        "What are some discussion questions for AI readiness?": "The discussion questions for AI readiness are designed to foster conversations and identify opportunities for AI adoption within your organization. They cover topics such as competitive advantages, employee feedback, operational optimization, AI investments, and data organization.",
        "How can the AI readiness checklist benefit my organization?": "The AI readiness checklist is a valuable resource to avoid AI pitfalls and ensure optimal AI utilization. It provides key questions that you and your stakeholders should be asking with every AI use case, helping you navigate through the complexities of AI adoption and engage stakeholders effectively.",
        "What are some organizational AI readiness factors?": "Organizational AI readiness factors are crucial for making purposeful decisions in the AI journey. While the search results did not provide specific factors, the study mentioned in the search results aims to conceptualize relevant factors that contribute to organizational AI readiness.",
        "How can I assess my organization's AI readiness level?": "Assessing your organization's AI readiness level involves considering factors such as your company's goals with AI, growth strategy, and competitive advantage. By evaluating these elements, you can determine your organization's readiness to embrace AI and identify areas for improvement.",
        "What is an AI Readiness Workshop?": "An AI Readiness Workshop offered by Google Cloud Consulting is a two- to three-week engagement designed to accelerate value realization from your AI efforts. It helps you understand your business objectives, benchmark your AI capabilities, and provides tailored recommendations and a roadmap for AI adoption.",
        "What is autonomous machine learning?": "Autonomous machine learning refers to the use of automated processes and algorithms that enable machines or systems to independently perform the entire process of learning from data, model building, and making decisions or predictions without human intervention.",
        "How can autonomous machine learning be beneficial for a business?": "Autonomous machine learning can be beneficial for a business in several ways:\n- It reduces the need for human intervention, saving time and resources.\n- It can process large volumes of data quickly and efficiently.\n- It improves decision-making by leveraging real-time data and insights.\n- It allows businesses to scale and adapt to changing conditions more effectively.",
        "Can you provide an example of how a business might adopt autonomous machine learning decisions?": "A business could use autonomous machine learning to automate customer support through chatbots. The chatbot could use natural language processing to understand customer inquiries, learn from past interactions, and autonomously provide appropriate responses or escalate issues to human agents when necessary.",
        "What types of businesses or industries can benefit the most from adopting autonomous machine learning?": "Industries dealing with vast amounts of data and complex decision-making can benefit the most, including finance, healthcare, manufacturing, logistics, e-commerce, and marketing.",
        "What are some key factors to consider when implementing autonomous machine learning into a business model?": "- Data quality and availability: Ensure that the data used for training and decision-making is accurate and sufficient.\n- Transparency and explainability: Understand how the autonomous system makes decisions and be able to explain its outputs.\n- Monitoring and auditing: Continuously monitor the system's performance and audit its decisions to detect and correct biases or errors.\n- Human oversight: Have a process in place to intervene or override the autonomous system if needed.",
        "How can autonomous machine learning improve decision-making processes in a business?": "Autonomous machine learning can improve decision-making by:\n- Analyzing large datasets quickly and accurately.\n- Identifying patterns, trends, and insights that humans might miss.\n- Providing real-time recommendations based on the latest data.\n- Reducing human biases and errors in decision-making.",
        "What are some potential challenges or risks that a business might face when adopting autonomous machine learning?": "- Data privacy and security concerns.\n- Lack of transparency and interpretability in the decision-making process.\n- Overreliance on autonomous systems without human oversight.\n- Ethical considerations regarding the impact of decisions made by machines.",
        "What steps can a business take to ensure the successful adoption of autonomous machine learning?": "- Start with a well-defined use case and a clear problem statement.\n- Invest in high-quality data collection and preparation.\n- Collaborate with data scientists and domain experts to build robust models.\n- Implement a gradual rollout to test and validate the system's performance.\n- Continuously monitor and update the system as needed.",
        "Can you explain the concept of a machine learning model and how it fits into an autonomous system?": "A machine learning model is a mathematical algorithm that learns patterns and relationships from data. In an autonomous system, the machine learning model is a crucial component responsible for processing data, making predictions, and providing decisions or actions without requiring human intervention.",
        "How can a business measure the success or effectiveness of its autonomous machine learning adoption?": "The success of autonomous machine learning adoption can be measured through various metrics, such as:\n- Accuracy and performance of the autonomous system compared to human decisions or alternative approaches.\n- Efficiency gains in terms of time and cost savings.\n- Reduction in errors"
        }


    # Text input for user questions
    user_question = st.text_input("Ask a question")

    # Chatbot response
    if st.button("Ask"):
        if user_question:
            chatbot_response = get_chatbot_response(user_question)
            st.text_area("Chatbot Response", value=chatbot_response, height=200, max_chars=None)
        else:
            st.warning("Please enter a question.")

# AI Adoption Benchmarking page
elif selected_page == "AI Adoption Benchmarking":
    st.header('Benchmarking')

    # UK benchmarks for AI/ML adoption
    uk_benchmarks = {
        "Readiness Score": 8,
        "Data Quality": 7,
        "Technical Infrastructure": 6,
        "Talent and Skills": 8,
        # Add more benchmarks as needed
    }

    st.header('Technology Readiness Level (TRL): Assessing Technology and System Maturity')
    st.write("Technology Readiness Level (TRL) is a common scale used to assess the maturity of a technology or system. The higher the TRL level, the more advanced and mature the technology is in its development and implementation.")

    # Description of TRL levels
    st.write("TRL 1 - Basic principles observed and reported: Your organization is in the initial stages of understanding and observing AI principles and concepts.")
    st.write("TRL 2 - Technology concept and/or application formulated: Your organization has formulated a general idea of how AI can be applied in your business, but it is still at the conceptual stage.")
    st.write("TRL 3 - Analytical and experimental critical function and/or characteristic proof of concept: Your organization has conducted some initial experiments and analysis to prove the concept of AI application, but it is not yet at a practical implementation stage.")
    st.write("TRL 4 - Component and/or breadboard validation in a laboratory environment: Your organization has validated some AI components or modules in a controlled laboratory environment, but it has not been tested in real-world conditions.")
    st.write("TRL 5 - Technology validated in a relevant environment: Your organization has validated the AI technology in an environment that closely simulates real-world conditions relevant to your business needs.")
    st.write("TRL 6 - Technology demonstrated in a relevant environment: Your organization has demonstrated the AI technology in an environment that closely represents your actual business setting.")
    st.write("TRL 7 - System prototype demonstration in an operational environment: Your organization has developed a prototype of the AI system and demonstrated its functionality in an operational environment.")
    st.write("TRL 8 - System complete and approved: Your organization has completed the AI system development, and it has been approved for implementation within your business operations.")
    st.write("TRL 9 - Actual system proven in its operational environment: The AI system has been fully implemented and proven to be effective and efficient in your business operations. It has been used extensively in your business processes and has undergone competitive manufacturing or real-world application.")

    # User input for readiness score
    user_readiness_score = st.number_input("Enter your readiness score", min_value=0, max_value=10, step=1)
    # User input for Data Quality
    user_Data_Quality = st.number_input("Enter your Data Quality", min_value=0, max_value=10, step=2)
    # User input for Technical Infrastructure
    user_Technical_Infrastructure = st.number_input("Enter your Technical Infrastructure", min_value=0, max_value=10, step=3)
    # User input for Technical Infrastructure
    user_Talent_and_Skills = st.number_input("Enter your Talent and Skills", min_value=0, max_value=10, step=4)

    # Compare readiness score to benchmarks
    if st.button("Compare"):
        if user_readiness_score:
            st.subheader("Benchmark Comparison")
            for benchmark, score in uk_benchmarks.items():
                st.write(f"{benchmark}:")
                st.progress(user_readiness_score / score)
        else:
            st.warning("Please enter your readiness score.")

# Feedback Form page
elif selected_page == "Feedback Form":
    # Title and description
    st.title("Feedback Form")
    st.write("Please provide your feedback and suggestions.")

    # Feedback form
    feedback = st.text_area("Comments or Suggestions")

    # Submit button
    if st.button("Submit", key="submit_button"):
        if feedback:
            # Save feedback to CSV file
            with open('feedback.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([feedback])
            st.success("Thank you for your feedback!")
            st.write("Your feedback has been submitted successfully.")
        else:
            st.warning("Please enter your feedback before submitting.")
