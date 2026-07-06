def suggest_projects(goal):

    projects = {

        "AI Engineer":[
            "Resume Screening AI",
            "Chatbot using LLM",
            "Face Emotion Detection"
        ],

        "Web Developer":[
            "Portfolio Website",
            "E-commerce Website",
            "Blog Platform"
        ],

        "ML Engineer":[
            "House Price Prediction",
            "Movie Recommendation System",
            "Spam Detection"
        ],

        "GSSoC Contributor":[
            "GitHub Issue Finder",
            "Contribution Tracker",
            "Open Source Dashboard"
        ],

        "Internship Preparation":[
            "Resume Analyzer",
            "Interview Preparation App",
            "Student Planner"
        ]
    }

    return projects.get(goal, [])