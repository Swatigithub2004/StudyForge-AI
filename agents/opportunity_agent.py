def suggest_opportunities(goal):

    opportunities = {

        "AI Engineer":[
            "Kaggle Competitions",
            "Google AI projects",
            "AI internships"
        ],

        "Web Developer":[
            "Frontend internships",
            "Open source projects",
            "Hackathons"
        ],

        "ML Engineer":[
            "Machine Learning internships",
            "Data science competitions",
            "Research projects"
        ],

        "GSSoC Contributor":[
            "GSSoC",
            "GitHub open source repositories",
            "Hacktoberfest"
        ],

        "Internship Preparation":[
            "LinkedIn internships",
            "Campus opportunities",
            "Coding contests"
        ]
    }

    return opportunities.get(goal, [])