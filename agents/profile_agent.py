def analyze_profile(resume_text):

    strengths = []
    missing_skills = []

    skill_keywords = [
        "Python",
        "Machine Learning",
        "SQL",
        "Power BI",
        "Data Structures",
        "Deep Learning",
        "Git",
        "TensorFlow",
        "React",
        "Docker"
    ]

    for skill in skill_keywords:

        if skill.lower() in resume_text.lower():

            strengths.append(skill)

        else:

            missing_skills.append(skill)

    result = {
        "strengths": strengths,
        "missing_skills": missing_skills
    }

    return result