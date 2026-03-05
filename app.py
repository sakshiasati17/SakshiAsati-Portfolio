import streamlit as st
from streamlit_option_menu import option_menu
import base64
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
from streamlit_pdf_viewer import pdf_viewer

# Page Configuration
st.set_page_config(
    page_title="Sakshi Asati | Data Scientist",
    page_icon="💫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Professional & Sophisticated
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        padding-top: 0;
    }
    
    .stApp {
        background: #0a0e27;
    }
    
    .stApp > header {
        background: transparent;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hero Section */
    .hero-wrapper {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        padding: 6rem 3rem;
        border-radius: 0 0 40px 40px;
        position: relative;
        overflow: hidden;
    }
    
    .hero-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: radial-gradient(circle at 30% 50%, rgba(99, 102, 241, 0.2) 0%, transparent 50%);
    }
    
    .profile-frame {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        border: 4px solid #6366f1;
        padding: 5px;
        background: linear-gradient(135deg, #6366f1, #8b5cf6, #ec4899);
        margin: 0 auto 2rem;
        animation: gradientRotate 8s ease infinite;
        box-shadow: 0 20px 60px rgba(99, 102, 241, 0.4);
    }
    
    @keyframes gradientRotate {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .profile-frame img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
    }
    
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 1rem 0;
        letter-spacing: -1px;
    }
    
    .hero-subtitle {
        font-size: 1.8rem;
        font-weight: 600;
        color: #6366f1;
        margin-bottom: 1rem;
    }
    
    .hero-description {
        font-size: 1.2rem;
        color: #94a3b8;
        max-width: 800px;
        margin: 0 auto 2rem;
        line-height: 1.8;
    }
    
    /* Button Styles */
    .action-buttons {
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    
    .btn-custom {
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .btn-primary-custom {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
    }
    
    .btn-primary-custom:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(99, 102, 241, 0.6);
    }
    
    .btn-secondary-custom {
        background: transparent;
        color: #6366f1;
        border: 2px solid #6366f1;
    }
    
    .btn-secondary-custom:hover {
        background: #6366f1;
        color: white;
        transform: translateY(-3px);
    }
    
    /* Social Links */
    .social-links {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin-top: 2rem;
        padding-top: 2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .social-link {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: #cbd5e1;
        text-decoration: none;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .social-link:hover {
        color: #6366f1;
        transform: translateY(-2px);
    }
    
    /* Section Containers */
    .section-wrapper {
        background: white;
        margin: 3rem 0;
        padding: 4rem 3rem;
        border-radius: 30px;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
    }
    
    .section-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 3rem;
        text-align: center;
    }
    
    /* Stats Grid */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-10px);
        border-color: #6366f1;
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.2);
    }
    
    .stat-number {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1rem;
        color: #64748b;
        font-weight: 600;
    }
    
    /* Skills Grid */
    .skills-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .skill-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        padding: 2.5rem;
        border-radius: 20px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .skill-card:hover {
        transform: translateY(-8px);
        border-color: #6366f1;
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.15);
    }
    
    .skill-card-header {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .skill-icon {
        font-size: 3rem;
        width: 70px;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 15px;
    }
    
    .skill-card-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1e293b;
    }
    
    .skill-card-desc {
        color: #64748b;
        margin-bottom: 1.5rem;
    }
    
    .skills-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
        gap: 0.75rem;
    }
    
    .skill-badge {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        color: white;
        padding: 0.75rem 1rem;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(99, 102, 241, 0.2);
    }
    
    .skill-badge:hover {
        transform: scale(1.05) translateY(-2px);
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.4);
    }
    
    /* Project Cards */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .project-card {
        background: white;
        padding: 0;
        border-radius: 20px;
        overflow: hidden;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    }
    
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 50px rgba(99, 102, 241, 0.2);
        border-color: #6366f1;
    }
    
    .project-header {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        padding: 2rem;
        color: white;
    }
    
    .project-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .project-badges {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
    }
    
    .project-badge {
        background: rgba(255, 255, 255, 0.2);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
    }
    
    .project-body {
        padding: 2rem;
    }
    
    .project-description {
        color: #64748b;
        line-height: 1.8;
        margin-bottom: 1.5rem;
    }
    
    .project-highlight {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #e2e8f0;
    }
    
    .highlight-label {
        font-size: 0.9rem;
        color: #64748b;
        font-weight: 600;
    }
    
    .highlight-value {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Experience Timeline */
    .timeline {
        position: relative;
        padding: 2rem 0;
    }
    
    .timeline-item {
        background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 2px solid #e2e8f0;
        position: relative;
        transition: all 0.3s ease;
    }
    
    .timeline-item:hover {
        transform: translateX(10px);
        border-color: #6366f1;
        box-shadow: 0 15px 40px rgba(99, 102, 241, 0.15);
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -20px;
        top: 2.5rem;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border: 4px solid white;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
    }
    
    .job-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .job-company {
        font-size: 1.2rem;
        font-weight: 600;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .job-period {
        color: #64748b;
        margin: 1rem 0;
    }
    
    .job-responsibilities {
        list-style: none;
        padding: 0;
    }
    
    .job-responsibilities li {
        padding: 0.75rem 0;
        padding-left: 1.5rem;
        position: relative;
        color: #475569;
        line-height: 1.8;
    }
    
    .job-responsibilities li::before {
        content: '▸';
        position: absolute;
        left: 0;
        color: #6366f1;
        font-weight: bold;
    }
    
    /* Contact Cards */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .contact-card {
        background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
        padding: 2.5rem;
        border-radius: 20px;
        text-align: center;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .contact-card:hover {
        transform: translateY(-10px);
        border-color: #6366f1;
        box-shadow: 0 20px 40px rgba(99, 102, 241, 0.15);
    }
    
    .contact-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .contact-label {
        font-size: 0.9rem;
        color: #64748b;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .contact-value {
        font-size: 1.1rem;
        color: #1e293b;
        font-weight: 600;
        text-decoration: none;
    }
    
    .contact-value:hover {
        color: #6366f1;
    }
    
    /* Streamlit button overrides */
    .stButton > button {
        all: unset;
    }
    
    .stDownloadButton > button {
        all: unset;
    }
    
    /* Scroll to Top Button */
    .scroll-top {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        z-index: 1000;
        opacity: 0;
        visibility: hidden;
    }
    
    .scroll-top.visible {
        opacity: 1;
        visibility: visible;
    }
    
    .scroll-top:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.6);
    }
    
    /* Background Particles */
    .particles {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: none;
        z-index: 1;
    }
    
    .particle {
        position: absolute;
        width: 4px;
        height: 4px;
        background: rgba(99, 102, 241, 0.5);
        border-radius: 50%;
        animation: float 15s infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0) translateX(0); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100vh) translateX(50px); opacity: 0; }
    }
    
    /* Skill Progress Bars */
    .progress-container {
        margin: 1rem 0;
    }
    
    .progress-label {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.5rem;
        font-weight: 600;
        color: #1e293b;
    }
    
    .progress-bar-wrapper {
        background: #e2e8f0;
        border-radius: 10px;
        height: 12px;
        overflow: hidden;
    }
    
    .progress-bar {
        height: 100%;
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 10px;
        transition: width 1.5s ease;
        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
    }
    
    /* Accessibility */
    *:focus {
        outline: 2px solid #6366f1;
        outline-offset: 2px;
    }
    
    /* Print-friendly styles */
    @media print {
        .hero-wrapper { page-break-after: always; }
        .section-wrapper { page-break-inside: avoid; }
        .stApp { background: white !important; }
        .scroll-top { display: none !important; }
    }
    
    /* Loading skeleton */
    @keyframes skeleton-loading {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }
    
    .skeleton {
        background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
        background-size: 200% 100%;
        animation: skeleton-loading 1.5s ease infinite;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<meta name="description" content="Sakshi Asati - Data Scientist & Machine Learning Engineer. Transforming data into insights through cutting-edge AI and analytics solutions.">
<meta name="keywords" content="Data Scientist, Machine Learning, AI, Python, Analytics, Data Engineering">
<meta property="og:title" content="Sakshi Asati | Data Scientist & ML Engineer">
<meta property="og:description" content="Portfolio showcasing skills in Data Science, Machine Learning, and Data Engineering">
<meta property="og:type" content="website">
""", unsafe_allow_html=True)

st.markdown("""
<script>
// Scroll to top functionality
window.addEventListener('scroll', function() {
    const scrollTop = document.querySelector('.scroll-top');
    if (window.pageYOffset > 300) {
        scrollTop.classList.add('visible');
    } else {
        scrollTop.classList.remove('visible');
    }
});

document.querySelector('.scroll-top')?.addEventListener('click', function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});
</script>
""", unsafe_allow_html=True)

def load_resume():
    """Load resume PDF if it exists"""
    resume_path = Path("resume.pdf")
    if resume_path.exists():
        with open(resume_path, "rb") as pdf_file:
            return pdf_file.read()
    return None

def render_hero_section():
    """Render professional hero section"""
    st.markdown("""
    <div class="hero-wrapper">
    """, unsafe_allow_html=True)
    
    # Profile Picture
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        profile_pic_path = Path("profile_picture.jpeg")
        if profile_pic_path.exists():
            st.markdown("""
            <div class="profile-frame">
                <img src="data:image/jpeg;base64,{}" />
            </div>
            """.format(base64.b64encode(profile_pic_path.read_bytes()).decode()), unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center;">
                <div class="profile-frame">
                    <div style="width: 100%; height: 100%; border-radius: 50%; background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%); 
                                display: flex; align-items: center; justify-content: center; font-size: 5rem; color: white;">SA</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Title and Description
    st.markdown("""
    <div style="text-align: center;">
        <h1 class="hero-title">Sakshi Asati</h1>
        <div class="hero-subtitle">Data Scientist & Machine Learning Engineer</div>
        <div class="hero-description">
            Transforming complex data into strategic insights through cutting-edge analytics, 
            AI, and machine learning solutions that drive real business value.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Action Buttons
    col1, col2, col3 = st.columns([2, 2, 2])
    with col2:
        if st.button("📊 Explore My Work", use_container_width=True, key="btn_work"):
            st.session_state.nav_to = "Projects"
    
    # Resume Download
    resume_data = load_resume()
    if resume_data:
        col1, col2, col3 = st.columns([2, 2, 2])
        with col2:
            st.download_button(
                label="📄 Download Resume",
                data=resume_data,
                file_name="Sakshi_Asati_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    
    # Social Links
    st.markdown("""
    <div class="social-links">
        <a href="https://linkedin.com/in/sakshiasati" target="_blank" class="social-link">
            🔗 LinkedIn
        </a>
        <a href="https://github.com/sakshiasati17" target="_blank" class="social-link">
            💻 GitHub
        </a>
        <a href="mailto:sakshiasati51@gmail.com" class="social-link">
            ✉️ Email
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_about_section():
    """Render About section"""
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div style="font-size: 1.2rem; line-height: 1.9; color: #475569; margin-bottom: 2rem;">
            <p style="margin-bottom: 1.5rem;">
                I'm a passionate Data Scientist currently pursuing my Master's in Data Science at the University of Colorado Boulder. 
                With expertise spanning from building secure ETL pipelines to developing state-of-the-art AI models, I bridge the gap 
                between complex datasets and actionable business insights.
            </p>
            <p>
                My work is driven by a commitment to excellence and a belief that data holds the key to solving tomorrow's challenges. 
                I specialize in transforming raw information into strategic advantages through advanced analytics, machine learning, and AI solutions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Education
        st.markdown("### 🎓 Education")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); padding: 2rem; border-radius: 15px; margin-bottom: 1.5rem; border: 2px solid #e2e8f0;">
            <h4 style="color: #6366f1; font-size: 1.3rem; margin-bottom: 0.5rem; font-weight: 700;">M.S. in Data Science</h4>
            <p style="font-weight: 600; margin-bottom: 0.25rem; color: #1e293b;">University of Colorado Boulder, CO</p>
            <p style="color: #64748b; font-size: 0.95rem;">Aug 2024 – May 2026 (Expected)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); padding: 2rem; border-radius: 15px; border: 2px solid #e2e8f0;">
            <h4 style="color: #6366f1; font-size: 1.3rem; margin-bottom: 0.5rem; font-weight: 700;">B.E. in Information Technology</h4>
            <p style="font-weight: 600; margin-bottom: 0.25rem; color: #1e293b;">G. H. Raisoni College of Engineering, Nagpur, India</p>
            <p style="color: #64748b; font-size: 0.95rem;">Aug 2018 – May 2022</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stats-container">
        """, unsafe_allow_html=True)
        
        stats = [
            {"value": "2.5+", "label": "Years Experience"},
            {"value": "10+", "label": "Projects"},
            {"value": "97%", "label": "Best Accuracy"}
        ]
        
        for stat in stats:
            st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{stat['value']}</div>
                <div class="stat-label">{stat['label']}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_skills_section():
    """Render Skills section with professional cards and proficiency bars"""
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Technical Expertise</h2>', unsafe_allow_html=True)
    
    # Add skill proficiency data
    proficiency_data = {
        "Python": 95, "R": 85, "SQL": 90, "JavaScript": 80,
        "TensorFlow": 88, "PyTorch": 85, "Scikit-Learn": 92,
        "AWS": 85, "GCP": 80, "Azure": 75, "Docker": 88,
        "React": 82, "Node.js": 80, "MongoDB": 85
    }
    
    # Show proficiency chart
    st.markdown("### 📊 Skill Proficiency Overview")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Create a radar/polar chart for skill categories
        categories = ['Programming', 'ML/AI', 'Data Eng', 'Cloud', 'Tools']
        proficiency_scores = [90, 88, 85, 80, 85]
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=proficiency_scores,
            theta=categories,
            fill='toself',
            name='Proficiency',
            line=dict(color='#6366f1')
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=False,
            height=300,
            margin=dict(l=50, r=50, t=50, b=50)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Top skills progress bars
        st.markdown("**Top Skills**")
        top_skills = sorted(proficiency_data.items(), key=lambda x: x[1], reverse=True)[:5]
        for skill, proficiency in top_skills:
            st.markdown(f"""
            <div class="progress-container">
                <div class="progress-label">
                    <span>{skill}</span>
                    <span>{proficiency}%</span>
                </div>
                <div class="progress-bar-wrapper">
                    <div class="progress-bar" style="width: {proficiency}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    skills_data = {
        "Programming & Frameworks": {
            "icon": "⚡",
            "desc": "Building scalable applications and APIs",
            "skills": ["Python", "R", "SQL", "JavaScript", "HTML/CSS", "React", "Node.js", "FastAPI", "Supabase"],
            "gradient": "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)"
        },
        "Machine Learning & AI": {
            "icon": "🤖",
            "desc": "Creating intelligent models and predictions",
            "skills": ["Scikit-Learn", "XGBoost", "TensorFlow", "Keras", "PyTorch", "Pandas", "NumPy", "OpenCV", "Matplotlib", "Seaborn"],
            "gradient": "linear-gradient(135deg, #f59e0b 0%, #ef4444 100%)"
        },
        "Data Engineering & Big Data": {
            "icon": "📊",
            "desc": "Processing and managing large-scale data",
            "skills": ["Hadoop", "PySpark", "Airflow", "MongoDB", "PostgreSQL", "MySQL", "Linux/Unix"],
            "gradient": "linear-gradient(135deg, #10b981 0%, #059669 100%)"
        },
        "Cloud & DevOps": {
            "icon": "☁️",
            "desc": "Deploying and managing infrastructure",
            "skills": ["AWS", "GCP", "Azure", "Docker", "Git", "Jenkins", "Tableau", "Power BI", "Looker", "Excel"],
            "gradient": "linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)"
        }
    }
    
    st.markdown("---")
    st.markdown("### 🛠️ All Skills")
    st.markdown("""<div class="skills-container">""", unsafe_allow_html=True)
    
    for category, data in skills_data.items():
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-card-header">
                <div class="skill-icon" style="background: {data['gradient']};">
                    <span style="font-size: 2rem;">{data['icon']}</span>
                </div>
                <div>
                    <div class="skill-card-title">{category}</div>
                    <div class="skill-card-desc">{data['desc']}</div>
                </div>
            </div>
            <div class="skills-grid">
        """, unsafe_allow_html=True)
        
        for skill in data['skills']:
            proficiency = proficiency_data.get(skill, 75)
            st.markdown(f"""
            <div class="skill-badge" title="{skill}: {proficiency}%">{skill}</div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

def render_experience_section():
    """Render Experience section"""
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Professional Experience</h2>', unsafe_allow_html=True)
    
    st.markdown('<div class="timeline">', unsafe_allow_html=True)
    
    # Recess App Intern
    st.markdown("""
    <div class="timeline-item">
        <div class="job-title">Intern</div>
        <div class="job-company">The Recess App</div>
        <div style="color: #64748b; margin: 0.5rem 0;">Denver, CO • Jun 2024 – Aug 2024</div>
        <ul class="job-responsibilities">
            <li>Redesigned the backend data layer by migrating MySQL tables into a PostgreSQL schema on Supabase, enabling faster queries and seamless scaling for new features</li>
            <li>Automated user retention and onboarding by wiring Supabase triggers to Customer.io workflows, replacing manual outreach with real-time, event-based messaging</li>
            <li>Eliminated high-latency AWS Lambda calls by moving services to Supabase Edge Functions (Deno), reducing response times and simplifying infrastructure maintenance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Cognizant Programmer Analyst
    st.markdown("""
    <div class="timeline-item">
        <div class="job-title">Programmer Analyst</div>
        <div class="job-company">Cognizant Technology Solutions</div>
        <div style="color: #64748b; margin: 0.5rem 0;">Pune, Maharashtra, India • Jun 2023 – May 2024</div>
        <ul class="job-responsibilities">
            <li>Built and maintained secure ETL pipelines to process millions of customer and transaction records into Hadoop, keeping all data flows fully GDPR-compliant</li>
            <li>Replaced legacy schedulers with automated workflows in Apache Airflow, adding retry logic and SLA monitoring, which <strong>cut pipeline downtime by 30%</strong> in six months</li>
            <li>Troubleshot and fixed Spark job failures through log analysis and better exception handling, <strong>boosting reliability and throughput by 40%</strong></li>
            <li>Wrote Python and SQL scripts to monitor pipelines proactively, <strong>reducing incident response time by 25%</strong> and giving analytics teams clearer visibility into data health</li>
            <li>Set up CI/CD pipelines with Jenkins and Bitbucket to streamline deployments, adding pre-validation and alerts that <strong>prevented 90% of production issues</strong></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Cognizant Programmer Analyst Trainee
    st.markdown("""
    <div class="timeline-item">
        <div class="job-title">Programmer Analyst (Trainee)</div>
        <div class="job-company">Cognizant Technology Solutions</div>
        <div style="color: #64748b; margin: 0.5rem 0;">Pune, Maharashtra, India • Jun 2022 – May 2023</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Cognizant Intern
    st.markdown("""
    <div class="timeline-item">
        <div class="job-title">Intern</div>
        <div class="job-company">Cognizant Technology Solutions</div>
        <div style="color: #64748b; margin: 0.5rem 0;">Pune, Maharashtra, India • Jan 2022 – May 2022</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_projects_section():
    """Render Projects section"""
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)
    
    projects = [
        {
            "title": "SCANET – AI Disease Classifier",
            "badges": ["TensorFlow", "DenseNet121", "CNN"],
            "description": "Fine-tuned DenseNet121 on NIH chest X-rays (112K images), achieving <strong>91.7% accuracy</strong> across 14 disease classes. Deployed Flask + React webapp on Firebase with MapBox API integration.",
            "highlight": {"label": "Accuracy", "value": "91.7%"}
        },
        {
            "title": "NexChain – Supply Chain Optimization",
            "badges": ["Python", "XGBoost", "Clustering"],
            "description": "Compared ML models achieving <strong>97% accuracy</strong>. Applied clustering to optimize inventory, cutting overstock risk by <strong>20%</strong>. Analyzed multiple algorithms including Logistic Regression, Naïve Bayes, and Decision Trees.",
            "highlight": {"label": "Accuracy", "value": "97%"}
        },
        {
            "title": "Support Sync – CRM Ticketing System",
            "badges": ["MongoDB", "Node.js", "React", "AI"],
            "description": "Built a real-time CRM platform with MongoDB Change Streams. Integrated AI chatbot for FAQs and password resets, <strong>reducing agent workload by 30%</strong>.",
            "highlight": {"label": "Efficiency", "value": "30%"}
        },
        {
            "title": "Food Allergy Risk Analysis",
            "badges": ["Python", "Statistical Analysis", "ANOVA"],
            "description": "Analyzed 400+ food items to identify nutrient differences and high-risk ingredients. Applied Logistic Regression, ANOVA, and T-tests for comprehensive statistical analysis.",
            "highlight": {"label": "Dataset", "value": "400+"}
        }
    ]
    
    st.markdown("""<div class="projects-grid">""", unsafe_allow_html=True)
    
    for project in projects:
        badges_html = " ".join([f'<span class="project-badge">{badge}</span>' for badge in project["badges"]])
        
        st.markdown(f"""
        <div class="project-card">
            <div class="project-header">
                <div class="project-title">{project['title']}</div>
                <div class="project-badges">{badges_html}</div>
            </div>
            <div class="project-body">
                <div class="project-description">{project['description']}</div>
                <div class="project-highlight">
                    <div class="highlight-label">{project['highlight']['label']}</div>
                    <div class="highlight-value">{project['highlight']['value']}</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div></div>", unsafe_allow_html=True)

def render_resume_section():
    """Render Resume section with PDF viewer"""
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Resume</h2>', unsafe_allow_html=True)
    
    resume_data = load_resume()
    if resume_data:
        st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #64748b; margin-bottom: 2rem;">View or download my professional resume</p>', unsafe_allow_html=True)
        
        # PDF Viewer
        with st.expander("📄 View Resume", expanded=True):
            pdf_viewer(resume_data, width=700)
        
        # Download button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📥 Download Resume PDF",
                data=resume_data,
                file_name="Sakshi_Asati_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning("📄 Resume PDF not found. Please add your resume as 'resume.pdf' in the portfolio folder.")
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_contact_section():
    """Render Contact section"""
    st.markdown('<div class="section-wrapper">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Let\'s Connect</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #64748b; margin-bottom: 3rem;">I\'m always open to discussing new opportunities and exciting projects</p>', unsafe_allow_html=True)
    
    st.markdown("""<div class="contact-grid">""", unsafe_allow_html=True)
    
    contact_info = [
        {"icon": "📍", "label": "Location", "value": "Boulder, CO"},
        {"icon": "📧", "label": "Email", "value": "sakshiasati51@gmail.com", "link": "mailto:sakshiasati51@gmail.com"},
        {"icon": "📱", "label": "Phone", "value": "303-356-2393", "link": "tel:303-356-2393"},
        {"icon": "💼", "label": "LinkedIn", "value": "sakshiasati", "link": "https://linkedin.com/in/sakshiasati"},
        {"icon": "💻", "label": "GitHub", "value": "sakshiasati17", "link": "https://github.com/sakshiasati17"}
    ]
    
    for contact in contact_info:
        link_start = f'<a href="{contact["link"]}" target="_blank" class="contact-value">' if "link" in contact else ''
        link_end = '</a>' if "link" in contact else ''
        value = f'<span class="contact-value">{contact["value"]}</span>' if "link" not in contact else f'{link_start}{contact["value"]}{link_end}'
        
        st.markdown(f"""
        <div class="contact-card">
            <div class="contact-icon">{contact['icon']}</div>
            <div class="contact-label">{contact['label']}</div>
            {value}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Contact Form
    st.markdown("---")
    st.markdown("### 💬 Send Me a Message")
    
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name", placeholder="Your name")
        with col2:
            email = st.text_input("Email", placeholder="your.email@example.com")
        
        subject = st.text_input("Subject", placeholder="Project inquiry, collaboration, etc.")
        message = st.text_area("Message", placeholder="Tell me about your project or opportunity...", height=150)
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you! I'll get back to you soon.")
                st.info("💡 For immediate contact, please email: sakshiasati51@gmail.com")
            else:
                st.warning("⚠️ Please fill in all required fields.")
    
    # Resume download in contact
    resume_data = load_resume()
    if resume_data:
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.download_button(
                label="📄 Download My Resume",
                data=resume_data,
                file_name="Sakshi_Asati_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state
if 'nav_to' not in st.session_state:
    st.session_state.nav_to = None

# Main App
def main():
    # Navigation Menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Skills", "Experience", "Projects", "Resume", "Contact"],
        icons=["house", "person", "code-slash", "briefcase", "folder", "file-text", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#6366f1", "font-size": "20px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "center",
                "margin": "0px",
                "color": "#cbd5e1",
                "--hover-color": "#6366f1",
            },
            "nav-link-selected": {"background": "linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)", "color": "white"},
        }
    )
    
    # Handle navigation from buttons
    if st.session_state.nav_to:
        if st.session_state.nav_to == "Projects":
            selected = "Projects"
        st.session_state.nav_to = None
    
    # Route to selected page
    if selected == "Home":
        render_hero_section()
    elif selected == "About":
        render_about_section()
    elif selected == "Skills":
        render_skills_section()
    elif selected == "Experience":
        render_experience_section()
    elif selected == "Projects":
        render_projects_section()
    elif selected == "Resume":
        render_resume_section()
    elif selected == "Contact":
        render_contact_section()
    
    # Add scroll to top button
    st.markdown("""
    <div class="scroll-top">
        ↑
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()