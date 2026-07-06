def generate_roadmap(goal):

    roadmap = {

        "AI Engineer": [
            "Learn Python fundamentals",
            "Study Machine Learning basics",
            "Build ML mini projects"
        ],

        "Web Developer": [
            "Learn HTML/CSS",
            "Learn JavaScript",
            "Build full-stack projects"
        ],

        "ML Engineer": [
            "Learn ML algorithms",
            "Practice datasets",
            "Deploy ML projects"
        ],

        "GSSoC Contributor": [
            "Learn Git and GitHub",
            "Practice open-source contributions",
            "Contribute to repositories"
        ],

        "Internship Preparation": [
            "Practice DSA",
            "Build projects",
            "Prepare interview questions"
        ]
    }

    return roadmap.get(goal, [])