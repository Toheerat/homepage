import streamlit as st


st.title("Adopting AI and Machine Learning for your Business")
st.markdown("""This tool provides guidance and resources to help your small and medium enterprise assess readiness and adopt AI/ML technologies. The purpose of AI and machine learning tools for SMEs is to leverage the power of these technologies to improve operational efficiency, enhance decision-making, provide personalized experiences, and gain a competitive advantage in their respective markets. Autonomous machine learning is the development of systems or algorithms that learn and improve from data without explicit programming or human intervention. These tools automate the machine learning process, including data preprocessing, feature selection, model training, and hyperparameter tuning. They utilize techniques like automated machine learning (AutoML), reinforcement learning, and meta-learning to automate decision-making and optimize model performance. The goal is to minimize the time and effort needed to build accurate and reliable machine learning models.""")
st.button("Get Started")

# Import libraries
# Create list of questions and answers
questions = [
    {
        "question": "1. Does your organization have a clear understanding of AI and machine learning?",
        "answer": "Yes"
    },
    {
        "question": "2. Has your organization identified potential use cases for AI and machine learning?",
        "answer": "Yes"
    },
    {
        "question": "3. Does your organization have access to relevant data for implementing AI and machine learning?",
        "answer": "Yes"
    },
    {
        "question": "4. Has your organization allocated sufficient resources (financial, technical, human) for AI and machine learning initiatives?",
        "answer": "Yes"
    },
    {
        "question": "5. Has your organization developed a roadmap or strategy for AI and machine learning adoption?",
        "answer": "Yes"
    }
    # Add more questions as needed
]

# Create function to score quiz responses
def score_quiz_responses(responses):
    score = 0
    for i, response in enumerate(responses):
        if response == questions[i]["answer"]:
            score += 1
    return score





# Display questions and response form
st.header("AI and Machine Learning Readiness Quiz")

responses = []
for i, question in enumerate(questions):
    st.subheader(question["question"])
    response = st.radio(f"Select your response for question {i+1}:", ("Yes", "No", "Not Sure"), key=f"question_{i}")
    responses.append(response)

# Submit button
submitted = st.button("Submit")

# Assess readiness, display score and recommendations
if submitted:
    readiness_score = score_quiz_responses(responses)
    st.write("Readiness Score:", readiness_score)
    
    if readiness_score == len(questions):
        st.success("Congratulations! Your organization is ready for AI and machine learning adoption.")
    else:
        st.warning("There are areas for improvement in your organization's readiness for AI and machine learning adoption. Consider addressing the identified gaps.")




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
    "Can machines become more intelligent than humans?": "The concept of machines surpassing human intelligence, known as artificial general intelligence (AGI), is still hypothetical. While AI systems can excel in specific tasks, replicating the complexity and breadth of human intelligence remains a significant challenge."

    # Add more FAQ questions and answers as needed
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

