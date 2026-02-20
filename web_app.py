import streamlit as st
from deepface import DeepFace
import os

# --- Page Config & Styling ---
st.set_page_config(page_title="ShadowProof | Identity Sanctuary", layout="wide", page_icon="🛡️")

# --- CUSTOM CSS FOR ELEGANCE ---
st.markdown("""
    <style>
    /* Change the main font to something more elegant */
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #1E1B4B;
    }

    /* Gradient Header Background */
    .stApp {
        background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%);
    }

    /* Styled Buttons */
    .stButton>button {
        background-color: #6366F1;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.6rem 2rem;
        transition: all 0.3s ease;
        font-weight: 600;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button:hover {
        background-color: #4F46E5;
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    /* Card styling */
    div[data-testid="stExpander"] {
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        background-color: white;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>Guardian Menu</h2>", unsafe_allow_html=True)
    page = st.radio("Navigate to:", ["🛡️ Identity Sanctuary", "🌐 Site X (Simulated)"])
    st.markdown("---")
    st.write("✨ **ShadowProof** is built to empower women in the digital age.")

# --- PAGE 1: SHADOWPROOF (The Winning UI) ---
if page == "🛡️ Identity Sanctuary":
    # Hero Section
    st.markdown("<h1 style='text-align: center; font-size: 3rem;'>Reclaim Your Presence.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4B5563; font-size: 1.2rem;'>Advanced biometric defense for the modern woman.</p>", unsafe_allow_html=True)
    
    st.markdown("---")

    # Main Tool Section with better spacing
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 🔍 Global Identity Scan")
        original_file = st.file_uploader("Upload your profile photo", type=['jpg', 'png'])
        
        if original_file:
            with open("temp_real.jpg", "wb") as f:
                f.write(original_file.getbuffer())
            
            if st.button("Begin Biometric Audit", use_container_width=True):
                # ... [Keep your scan logic here] ...
                st.balloons() # Adding a small 'success' celebration for clean scans
                st.success("Analysis complete. Your digital footprint is currently secure.")

    # --- Resource Hub with "Glassmorphism" look ---
    st.markdown("<h3 style='margin-top: 3rem;'>Empowerment & Action Hub</h3>", unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        with st.container():
            st.markdown("#### ⚖️ Legal Shield")
            st.info("Direct paths to justice and takedown rights.")
            st.button("Takedown Guides", key="btn_legal")

    with col_b:
        with st.container():
            st.markdown("#### ❤️ Sisterhood Support")
            st.info("Anonymous mental health and peer support.")
            st.button("Reach Out", key="btn_support")

    with col_c:
        with st.container():
            st.markdown("#### 🛡️ Safe-Share Pro")
            st.info("Cryptographic cloaking for your next post.")
            st.button("Cloak Photo", key="btn_cloak")

# --- FOOTER ---
st.markdown("<br><hr><p style='text-align: center; color: #9CA3AF;'>ShadowProof © 2026 | Dedicated to Every Woman's Digital Safety</p>", unsafe_allow_html=True)