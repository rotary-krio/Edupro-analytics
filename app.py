import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="EduPro Learner Analytics",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS — BRIGHT, GLOWING, HOVER-RICH
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #0f172a, #1e1b4b, #312e81, #0f172a);
        background-size: 400% 400%;
        animation: gradientShift 18s ease infinite;
    }
    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Main Container */
    .main .block-container {
        background: rgba(30, 27, 75, 0.75);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(139, 92, 246, 0.55);
        border-radius: 22px;
        padding: 1.8rem 2.2rem;
        margin-top: 1rem;
        box-shadow:
            0 0 40px rgba(139, 92, 246, 0.25),
            inset 0 0 60px rgba(99, 102, 241, 0.06);
        transition: box-shadow 0.5s ease;
    }
    .main .block-container:hover {
        box-shadow:
            0 0 60px rgba(168, 85, 247, 0.45),
            inset 0 0 80px rgba(99, 102, 241, 0.1);
    }

    /* Neon Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
        font-weight: 900 !important;
        letter-spacing: 0.5px;
    }
    h1 {
        text-align: center;
        background: linear-gradient(90deg, #22d3ee, #a78bfa, #f472b6, #facc15);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradientText 6s ease infinite;
        filter: drop-shadow(0 0 18px rgba(167, 139, 250, 0.65));
        font-size: 2.6rem !important;
    }
    @keyframes gradientText {
        0%,100% { background-position: 0% 50%; }
        50%     { background-position: 100% 50%; }
    }
    h2 {
        border-bottom: 3px solid #8b5cf6;
        padding-bottom: 8px;
        font-size: 1.6rem;
        text-shadow: 0 0 15px rgba(167, 139, 250, 0.6);
    }
    h3 {
        font-size: 1.2rem;
        color: #67e8f9 !important;
        text-shadow: 0 0 10px rgba(34, 211, 238, 0.5);
    }

    /* Text */
    p, span, label {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
    }
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #93c5fd !important;
        font-weight: 600 !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1e1b4b 100%);
        border-right: 2px solid rgba(139, 92, 246, 0.4);
        box-shadow: 4px 0 30px rgba(139, 92, 246, 0.25);
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    [data-testid="stSidebar"] hr {
        border-color: rgba(139, 92, 246, 0.4);
    }

    /* Glowing Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 50%, #ec4899 100%);
        background-size: 200% 200%;
        color: white !important;
        border: none;
        border-radius: 14px;
        padding: 11px 24px;
        font-weight: 800 !important;
        letter-spacing: 0.4px;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.5);
        width: 100%;
        animation: btnGradient 5s ease infinite;
    }
    @keyframes btnGradient {
        0%,100% { background-position: 0% 50%; }
        50%     { background-position: 100% 50%; }
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow:
            0 12px 35px rgba(236, 72, 153, 0.7),
            0 0 0 4px rgba(236, 72, 153, 0.15);
    }
    .stButton > button:active {
        transform: translateY(0) scale(0.98);
    }

    /* Neon Metric Cards */
    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #1e293b, #312e81);
        border: 2px solid rgba(139, 92, 246, 0.6);
        border-radius: 18px;
        padding: 16px;
        box-shadow:
            0 6px 22px rgba(79, 70, 229, 0.35),
            inset 0 0 25px rgba(99, 102, 241, 0.08);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    div[data-testid="stMetric"]:hover {
        transform: translateY(-6px) scale(1.03);
        border-color: #22d3ee;
        box-shadow:
            0 15px 40px rgba(34, 211, 238, 0.45),
            inset 0 0 35px rgba(34, 211, 238, 0.12);
    }
    div[data-testid="stMetricValue"] {
        background: linear-gradient(90deg, #22d3ee, #a78bfa, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 1.9rem;
        font-weight: 900 !important;
        filter: drop-shadow(0 0 8px rgba(167, 139, 250, 0.6));
    }
    div[data-testid="stMetricLabel"] {
        color: #e2e8f0 !important;
        font-weight: 700 !important;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: rgba(15, 23, 42, 0.8);
        padding: 10px;
        border-radius: 14px;
        border: 1px solid rgba(139, 92, 246, 0.4);
        box-shadow: inset 0 0 25px rgba(99, 102, 241, 0.12);
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 800 !important;
        color: #a5b4fc !important;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(139, 92, 246, 0.2);
        color: #22d3ee !important;
        transform: translateY(-2px);
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #06b6d4 0%, #8b5cf6 50%, #ec4899 100%) !important;
        color: #ffffff !important;
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.55);
    }

    /* Alerts */
    .stSuccess, div[data-testid="stAlert"] {
        border-radius: 14px;
        background: linear-gradient(135deg, #064e3b, #065f46) !important;
        color: #6ee7b7 !important;
        border: 1px solid #10b981;
        box-shadow: 0 0 22px rgba(16, 185, 129, 0.4);
        transition: transform 0.3s ease;
    }
    div[data-testid="stAlert"]:hover {
        transform: scale(1.01);
    }
    div[data-testid="stAlert"] p {
        color: #d1fae5 !important;
        font-weight: 700 !important;
    }

    /* Sidebar Cards */
    .sidebar-card {
        background: linear-gradient(145deg, #1e293b, #312e81);
        border: 1px solid rgba(139, 92, 246, 0.6);
        border-radius: 14px;
        padding: 13px;
        margin-bottom: 12px;
        font-size: 13px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
        transition: all 0.35s ease;
        position: relative;
        overflow: hidden;
    }
    .sidebar-card::after {
        content: "";
        position: absolute;
        top: 0; left: -100%;
        width: 100%; height: 100%;
        background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.25), transparent);
        transition: left 0.6s ease;
    }
    .sidebar-card:hover::after {
        left: 100%;
    }
    .sidebar-card:hover {
        transform: translateX(4px);
        border-color: #22d3ee;
        box-shadow: 0 6px 22px rgba(34, 211, 238, 0.4);
    }
    .sidebar-card b { color: #67e8f9 !important; }

    /* Charts hover lift */
    .js-plotly-plot, .plot-container {
        width: 100% !important;
        border-radius: 16px;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }
    .js-plotly-plot:hover {
        transform: scale(1.01);
        box-shadow: 0 0 40px rgba(139, 92, 246, 0.35);
    }

    /* Multiselect */
    div[data-baseweb="select"] > div {
        background-color: #1e293b !important;
        border: 1px solid rgba(139, 92, 246, 0.5) !important;
        border-radius: 10px !important;
        transition: all 0.3s ease;
    }
    div[data-baseweb="select"] > div:hover {
        border-color: #22d3ee !important;
        box-shadow: 0 0 16px rgba(34, 211, 238, 0.4);
    }
    span[data-baseweb="tag"] {
        background: linear-gradient(135deg, #06b6d4, #8b5cf6) !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"] {
        border-radius: 14px;
        overflow: hidden;
        border: 1px solid rgba(139, 92, 246, 0.4);
        transition: box-shadow 0.35s ease;
    }
    div[data-testid="stDataFrame"]:hover {
        box-shadow: 0 0 28px rgba(139, 92, 246, 0.35);
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 9px; height: 9px; }
    ::-webkit-scrollbar-track { background: #0f172a; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #6366f1, #ec4899);
        border-radius: 10px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #22d3ee, #f472b6);
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER
# ============================================
st.markdown("""
<div style='text-align:center; padding:10px;'>
    <h1>🎓 EduPro Learner Analytics Dashboard</h1>
    <p style='font-size:16px; color:#67e8f9; font-weight:700; letter-spacing:0.5px;'>
        ✨ Learner Demographics &amp; Course Enrollment Behavior Analysis ✨
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# AUTO DATA LOADER
# ============================================
REQUIRED_FILES = ["Users.csv", "Courses.csv", "Transactions.csv", "Teachers.csv"]

@st.cache_data(show_spinner=False)
def auto_find_data_folder():
    candidates = [
        Path("data"),
        Path("./data"),
        Path("../data"),
        Path.cwd() / "data",
        Path(__file__).parent / "data" if "__file__" in globals() else None,
    ]
    for p in candidates:
        if p and p.exists() and all((p / f).exists() for f in REQUIRED_FILES):
            return p.resolve()
    return None

@st.cache_data(show_spinner="📂 Loading EduPro data...")
def load_all_data(folder: str):
    folder = Path(folder)
    return (
        pd.read_csv(folder / "Users.csv"),
        pd.read_csv(folder / "Courses.csv"),
        pd.read_csv(folder / "Transactions.csv"),
        pd.read_csv(folder / "Teachers.csv"),
    )

@st.cache_data(show_spinner="🔗 Merging tables...")
def build_merged(users, courses, transactions):
    merged = transactions.merge(
        users[['UserID', 'UserName', 'Age', 'Gender']], on='UserID', how='left'
    )
    merged = merged.merge(
        courses[['CourseID', 'CourseName', 'CourseCategory',
                 'CourseType', 'CourseLevel', 'CoursePrice', 'CourseRating']],
        on='CourseID', how='left'
    )
    def age_group(age):
        if pd.isna(age): return 'Unknown'
        if age < 18:    return '<18'
        if age <= 25:   return '18-25'
        if age <= 35:   return '26-35'
        if age <= 45:   return '36-45'
        return '45+'
    merged['AgeGroup'] = merged['Age'].apply(age_group)
    return merged

# ============================================
# LOAD
# ============================================
data_folder = auto_find_data_folder()
if data_folder is None:
    st.error("🚫 **Data files not found.**")
    st.markdown(f"Place `Users.csv`, `Courses.csv`, `Transactions.csv`, `Teachers.csv` inside a `data` folder next to `app.py`.\n\n**CWD:** `{Path.cwd()}`")
    st.stop()

users, courses, transactions, teachers = load_all_data(str(data_folder))
merged_data = build_merged(users, courses, transactions)

AGE_ORDER = ['<18', '18-25', '26-35', '36-45', '45+']

# ============================================
# BRIGHT PALETTES
# ============================================
# For PIE / categorical discrete colors (a LIST is valid)
NEON_PALETTE = ['#22d3ee', '#a78bfa', '#f472b6', '#facc15',
                '#4ade80', '#fb923c', '#60a5fa', '#f87171',
                '#c084fc', '#34d399']

# For continuous color scales (must be a NAMED plotly scale OR list of [pos,color] pairs)
BRIGHT_CONTINUOUS = [
    [0.0,  '#0f172a'],
    [0.15, '#22d3ee'],
    [0.35, '#60a5fa'],
    [0.55, '#a78bfa'],
    [0.75, '#f472b6'],
    [0.9,  '#facc15'],
    [1.0,  '#fde047'],
]

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("## 🎓 EduPro Analytics")
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="sidebar-card">
        ✅ <b>Data loaded automatically</b><br>
        📁 <code>{data_folder.name}/</code>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 Dataset Snapshot")
    st.markdown(f"""
    <div class="sidebar-card">
        👥 Users: <b>{len(users):,}</b><br>
        📚 Courses: <b>{len(courses):,}</b><br>
        🛒 Enrollments: <b>{len(transactions):,}</b><br>
        👨‍🏫 Teachers: <b>{len(teachers):,}</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### 🎛️ Quick Filters")

    sel_age = st.multiselect("Age Group", options=AGE_ORDER, default=AGE_ORDER, key="sb_age")
    sel_gender = st.multiselect("Gender",
                                options=sorted(users['Gender'].dropna().unique()),
                                default=sorted(users['Gender'].dropna().unique()),
                                key="sb_gender")
    sel_cat = st.multiselect("Course Category",
                             options=sorted(courses['CourseCategory'].dropna().unique()),
                             default=sorted(courses['CourseCategory'].dropna().unique()),
                             key="sb_cat")
    sel_level = st.multiselect("Course Level",
                               options=sorted(courses['CourseLevel'].dropna().unique()),
                               default=sorted(courses['CourseLevel'].dropna().unique()),
                               key="sb_level")

    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("🔄 Refresh Data"):
        st.cache_data.clear()
        st.rerun()

    st.markdown("""
    <div class="sidebar-card" style="margin-top:12px;">
        <b>ℹ️ Tip:</b> Filters apply to every tab. Hover over cards & charts for glow effects!
    </div>
    """, unsafe_allow_html=True)

# ============================================
# FILTER
# ============================================
filtered = merged_data[
    merged_data['AgeGroup'].isin(sel_age) &
    merged_data['Gender'].isin(sel_gender) &
    merged_data['CourseCategory'].isin(sel_cat) &
    merged_data['CourseLevel'].isin(sel_level)
]

# ============================================
# STYLED CHART HELPER
# ============================================
DEFAULT_HEIGHT = 440

def styled_chart(fig, height=DEFAULT_HEIGHT):
    fig.update_layout(
        height=height,
        title=dict(font=dict(size=19, color='#ffffff', family='Outfit'), x=0.02, xanchor='left'),
        font=dict(color='#ffffff', size=13, family='Outfit'),
        legend=dict(
            font=dict(color='#ffffff', size=12, family='Outfit'),
            bgcolor='rgba(15, 23, 42, 0.75)',
            bordercolor='rgba(139, 92, 246, 0.5)',
            borderwidth=1,
        ),
        paper_bgcolor='rgba(15, 23, 42, 0)',
        plot_bgcolor='rgba(15, 23, 42, 0.35)',
        margin=dict(l=30, r=30, t=70, b=40),
        coloraxis_colorbar=dict(
            tickfont=dict(color='#ffffff', family='Outfit'),
            title_font=dict(color='#ffffff', family='Outfit'),
            outlinecolor='rgba(139, 92, 246, 0.5)',
            outlinewidth=1,
        ),
        hoverlabel=dict(
            bgcolor='#1e1b4b',
            bordercolor='#22d3ee',
            font=dict(color='#ffffff', size=13, family='Outfit'),
        ),
    )
    fig.update_xaxes(
        tickfont=dict(color='#e2e8f0', size=12, family='Outfit'),
        title_font=dict(color='#67e8f9', size=13, family='Outfit'),
        gridcolor='rgba(139, 92, 246, 0.12)',
        zerolinecolor='rgba(139, 92, 246, 0.3)',
        showline=True,
        linecolor='rgba(139, 92, 246, 0.4)',
    )
    fig.update_yaxes(
        tickfont=dict(color='#e2e8f0', size=12, family='Outfit'),
        title_font=dict(color='#67e8f9', size=13, family='Outfit'),
        gridcolor='rgba(139, 92, 246, 0.12)',
        zerolinecolor='rgba(139, 92, 246, 0.3)',
        showline=True,
        linecolor='rgba(139, 92, 246, 0.4)',
    )
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

# ============================================
# TABS
# ============================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview", "👥 Demographics", "📚 Course Analysis", "🎯 Preferences", "📈 Insights"
])

# ============================================
# TAB 1: OVERVIEW
# ============================================
with tab1:
    st.markdown("## 📊 Platform Overview")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("👥 Total Learners", f"{users['UserID'].nunique():,}")
    c2.metric("📚 Total Courses", f"{courses['CourseID'].nunique():,}")
    c3.metric("🛒 Total Enrollments", f"{len(transactions):,}")
    c4.metric("👨‍🏫 Total Teachers", f"{teachers['TeacherID'].nunique():,}")

    st.markdown("---")

    fp = courses['CourseType'].value_counts()
    fig = px.pie(values=fp.values, names=fp.index,
                 title="🎁 Free vs Paid Courses",
                 color_discrete_sequence=['#22d3ee', '#f472b6'], hole=0.45)
    fig.update_traces(
        textinfo='percent+label',
        textfont=dict(size=14, color='#ffffff', family='Outfit'),
        marker=dict(line=dict(color='#0f172a', width=3)),
    )
    styled_chart(fig)

    cc = courses['CourseCategory'].value_counts()
    fig = px.bar(x=cc.values, y=cc.index, orientation='h',
                 title="📚 Courses by Category",
                 color=cc.values, color_continuous_scale=BRIGHT_CONTINUOUS,
                 text=cc.values)
    fig.update_traces(textposition='outside')
    styled_chart(fig, height=480)

    lc = courses['CourseLevel'].value_counts()
    fig = px.pie(values=lc.values, names=lc.index,
                 title="📊 Course Levels",
                 color_discrete_sequence=['#22d3ee', '#a78bfa', '#f472b6'], hole=0.45)
    fig.update_traces(
        textinfo='percent+label',
        textfont=dict(size=14, color='#ffffff', family='Outfit'),
        marker=dict(line=dict(color='#0f172a', width=3)),
    )
    styled_chart(fig)

    course_ratings = courses['CourseRating'].dropna()
    bins = pd.cut(course_ratings, bins=20)
    rating_counts = bins.value_counts().sort_index()
    labels = [f"{iv.left:.1f}–{iv.right:.1f}" for iv in rating_counts.index]

    fig = px.bar(x=labels, y=rating_counts.values,
                 title="⭐ Course Ratings Distribution",
                 color=rating_counts.values, color_continuous_scale='Plasma',
                 text=rating_counts.values)
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title="Rating Range", yaxis_title="Number of Courses", xaxis_tickangle=-45)
    styled_chart(fig)

# ============================================
# TAB 2: DEMOGRAPHICS
# ============================================
with tab2:
    st.markdown("## 👥 Learner Demographics")
    st.caption("Sidebar filters apply here.")

    age_dist = users['Age'].value_counts().sort_index()
    fig = px.bar(x=age_dist.index, y=age_dist.values,
                 labels={'x': 'Age', 'y': 'Count'},
                 title="📊 Age Distribution of Learners",
                 color=age_dist.values, color_continuous_scale='Turbo')
    styled_chart(fig)

    gd = users['Gender'].value_counts()
    fig = px.pie(values=gd.values, names=gd.index,
                 title="👫 Gender Distribution",
                 color_discrete_sequence=['#22d3ee', '#f472b6', '#facc15'], hole=0.45)
    fig.update_traces(
        textinfo='percent+label',
        textfont=dict(size=14, color='#ffffff', family='Outfit'),
        marker=dict(line=dict(color='#0f172a', width=3)),
    )
    styled_chart(fig)

    ae = filtered['AgeGroup'].value_counts().reindex(AGE_ORDER).fillna(0)
    fig = px.bar(x=ae.index, y=ae.values,
                 labels={'x': 'Age Group', 'y': 'Enrollments'},
                 title="🎯 Enrollments by Age Group",
                 color=ae.values, color_continuous_scale=BRIGHT_CONTINUOUS,
                 text=ae.values.astype(int))
    fig.update_traces(textposition='outside')
    styled_chart(fig)

    gc = filtered.groupby(['Gender', 'CourseCategory']).size().reset_index(name='Enrollments')
    fig = px.bar(gc, x='CourseCategory', y='Enrollments', color='Gender',
                 barmode='group',
                 title="🎨 Gender × Course Category",
                 color_discrete_sequence=['#22d3ee', '#f472b6', '#facc15'])
    styled_chart(fig, height=480)

# ============================================
# TAB 3: COURSE ANALYSIS
# ============================================
with tab3:
    st.markdown("## 📚 Course Popularity Analysis")

    ce = filtered['CourseCategory'].value_counts()
    fig = px.bar(x=ce.values, y=ce.index, orientation='h',
                 labels={'x': 'Enrollments', 'y': 'Category'},
                 title="🏆 Most Popular Categories",
                 color=ce.values, color_continuous_scale=BRIGHT_CONTINUOUS,
                 text=ce.values)
    fig.update_traces(textposition='outside')
    styled_chart(fig, height=480)

    le = filtered['CourseLevel'].value_counts()
    fig = px.pie(values=le.values, names=le.index,
                 title="🎓 Enrollments by Level",
                 color_discrete_sequence=['#22d3ee', '#a78bfa', '#f472b6'], hole=0.45)
    fig.update_traces(
        textinfo='percent+label',
        textfont=dict(size=14, color='#ffffff', family='Outfit'),
        marker=dict(line=dict(color='#0f172a', width=3)),
    )
    styled_chart(fig)

    te = filtered['CourseType'].value_counts()
    fig = px.pie(values=te.values, names=te.index,
                 title="💰 Free vs Paid Enrollments",
                 color_discrete_sequence=['#22d3ee', '#f472b6'], hole=0.45)
    fig.update_traces(
        textinfo='percent+label',
        textfont=dict(size=14, color='#ffffff', family='Outfit'),
        marker=dict(line=dict(color='#0f172a', width=3)),
    )
    styled_chart(fig)

    tc = filtered['CourseName'].value_counts().head(10)
    fig = px.bar(x=tc.values, y=tc.index, orientation='h',
                 labels={'x': 'Enrollments', 'y': 'Course'},
                 title="🔥 Top 10 Most Enrolled Courses",
                 color=tc.values, color_continuous_scale='Plasma',
                 text=tc.values)
    fig.update_traces(textposition='outside')
    styled_chart(fig, height=500)

# ============================================
# TAB 4: PREFERENCES (HEATMAPS)
# ============================================
with tab4:
    st.markdown("## 🎯 Learner Preference Analysis")

    h1 = filtered.groupby(['AgeGroup', 'CourseCategory']).size().reset_index(name='Enrollments')
    p1 = h1.pivot(index='AgeGroup', columns='CourseCategory', values='Enrollments').fillna(0)
    p1 = p1.reindex([a for a in AGE_ORDER if a in p1.index])
    fig = px.imshow(p1,
                    labels=dict(x="Category", y="Age Group", color="Enrollments"),
                    title="🔥 Age Group × Course Category",
                    color_continuous_scale='Magma', text_auto=True, aspect='auto')
    styled_chart(fig, height=450)

    h2 = filtered.groupby(['Gender', 'CourseLevel']).size().reset_index(name='Enrollments')
    p2 = h2.pivot(index='Gender', columns='CourseLevel', values='Enrollments').fillna(0)
    fig = px.imshow(p2,
                    labels=dict(x="Level", y="Gender", color="Enrollments"),
                    title="🔥 Gender × Course Level",
                    color_continuous_scale='Plasma', text_auto=True, aspect='auto')
    styled_chart(fig, height=350)

    h3 = filtered.groupby(['CourseCategory', 'CourseLevel']).size().reset_index(name='Enrollments')
    p3 = h3.pivot(index='CourseCategory', columns='CourseLevel', values='Enrollments').fillna(0)
    fig = px.imshow(p3,
                    labels=dict(x="Level", y="Category", color="Enrollments"),
                    title="🔥 Category × Level",
                    color_continuous_scale='Turbo', text_auto=True, aspect='auto')
    styled_chart(fig, height=500)

# ============================================
# TAB 5: INSIGHTS
# ============================================
with tab5:
    st.markdown("## 📈 Behavioral Insights & KPIs")

    total_enr = len(filtered)
    uniq_learners = filtered['UserID'].nunique()
    avg_courses = (total_enr / uniq_learners) if uniq_learners else 0
    top_cat = filtered['CourseCategory'].value_counts().idxmax() if total_enr else "N/A"
    top_age = filtered['AgeGroup'].value_counts().idxmax() if total_enr else "N/A"

    c1, c2, c3 = st.columns(3)
    c1.metric("📊 Avg Courses / Learner", f"{avg_courses:.2f}")
    c2.metric("🏆 Top Category", top_cat)
    c3.metric("👥 Most Active Age", top_age)

    st.markdown("---")
    st.markdown("### 📊 Enrollment Concentration")

    if total_enr > 0:
        ue = filtered.groupby('UserID').size().reset_index(name='Enrollments').sort_values('Enrollments', ascending=False)
        top10 = max(1, int(len(ue) * 0.1))
        share = ue.head(top10)['Enrollments'].sum() / total_enr * 100
        st.info(f"🎯 **Top 10% of active learners account for {share:.1f}% of enrollments**")

        enrollments_data = ue['Enrollments']
        bins_enr = pd.cut(enrollments_data, bins=30)
        enr_counts = bins_enr.value_counts().sort_index()
        labels_enr = [f"{iv.left:.0f}–{iv.right:.0f}" for iv in enr_counts.index]

        fig = px.bar(x=labels_enr, y=enr_counts.values,
                     title="Distribution of Enrollments per Learner",
                     color=enr_counts.values, color_continuous_scale=BRIGHT_CONTINUOUS)
        fig.update_layout(
            xaxis_title="Enrollments per Learner",
            yaxis_title="Count of Learners",
            xaxis_tickangle=-45,
        )
        styled_chart(fig)

    st.markdown("### 🎓 Beginner vs Advanced")
    ls = filtered.groupby('CourseLevel').agg(
        UniqueLearners=('UserID', 'nunique'),
        TotalEnrollments=('TransactionID', 'count')
    ).reset_index()
    ls['AvgCourses'] = (ls['TotalEnrollments'] / ls['UniqueLearners']).round(2)
    st.dataframe(ls, use_container_width=True, hide_index=True)

    st.markdown("### 📅 Enrollment Trend Over Time")