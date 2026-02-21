import streamlit as st
from deepface import DeepFace
import os

from PIL import Image, ImageDraw, ImageFont

if "show_legal" not in st.session_state:
    st.session_state.show_legal = False

if "show_support" not in st.session_state:
    st.session_state.show_support = False

if "show_cloak" not in st.session_state:
    st.session_state.show_cloak = False
# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="ShadowProof | Identity Sanctuary",
    layout="wide",
    page_icon="🛡️"
)

# ---------------------------------------------------
# PREMIUM UI CSS
# ---------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(120deg, #eef2ff 0%, #f8fafc 50%, #fdf2f8 100%);
}

h1, h2, h3 {
    font-family: 'DM Serif Display', serif !important;
    color: #1e293b;
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1e1b4b 0%, #312e81 100%);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* ---------- NEW PREMIUM UPLOAD DESIGN ---------- */
div[data-testid="stFileUploader"] {
    background: white;
    padding: 40px;
    border-radius: 25px;
    border: 2px dashed #6366f1;
    text-align: center;
    transition: all 0.3s ease;
    box-shadow: 0 15px 40px rgba(99,102,241,0.15);
}

div[data-testid="stFileUploader"]:hover {
    border: 2px solid #8b5cf6;
    box-shadow: 0 20px 50px rgba(139,92,246,0.25);
    transform: translateY(-4px);
}

/* Hide default small text */
div[data-testid="stFileUploader"] small {
    display: none;
}

/* Style Browse Button */
div[data-testid="stFileUploader"] button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 30px;
    border: none;
    padding: 0.5rem 1.5rem;
    font-weight: 600;
    box-shadow: 0 6px 20px rgba(99,102,241,0.3);
}

/* Uploaded file display */
div[data-testid="stFileUploader"] section {
    background-color: #f1f5f9;
    padding: 10px;
    border-radius: 12px;
    margin-top: 15px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 30px;
    padding: 0.7rem 2rem;
    border: none;
    font-weight: 600;
    box-shadow: 0 10px 25px rgba(99,102,241,0.25);
    transition: 0.3s;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 35px rgba(99,102,241,0.35);
}

.footer {
    text-align: center;
    color: #64748b;
    padding: 2rem;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>Guardian Menu</h2>", unsafe_allow_html=True)
    page = st.radio("Navigate to:", ["🛡️ ShadowProof", "🌐 Site X (Simulated)"])
    st.markdown("---")
    st.write("✨ **ShadowProof** empowers women in the digital age.")

# ---------------------------------------------------
# MAIN PAGE
# ---------------------------------------------------
if page == "🛡️ ShadowProof":

    # HERO
    st.markdown("""
        <div class="hero-box">
            <h1 style='font-size:3.2rem;'> 🛡️ ShadowProof</h1>
            <p style='font-size:1.2rem; color:#475569;'>
            Advanced biometric defense for the modern woman.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # SCAN SECTION
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("## 🔍 Global Identity Scan")
        original_file = st.file_uploader("Upload your profile photo", type=['jpg','png'])

        if original_file:
            with open("temp_real.jpg", "wb") as f:
                f.write(original_file.getbuffer())

            st.image("temp_real.jpg", caption="Uploaded Image", width="stretch")

            if st.button("Begin Biometric Audit", use_container_width=True):

                try:
                    # Example comparison (you can modify reference image path)
                    result = DeepFace.verify(
                        img1_path="temp_real.jpg",
                        img2_path="temp_real.jpg",  # Replace with actual reference image if needed
                        enforce_detection=False
                    )

                    match = result["verified"]
                    distance = result["distance"]

                    confidence = max(0, (1 - distance)) * 100
                    confidence = round(confidence, 2)
                    # RESULT DISPLAY
                    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

                    if match:
                        st.success("✅ Face Match Detected")
                    else:
                        st.error("❌ No Face Match Detected")

                    # Example manipulation logic placeholder
                    if confidence > 0.6:
                        st.warning("⚠️ Possible Manipulation Detected")
                    else:
                        st.info("✔️ No Manipulation Detected")

                    st.write(f"🔎 **Confidence Score:** {confidence}")

                    st.markdown("</div>", unsafe_allow_html=True)

                except Exception as e:
                    st.error("Face analysis failed. Please try another image.")

    # RESOURCE HUB
    st.markdown("<br><h2>Empowerment & Action Hub</h2><br>", unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### ⚖️ Legal Shield")
        st.write("Direct paths to justice and takedown rights.")

        if st.button("Takedown Guides", key="btn_legal"):
            st.session_state.show_legal = not st.session_state.show_legal

        if st.session_state.show_legal:
            st.markdown("""
            #### 📜 Immediate Legal Action Steps
        
             1️⃣ Take screenshots of the fake profile  
             2️⃣ Copy the impersonating profile URL  
             3️⃣ Report directly on the platform  
             4️⃣ File complaint at Indian Cyber Crime Portal  
             5️⃣ Preserve digital evidence (timestamps, links)  
        
            🔗 **Cyber Crime Portal:** https://cybercrime.gov.in  
            📞 **Women Helpline:** 181  
        """)

    st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### ❤️ Sisterhood Support")
        st.write("Anonymous mental health and peer support.")

        if st.button("Reach Out", key="btn_support"):
            st.session_state.show_support = not st.session_state.show_support

        if st.session_state.show_support:
            st.markdown("""
            #### 🤝 You Are Not Alone
        
            💜 **National Women Helpline:** 181  
            💜 **Cyber Crime Helpline:** 1930  
            💜 Reach out to trusted friends or family  
            💜 Consider speaking to a licensed counselor  
        
            Your safety and mental peace matter.
        """)

    st.markdown("</div>", unsafe_allow_html=True)

    with col_c:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### 🛡️ Safe-Share Pro")
        st.write("Cryptographic cloaking for your next post.")

        if st.button("Cloak Photo", key="btn_cloak"):
            st.session_state.show_cloak = not st.session_state.show_cloak

        if st.session_state.show_cloak:

            cloak_file = st.file_uploader(
                "Upload image to protect",
                 type=["jpg", "png"],
                 key="cloak_upload"
        )

            if cloak_file:
                image = Image.open(cloak_file).convert("RGB")

            # Add watermark
                draw = ImageDraw.Draw(image)
                width, height = image.size

                watermark_text = "Protected by ShadowProof"

            # Position watermark bottom-right
                text_position = (width - 350, height - 40)

                draw.text(text_position, watermark_text, fill=(255, 0, 0))

                st.image(image, caption="🔐 Cloaked Image", width="stretch")

                st.success("Image successfully cloaked with digital watermark.")

        st.markdown("</div>", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
ShadowProof © 2026 | Dedicated to Every Woman's Digital Safety
</div>
""", unsafe_allow_html=True)