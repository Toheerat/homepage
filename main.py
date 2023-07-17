import streamlit as st

st.title("Adopting AI and Machine Learning for your Business")
st.markdown("""This free online tool provides guidance and resources to help your small and medium enterprise assess readiness and adopt AI/ML technologies in a responsible and effective manner. By answering a few short questions, you'll receive a customised AI readiness score and recommendations to get started on your AI journey.""")
st.button("Assess your AI readiness in 5 minutes")

# Import libraries
# Title
st.title("AI and Machine Learning Readiness Quiz")

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

# Dictionary to store user answers
user_answers = {}

# Display questions and collect user answers
for question in questions:
    st.subheader(question["question"])
    key = question["question"]  # Use the question as the key
    selected_option = st.radio(key, options=question["options"])
    user_answers[question["question"]] = selected_option

st.subheader("Thank you for answering the questions!")

# Display recommendations based on user answers
if st.button("Show Recommendations"):
    st.subheader("Recommendations:")
    for question in questions:
        recommendation = ""  # Placeholder for recommendation
        if question["question"] in user_answers:
            selected_option = user_answers[question["question"]]
            # Add conditions to match user answers and display recommendations accordingly
            if question["question"] == "1. Does your organisation have the vision, support, and drive to enable successful AI solutions?":
                if selected_option in ["Strongly disagree", "Disagree", "Somewhat disagree"]:
                    recommendation = "Focus on building a strong AI vision and gaining leadership support. Educate the leadership team on the potential benefits of AI and how it can help the organisation achieve its business objectives."
            elif question["question"] == "2. Is your organisation ready to consider AI-related initiatives?":
                if selected_option in ["Not at all ready", "Not very ready"]:
                    recommendation = "Focus on building awareness and understanding of AI and its potential benefits. Organise training sessions and workshops for employees and stakeholders."
            elif question["question"] == "3. What is the state of your organisational data and content?":
                if selected_option in ["Poor", "Fair"]:
                    recommendation = "Focus on improving data management strategies and processes. Invest in data quality tools and technologies, and establish clear data governance policies."
            elif question["question"] == "4. What is your organisation's AI maturity level?":
                if selected_option in ["Novice", "Intermediate"]:
                    recommendation = "Focus on building AI capabilities and expertise. Invest in AI training and education programs for employees and hire AI experts."
            elif question["question"] == "5. What is your organisation's first AI initiative?":
                recommendation = "Evaluate the potential impact of the first AI initiative on the business and ensure it aligns with the overall AI strategy. Ensure the necessary resources and expertise are available to implement the initiative successfully."
            elif question["question"] == "6. How well adopted is AI-tech within your company?":
                if selected_option in ["Not very adopted", "Somewhat adopted"]:
                    recommendation = "Focus on building awareness and understanding of AI and its potential benefits. Organise training sessions and workshops for employees and stakeholders."
            elif question["question"] == "7. What is your organisation's AI readiness level?":
                recommendation = "Evaluate the AI readiness level and identify areas for improvement. Conduct an AI readiness assessment and develop an AI roadmap that outlines the necessary steps to achieve AI goals."
            elif question["question"] == "8. What are your organisation's strengths and weaknesses in terms of AI adoption?":
                recommendation = "Leverage strengths to build AI capabilities and address weaknesses. Invest in AI training and education programs for employees and hire AI experts."
            elif question["question"] == "9. What is your organisation's readiness to implement an AI project?":
                recommendation = "Evaluate readiness to implement an AI project and identify potential barriers to success. Conduct an AI readiness assessment and develop an AI roadmap that outlines the necessary steps to achieve AI goals."
            elif question["question"] == "10. What are the success criteria for your target AI initiatives?":
                recommendation = "Define the success criteria for AI initiatives and measure their impact on the business. Establish clear KPIs and metrics that align with the organisation's overall AI strategy."
            elif question["question"] == "11. What are the potential business values that could be realised once the target state is achieved?":
                recommendation = "Identify the potential benefits of AI adoption and prioritise initiatives accordingly. Conduct a cost-benefit analysis and evaluate the potential ROI of each AI initiative."
            elif question["question"] == "12. What are the ethical implications of AI adoption in your organisation?":
                recommendation = "Be aware of the ethical implications of AI adoption and develop clear policies and guidelines to address them. Establish an AI ethics committee and conduct regular audits of AI systems to ensure compliance with ethical standards."
            elif question["question"] == "13. What are the key concerns related to data management strategies that make information secure and shareable?":
                recommendation = "Focus on improving data management strategies and processes to ensure information is secure and shareable. Invest in data quality tools and technologies, and establish clear data governance policies."
            elif question["question"] == "14. What are the distinct but interdependent areas in which to assess AI readiness, including strategy, people and processes, data, technology and platforms, and ethical implications?":
                recommendation = "Evaluate each of these areas to assess AI readiness and develop an effective AI strategy. Conduct an AI readiness assessment and develop an AI roadmap that outlines the necessary steps to achieve AI goals."
            
            # Display the recommendation if it exists
            if recommendation:
                st.markdown(f"- {recommendation}")


st.header('Learn More Resources')
st.markdown("Here are some educational materials such as articles, videos, and ebooks on the adoption of AI")

# Case Studies
st.header("Case Studies")
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



# Load chatbot model

# Hardcoded FAQ data
faq_data = {
    "What is AI?": "Artificial Intelligence (AI) is the field of study that focuses on creating intelligent machines that can perform tasks requiring human-like intelligence.",
    "What is machine learning?": "Machine Learning (ML) is a subset of AI that enables systems to learn and make predictions or decisions without being explicitly programmed.",
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
    "What is an AI Readiness Workshop?": "An AI Readiness Workshop offered by Google Cloud Consulting is a two- to three-week engagement designed to accelerate value realization from your AI efforts. It helps you understand your business objectives, benchmark your AI capabilities, and provides tailored recommendations and a roadmap for AI adoption."
}

# Function to respond to user input
def get_chatbot_response(user_input):
    if user_input in faq_data:
        return faq_data[user_input]
    else:
        return "I'm sorry, I don't have the answer to that question. Please contact our support team for further assistance."

# Title and description
st.title("Chatbot")
st.write("Welcome! I'm here to help answer your questions about AI.")

# Text input for user questions
user_question = st.text_input("Ask a question")

# Chatbot response
if st.button("Ask"):
    if user_question:
        chatbot_response = get_chatbot_response(user_question)
        st.text_area("Chatbot Response", value=chatbot_response, height=200, max_chars=None)
    else:
        st.warning("Please enter a question.")


st.header('Benchmarking')

# UK benchmarks for AI/ML adoption
uk_benchmarks = {
    "Readiness Score": 8,
    "Data Quality": 7,
    "Technical Infrastructure": 6,
    "Talent and Skills": 8,
    # Add more benchmarks as needed
}

# Title and description
st.title("AI Adoption Benchmarking")
st.write("Compare your AI adoption progress against industry benchmarks in the UK.")

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



import csv

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











# Define your CSS code as a string
custom_css = """
<style>
    /* Add your CSS styles here */
    body {
        background-color: #3366cc;
        background-image: url('https://example.com/ai-background-image.jpg'); /* Replace with your AI background image URL */
        background-repeat: no-repeat;
        background-size: cover;
        font-family: Arial, sans-serif;
    }
    
    h1 {
        color: #ffffff;
        font-size: 24px;
    }
    
    .question {
        color: #ffffff;
        font-size: 18px;
        margin-bottom: 10px;
    }
    
    .options {
        display: flex;
        flex-direction: column;
    }
    
    .option {
        margin-bottom: 5px;
    }
    
    .recommendation {
        color: #ffffff;
        font-size: 16px;
        font-style: italic;
        margin-top: 10px;
    }
    
    .button {
        margin-top: 20px;
    }
</style>
"""

# Render the CSS code using the `st.markdown` function
st.markdown(custom_css, unsafe_allow_html=True)








