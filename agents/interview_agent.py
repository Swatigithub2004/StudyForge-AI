def generate_questions(goal):

    questions = {

        "AI Engineer":[
            "What is Machine Learning?",
            "Difference between AI and ML?",
            "Explain overfitting."
        ],

        "Web Developer":[
            "What is HTML?",
            "Difference between GET and POST?",
            "Explain REST API."
        ],

        "ML Engineer":[
            "What is supervised learning?",
            "What is feature engineering?",
            "Explain model evaluation."
        ],

        "GSSoC Contributor":[
            "What is Git?",
            "What is a pull request?",
            "How do branches work?"
        ],

        "Internship Preparation":[
            "Tell me about yourself.",
            "What are your strengths?",
            "Why should we hire you?"
        ]
    }

    return questions.get(goal, [])