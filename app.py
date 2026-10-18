import streamlit as st

# =====================================================
# EDUAI | SCI-TECH YOUTH EDITION
# =====================================================
st.set_page_config(
    page_title="EDUAI | Learn Beyond",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------ SESSION STATE --------------------
defaults = {
    "history": [],
    "quiz_score": 0,
    "quiz_done": False,
    "last_answers": [],
    "last_questions": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ------------------ VISUAL DESIGN --------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap');

:root {
    --blue: #4F46E5;
    --blue-dark: #3730A3;
    --purple: #8B5CF6;
    --cyan: #06B6D4;
    --ink: #172554;
    --muted: #64748B;
    --line: #E5E7F0;
    --surface: #FFFFFF;
    --page: #F7F8FC;
}

html, body, [class*="css"] {
    font-family: 'Be Vietnam Pro', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 88% 0%, rgba(167,139,250,.17), transparent 30%),
        radial-gradient(ellipse at 0% 18%, rgba(96,165,250,.13), transparent 28%),
        var(--page);
    color: var(--ink);
}

.block-container {
    max-width: 1280px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 {
    color: var(--ink);
    letter-spacing: -0.045em;
    font-weight: 800;
}

h1 { line-height: 1.18; }
p, label, .stMarkdown { line-height: 1.72; }

/* Sidebar: soft glass + clear navigation */
[data-testid="stSidebar"] {
    background: linear-gradient(165deg, #EEF2FF 0%, #F7F5FF 52%, #FFFFFF 100%);
    border-right: 1px solid #E0E7FF;
}
[data-testid="stSidebar"] > div { padding-top: 1.35rem; }
[data-testid="stSidebar"] h1 {
    color: #4F46E5;
    letter-spacing: -1.2px;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    border-radius: 12px;
    padding: .35rem .55rem;
    transition: background .18s ease, color .18s ease;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(99,102,241,.09);
}

/* Hero banner */
.hero {
    position: relative;
    overflow: hidden;
    padding: clamp(25px, 4vw, 42px);
    border-radius: 28px;
    color: #FFFFFF;
    background: linear-gradient(120deg, #1E40AF 0%, #4F46E5 52%, #9333EA 100%);
    
