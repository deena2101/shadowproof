import streamlit as st
from deepface import DeepFace
import os

# --- Page Config ---
st.set_page_config(
    page_title="ShadowProof | Identity Sanctuary",
    layout="wide",
    page_icon="🛡️"
)

# --- PREMIUM UI CSS ---
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #fdf2f8 40%, #eef2ff 100%);
}

/* Headings */
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #1E1B4B;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #f3f4f6 100%);
    border-right: 1px solid #e5e7eb;
    padding-top: 20px;
}

section[data-testid="stSidebar"] .stRadio > div {
    background: white;
    padding: 12px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

/* File Uploader */
div[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 25px;
    border: 2px dashed #c7d2fe;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #6366F1, #A855F7);
    color: white;
    border-radius: 30px;
    border: none;
    padding: 0.7rem 2rem;
    font-weight: 600;
    transition: all 0.3s ease;
    box-shadow: 0 10px 25px rgba(99,102,241,0.25);
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 20px 35px rgba(99,102,241,0.35);
}

/* Glass Card */
.glass-card {
    background: rgba(255,255,255,0.6);
    backdrop-filter: blur(20px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    border: 1px solid rgba(255,255,255,0.4);
}

/* Divider */
hr {
    margin-top: 3rem;
    margin-bottom: 1rem;
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #d1d5db, transparent);
}

</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>Guardian Menu</h2>", unsafe_allow_html=True)
    page = st.radio("", ["🛡️ Identity Sanctuary", "🌐 Site X (Simulated)"])
    st.markdown("---")
    st.markdown("✨ **ShadowProof** empowers women in the digital age.")

# --- MAIN PAGE ---
if page == "🛡️ Identity Sanctuary":

    # Hero Section
    st.markdown("""
    <div style='text-align:center; padding-top:40px; padding-bottom:10px;'>
        <h1 style='font-size:3.2rem;'>Reclaim Your Presence.</h1>
        <p style='color:#4B5563; font-size:1.2rem; margin-top:10px;'>
        Advanced biometric defense for the modern woman.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Center Scan Section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### 🔍 Global Identity Scan")

        uploaded_file = st.file_uploader("Upload your profile photo", type=['jpg', 'png'])

        if uploaded_file:
            with open("temp_real.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())

            st.image("temp_real.jpg", caption="Uploaded Image", width="stretch")

            if st.button("Begin Biometric Audit", use_container_width=True):

                try:
                    # For demo, comparing image with itself
                    # Replace second image path with database image if needed
                    result = DeepFace.verify("temp_real.jpg", "temp_real.jpg", enforce_detection=False)

                    confidence = round((1 - result["distance"]) * 100, 2)

                    if result["verified"]:
                        st.error("🚨 Face Match Detected")
                        st.warning("⚠ Possible Manipulation Detected")
                        st.metric("📊 Confidence Score", f"{confidence}%")

                    else:
                        st.balloons()
                        st.success("✅ No match found. Your digital footprint is secure.")
                        st.metric("📊 Confidence Score", f"{confidence}%")

                except Exception as e:
                    st.error("⚠ Error processing image. Please try again.")

        st.markdown("</div>", unsafe_allow_html=True)

    # Resource Hub
    st.markdown("<h3 style='margin-top:4rem;'>Empowerment & Action Hub</h3>", unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("#### ⚖️ Legal Shield")
        st.info("Direct paths to justice and takedown rights.")
        st.button("Takedown Guides", key="btn_legal")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("#### ❤️ Sisterhood Support")
        st.info("Anonymous mental health and peer support.")
        st.button("Reach Out", key="btn_support")
        st.markdown("</div>", unsafe_allow_html=True)

    with col_c:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("#### 🛡️ Safe-Share Pro")
        st.info("Cryptographic cloaking for your next post.")
        st.button("Cloak Photo", key="btn_cloak")
        st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<br>
<hr>
<p style='text-align:center; color:#9CA3AF;'>
ShadowProof © 2026 | Dedicated to Every Woman's Digital Safety
</p>
""", unsafe_allow_html=True)