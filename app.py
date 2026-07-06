import streamlit as st
from utils.pdf_reader import extract_text
from agents.roadmap_agent import generate_roadmap
from agents.interview_agent import generate_questions
from agents.project_agent import suggest_projects
from agents.ai_profile_agent import analyze_resume_ai
from agents.opportunity_agent import suggest_opportunities


# ---------------- PAGE ----------------

st.set_page_config(
    page_title="StudyForge AI",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp{
background:
linear-gradient(
rgba(5,10,25,.92),
rgba(5,10,25,.92)
),
url("https://images.unsplash.com/photo-1522202176988-66273c2fd55?q=80&w=1600");

background-size:cover;
background-position:center;
background-attachment:fixed;
}

section[data-testid="stSidebar"]{
background:#071028;
}

h1,h2,h3{
color:white !important;
}

/* CARD ANIMATION */

.card-hover{
background:rgba(255,255,255,.08);
padding:25px;
border-radius:20px;
border:1px solid rgba(255,255,255,.15);

height:180px;

display:flex;
flex-direction:column;
justify-content:center;
align-items:center;

overflow:hidden;

backdrop-filter:blur(20px);

box-shadow:0px 8px 25px rgba(0,0,0,.25);

transition:all .5s ease;
cursor:pointer;
}

.card-hover:hover{
transform:translateY(-12px) scale(1.05);

box-shadow:
0 0 20px rgba(236,72,153,.8),
0 0 40px rgba(124,58,237,.6),
0 20px 50px rgba(124,58,237,.55);

border:1px solid rgba(236,72,153,.7);
}

/* text fix */

.card-text{
word-wrap:break-word;
overflow-wrap:break-word;
white-space:normal;
line-height:1.4;
}

/* Button */

.stButton>button{
width:100%;
height:55px;
font-size:18px;
font-weight:bold;
border-radius:15px;
border:none;
background:linear-gradient(90deg,#3B82F6,#EC4899);
color:white;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HERO ----------------

st.markdown("""
<div style='
background:linear-gradient(135deg,#0F172A,#1E3A8A,#7C3AED);
padding:60px;
border-radius:30px;
margin-bottom:30px;
box-shadow:0px 0px 30px rgba(124,58,237,.35);
'>

<h1 style='color:white;font-size:60px;font-weight:900;'>
AI-Powered Student
<span style='color:#FF4FA3'>Success</span>
Platform 🚀
</h1>

<p style='color:#E2E8F0;font-size:20px;'>
Build roadmaps, analyze resumes,
prepare interviews and discover
career opportunities with AI.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

st.sidebar.header("Student Details")

name = st.sidebar.text_input("Enter your name")

goal = st.sidebar.selectbox(
    "Choose Goal",
    [
        "AI Engineer",
        "Web Developer",
        "ML Engineer",
        "GSSoC Contributor",
        "Internship Preparation"
    ]
)

resume = st.file_uploader("Upload Resume PDF", type=["pdf"])


# ---------------- BUTTON ----------------

if st.button("Generate Plan 🚀"):

    if resume:

        st.balloons()

        resume_text = extract_text(resume)

        with st.spinner("StudyForge AI analyzing..."):
            ai_analysis = analyze_resume_ai(resume_text)

        roadmap = generate_roadmap(goal)
        questions = generate_questions(goal)
        projects = suggest_projects(goal)
        opportunities = suggest_opportunities(goal)

        score = ai_analysis.get("score", 75)
        word_count = len(resume_text.split())

        tabs = st.tabs([
            "📊 Dashboard",
            "🤖 AI Analysis",
            "🚀 Roadmap",
            "🎤 Interview",
            "💼 Growth"
        ])

        # ---------------- Dashboard ----------------

        with tabs[0]:

            st.markdown("""
            <h1 style="color:white;font-size:40px;">
            📊 Student Dashboard
            </h1>
            """, unsafe_allow_html=True)

            c1, c2, c3, c4 = st.columns(4)

            cards = [
                ("👤 Student", name if name else "User"),
                ("📄 Resume Score", f"{score}/100"),
                ("📝 Words", word_count),
                ("🎯 Goal", goal)
            ]

            for col, (title, value) in zip([c1, c2, c3, c4], cards):
                with col:
                    st.markdown(f"""
                    <div class="card-hover">
                        <p style="color:#CBD5E1;font-size:18px;">
                            {title}
                        </p>
                        <h2 class="card-text" style="color:white;font-size:30px;">
                            {value}
                        </h2>
                    </div>
                    """, unsafe_allow_html=True)

            st.write("")

            left, right = st.columns([2, 1])

            with left:
                st.markdown("## 🎯 Next Action Plan")

                actions = [
                    "Improve missing skills",
                    "Build one project",
                    "Practice interviews",
                    "Apply for opportunities"
                ]

                for i, a in enumerate(actions, 1):
                    st.success(f"{i}. {a}")

            with right:
                st.markdown("## 🚀 Status")

                status = [
                    "Resume Uploaded ✅",
                    "AI Analysis Complete 🤖",
                    "Roadmap Ready 🎯"
                ]

                for s in status:
                    st.info(s)

        # ---------------- AI ANALYSIS ----------------

        with tabs[1]:

            st.markdown("## 🤖 AI Profile Analysis")

            st.markdown("### 📝 Summary")
            st.write(ai_analysis.get("summary", "No summary found"))

            st.markdown("### ✅ Strengths")
            for s in ai_analysis.get("strengths", []):
                st.success(s)

            st.markdown("### ⚠ Missing Skills")
            for m in ai_analysis.get("missing_skills", []):
                st.warning(m)

            st.markdown("### ❌ Weaknesses")
            for w in ai_analysis.get("weaknesses", []):
                st.error(w)

        # ---------------- ROADMAP ----------------

        with tabs[2]:
            st.markdown("## 🚀 Learning Roadmap")

            for i, step in enumerate(roadmap, start=1):
                st.info(f"Month {i}: {step}")

        # ---------------- INTERVIEW ----------------

        with tabs[3]:
            st.markdown("## 🎤 Interview Questions")

            for q in questions:
                st.success(q)

        # ---------------- GROWTH ----------------

        with tabs[4]:

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("## 💡 Projects")
                for p in projects:
                    st.info(p)

            with col2:
                st.markdown("## 💼 Opportunities")
                for o in opportunities:
                    st.success(o)

    else:
        st.warning("Please upload a resume")