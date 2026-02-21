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
# PREMIUM DARK UI CSS
# ---------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* ========== ROOT & GLOBAL ========== */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    color: #e2e8f0 !important;
}

.stApp {
    background: linear-gradient(135deg, #0a0a1a 0%, #0f0f2e 25%, #1a0a2e 50%, #0a1628 75%, #0a0a1a 100%);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

h1, h2, h3, h4 {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #f1f5f9 !important;
}

/* ========== SCROLLBAR ========== */
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #0a0a1a; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, #6366f1, #a855f7); border-radius: 10px; }

/* ========== SIDEBAR ========== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0d2b 0%, #1a1145 40%, #2d1b69 100%) !important;
    border-right: 1px solid rgba(139, 92, 246, 0.2);
}

section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}

section[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.04);
    border-radius: 12px;
    padding: 10px 16px;
    margin-bottom: 6px;
    transition: all 0.3s ease;
    border: 1px solid rgba(139, 92, 246, 0.1);
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(139, 92, 246, 0.15);
    border-color: rgba(139, 92, 246, 0.4);
    transform: translateX(4px);
}

/* ========== HERO ========== */
.hero-container {
    text-align: center;
    padding: 60px 20px 40px;
    position: relative;
}

.hero-icon {
    font-size: 4rem;
    display: inline-block;
    animation: pulse 2s ease-in-out infinite;
    filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.6));
}

@keyframes pulse {
    0%, 100% { transform: scale(1); filter: drop-shadow(0 0 20px rgba(139, 92, 246, 0.6)); }
    50% { transform: scale(1.1); filter: drop-shadow(0 0 35px rgba(139, 92, 246, 0.9)); }
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 3.8rem !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #818cf8, #a78bfa, #c084fc, #e879f9, #818cf8);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: textGradient 4s ease infinite;
    margin: 10px 0 !important;
    letter-spacing: -1px;
}

@keyframes textGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero-subtitle {
    font-size: 1.25rem;
    color: #94a3b8 !important;
    font-weight: 300;
    letter-spacing: 0.5px;
    max-width: 600px;
    margin: 0 auto;
}

.hero-badge {
    display: inline-block;
    margin-top: 20px;
    padding: 8px 20px;
    background: rgba(139, 92, 246, 0.15);
    border: 1px solid rgba(139, 92, 246, 0.3);
    border-radius: 999px;
    font-size: 0.85rem;
    color: #c4b5fd !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    animation: badgeGlow 3s ease-in-out infinite;
}

@keyframes badgeGlow {
    0%, 100% { box-shadow: 0 0 10px rgba(139, 92, 246, 0.2); }
    50% { box-shadow: 0 0 25px rgba(139, 92, 246, 0.5); }
}

/* ========== GLASS CARDS ========== */
.glass-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 30px;
    margin: 10px 0;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
}

.glass-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, #818cf8, #a855f7, transparent);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.glass-card:hover {
    transform: translateY(-6px);
    border-color: rgba(139, 92, 246, 0.3);
    box-shadow: 0 20px 60px rgba(139, 92, 246, 0.15),
                0 0 40px rgba(99, 102, 241, 0.08);
}

.glass-card:hover::before {
    opacity: 1;
}

/* Card color variants */
.glass-card-purple { border-left: 3px solid #8b5cf6; }
.glass-card-pink { border-left: 3px solid #ec4899; }
.glass-card-cyan { border-left: 3px solid #06b6d4; }

.glass-card-purple:hover { box-shadow: 0 20px 60px rgba(139, 92, 246, 0.2); }
.glass-card-pink:hover { box-shadow: 0 20px 60px rgba(236, 72, 153, 0.2); }
.glass-card-cyan:hover { box-shadow: 0 20px 60px rgba(6, 182, 212, 0.2); }

/* ========== SCAN SECTION ========== */
.scan-section {
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 24px;
    padding: 40px;
    margin: 20px 0;
    position: relative;
}

.scan-section::after {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: 24px;
    padding: 1px;
    background: linear-gradient(135deg, rgba(99,102,241,0.3), transparent, rgba(168,85,247,0.3));
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.6rem !important;
    color: #e2e8f0 !important;
    margin-bottom: 8px !important;
}

.section-desc {
    color: #94a3b8 !important;
    font-size: 0.95rem;
    margin-bottom: 20px;
}

/* ========== FILE UPLOADER ========== */
div[data-testid="stFileUploader"] {
    background: rgba(255, 255, 255, 0.03);
    padding: 40px;
    border-radius: 20px;
    border: 2px dashed rgba(139, 92, 246, 0.4);
    text-align: center;
    transition: all 0.4s ease;
    position: relative;
}

div[data-testid="stFileUploader"]:hover {
    border-color: rgba(168, 85, 247, 0.7);
    box-shadow: 0 0 30px rgba(139, 92, 246, 0.15),
                inset 0 0 30px rgba(139, 92, 246, 0.05);
    transform: translateY(-3px);
}

div[data-testid="stFileUploader"] small {
    display: none;
}

div[data-testid="stFileUploader"] button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7) !important;
    color: white !important;
    border-radius: 30px !important;
    border: none !important;
    padding: 0.6rem 1.8rem !important;
    font-weight: 600 !important;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.35);
    transition: all 0.3s ease;
}

div[data-testid="stFileUploader"] button:hover {
    box-shadow: 0 12px 35px rgba(139, 92, 246, 0.5);
    transform: translateY(-2px);
}

div[data-testid="stFileUploader"] section {
    background-color: rgba(255, 255, 255, 0.05);
    padding: 12px;
    border-radius: 14px;
    margin-top: 15px;
    border: 1px solid rgba(255, 255, 255, 0.08);
}

/* ========== BUTTONS ========== */
.stButton>button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6, #a855f7) !important;
    color: white !important;
    border-radius: 14px !important;
    padding: 0.7rem 2rem !important;
    border: none !important;
    font-weight: 600 !important;
    font-family: 'Outfit', sans-serif !important;
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    letter-spacing: 0.3px;
}

.stButton>button:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 15px 40px rgba(139, 92, 246, 0.45) !important;
}

.stButton>button:active {
    transform: translateY(0) scale(0.98) !important;
}

/* ========== RESULT / ALERT BOXES ========== */
div[data-testid="stAlert"] {
    background: rgba(255, 255, 255, 0.04) !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    backdrop-filter: blur(10px);
}

/* ========== HUB SECTION ========== */
.hub-header {
    text-align: center;
    margin: 50px 0 30px;
}

.hub-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 2.2rem !important;
    color: #f1f5f9 !important;
    margin-bottom: 8px !important;
}

.hub-subtitle {
    color: #94a3b8 !important;
    font-size: 1rem;
}

.card-icon {
    font-size: 2.5rem;
    margin-bottom: 10px;
    display: inline-block;
}

.card-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.3rem !important;
    color: #f1f5f9 !important;
    margin: 8px 0 !important;
}

.card-desc {
    color: #94a3b8 !important;
    font-size: 0.9rem;
    line-height: 1.6;
}

/* ========== DIVIDER ========== */
.glow-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.4), transparent);
    margin: 40px 0;
    border: none;
}

/* ========== FOOTER ========== */
.footer {
    text-align: center;
    padding: 40px 20px;
    margin-top: 60px;
    position: relative;
}

.footer::before {
    content: '';
    position: absolute;
    top: 0;
    left: 10%;
    right: 10%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.3), transparent);
}

.footer-text {
    color: #475569 !important;
    font-size: 0.85rem;
    letter-spacing: 1px;
    transition: color 0.3s ease;
}

.footer-text:hover {
    color: #94a3b8 !important;
}

/* ========== IMAGES ========== */
img {
    border-radius: 16px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
}

/* ========== EXPANDER (for expanded sections) ========== */
.stMarkdown {
    color: #cbd5e1 !important;
}

/* ========== SITE X STYLING ========== */
.site-x-header {
    text-align: center;
    padding: 40px 20px;
}

.site-x-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 2.8rem !important;
    color: #f1f5f9 !important;
}

.site-x-subtitle {
    color: #64748b !important;
    font-size: 1rem;
}

/* ========== FLOATING ORBS (decorative) ========== */
.orb-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.12;
    animation: float 20s ease-in-out infinite;
}

.orb-1 {
    width: 400px;
    height: 400px;
    background: #6366f1;
    top: -100px;
    right: -100px;
    animation-delay: 0s;
}

.orb-2 {
    width: 350px;
    height: 350px;
    background: #a855f7;
    bottom: -100px;
    left: -100px;
    animation-delay: -7s;
}

.orb-3 {
    width: 300px;
    height: 300px;
    background: #ec4899;
    top: 50%;
    left: 50%;
    animation-delay: -14s;
}

@keyframes float {
    0%, 100% { transform: translate(0, 0) scale(1); }
    25% { transform: translate(30px, -30px) scale(1.05); }
    50% { transform: translate(-20px, 20px) scale(0.95); }
    75% { transform: translate(15px, 15px) scale(1.02); }
}

</style>
""", unsafe_allow_html=True)

# Floating decorative orbs
st.markdown("""
<div class="orb-container">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:
    st.markdown("""
        <div style='text-align:center; padding: 20px 0 10px;'>
            <div style='font-size: 2.5rem; margin-bottom: 5px;'>🛡️</div>
            <h2 style='margin: 0; font-size: 1.4rem; letter-spacing: 1px;'>SHADOWPROOF</h2>
            <p style='color: #94a3b8 !important; font-size: 0.8rem; letter-spacing: 3px; text-transform: uppercase; margin-top: 4px;'>Identity Sanctuary</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    page = st.radio("Navigate to:", ["🛡️ ShadowProof", "🌐 Site X (Simulated)"])

    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    st.markdown("""
        <div style='padding: 16px; background: rgba(139,92,246,0.08); border-radius: 14px; border: 1px solid rgba(139,92,246,0.15);'>
            <p style='font-size: 0.85rem; color: #c4b5fd !important; margin: 0; line-height: 1.6;'>
                ✨ <strong>ShadowProof</strong> empowers women with AI-powered biometric defense in the digital age.
            </p>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------
# MAIN PAGE — SHADOWPROOF
# ---------------------------------------------------
if page == "🛡️ ShadowProof":

    # HERO SECTION
    st.markdown("""
        <div class="hero-container">
            <div class="hero-badge">🔒 AI-Powered Protection</div>
            <br><br>
            <div class="hero-icon">🛡️</div>
            <h1 class="hero-title">ShadowProof</h1>
            <p class="hero-subtitle">
                Advanced biometric defense for the modern woman.<br>
                Detect identity theft. Protect your digital presence. Reclaim your safety.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    # SCAN SECTION
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
            <div class="scan-section">
                <p class="section-title">🔍 Global Identity Scan</p>
                <p class="section-desc">Upload your photo to run an AI-powered biometric audit against potential impersonation.</p>
            </div>
        """, unsafe_allow_html=True)

        original_file = st.file_uploader("Upload your profile photo", type=['jpg', 'png'])

        if original_file:
            with open("temp_real.jpg", "wb") as f:
                f.write(original_file.getbuffer())

            st.image("temp_real.jpg", caption="Uploaded Image", use_container_width=True)

            if st.button("⚡ Begin Biometric Audit", use_container_width=True):
                try:
                    result = DeepFace.verify(
                        img1_path="temp_real.jpg",
                        img2_path="temp_real.jpg",
                        enforce_detection=False
                    )

                    match = result["verified"]
                    distance = result["distance"]
                    confidence = max(0, (1 - distance)) * 100
                    confidence = round(confidence, 2)

                    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

                    if match:
                        st.success("✅ Face Match Detected")
                    else:
                        st.error("❌ No Face Match Detected")

                    if confidence > 0.6:
                        st.warning("⚠️ Possible Manipulation Detected")
                    else:
                        st.info("✔️ No Manipulation Detected")

                    st.write(f"🔎 **Confidence Score:** {confidence}")

                    st.markdown("</div>", unsafe_allow_html=True)

                except Exception as e:
                    st.error("Face analysis failed. Please try another image.")

    # EMPOWERMENT HUB
    st.markdown("""
        <div class="hub-header">
            <div class='glow-divider'></div>
            <h2 class="hub-title">Empowerment & Action Hub</h2>
            <p class="hub-subtitle">Resources, support, and tools to protect your digital identity</p>
        </div>
    """, unsafe_allow_html=True)

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("""
            <div class='glass-card glass-card-purple'>
                <div class='card-icon'>⚖️</div>
                <p class='card-title'>Legal Shield</p>
                <p class='card-desc'>Direct paths to justice and takedown rights for impersonation cases.</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("📜 Takedown Guides", key="btn_legal"):
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

    with col_b:
        st.markdown("""
            <div class='glass-card glass-card-pink'>
                <div class='card-icon'>❤️</div>
                <p class='card-title'>Sisterhood Support</p>
                <p class='card-desc'>Anonymous mental health resources and peer support network.</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🤝 Reach Out", key="btn_support"):
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

    with col_c:
        st.markdown("""
            <div class='glass-card glass-card-cyan'>
                <div class='card-icon'>🛡️</div>
                <p class='card-title'>Safe-Share Pro</p>
                <p class='card-desc'>Cryptographic cloaking and watermarking for your photos.</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🔐 Cloak Photo", key="btn_cloak"):
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

                st.image(image, caption="🔐 Cloaked Image", use_container_width=True)

                st.success("Image successfully cloaked with digital watermark.")

# ---------------------------------------------------
# SITE X PAGE
# ---------------------------------------------------
else:
    # Initialize posts list in session state
    if "site_x_posts" not in st.session_state:
        st.session_state.site_x_posts = []

    st.markdown("""
        <div class="site-x-header">
            <h1 class="site-x-title">🌐 Site X — Simulated Platform</h1>
            <p class="site-x-subtitle">A controlled simulation environment for testing identity detection.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

    st.info("🚧 This is a simulated social media environment. Upload pictures and create posts to test ShadowProof's detection capabilities.")

    # --- CREATE POST SECTION ---
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        st.markdown("""
            <div class='glass-card glass-card-cyan'>
                <div class='card-icon'>✍️</div>
                <p class='card-title'>Create a Post</p>
                <p class='card-desc'>Share a photo and message on the simulated platform.</p>
            </div>
        """, unsafe_allow_html=True)

        # Profile picture
        profile_pic = st.file_uploader("📷 Upload Profile Picture", type=["jpg", "png", "jpeg"], key="site_x_profile")

        # Post content
        post_text = st.text_area("💬 Write your post...", placeholder="What's on your mind?", key="site_x_text")

        # Post image
        post_image = st.file_uploader("🖼️ Add a Photo to Your Post", type=["jpg", "png", "jpeg"], key="site_x_post_img")

        if st.button("📤 Publish Post", use_container_width=True, key="btn_publish"):
            if post_text or post_image:
                post_data = {
                    "text": post_text if post_text else "",
                    "profile_pic": profile_pic.getvalue() if profile_pic else None,
                    "post_image": post_image.getvalue() if post_image else None,
                    "profile_name": profile_pic.name if profile_pic else "Anonymous User",
                }
                st.session_state.site_x_posts.insert(0, post_data)
                st.success("✅ Post published to Site X!")
                st.rerun()
            else:
                st.warning("⚠️ Please add some text or an image to your post.")

    # --- FEED SECTION ---
    if st.session_state.site_x_posts:
        st.markdown("<div class='glow-divider'></div>", unsafe_allow_html=True)

        st.markdown("""
            <div style='text-align: center; margin-bottom: 20px;'>
                <p class='section-title'>📰 Site X Feed</p>
                <p class='section-desc'>Posts on the simulated platform</p>
            </div>
        """, unsafe_allow_html=True)

        col_f1, col_feed, col_f2 = st.columns([1, 2, 1])
        with col_feed:
            for i, post in enumerate(st.session_state.site_x_posts):
                st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

                # Profile header
                header_cols = st.columns([1, 5])
                with header_cols[0]:
                    if post["profile_pic"]:
                        st.image(post["profile_pic"], width=50)
                    else:
                        st.markdown("👤")
                with header_cols[1]:
                    display_name = post.get("profile_name", "Anonymous User")
                    if display_name and display_name != "Anonymous User":
                        display_name = display_name.rsplit('.', 1)[0]
                    st.markdown(f"**{display_name}**")

                # Post text
                if post["text"]:
                    st.write(post["text"])

                # Post image
                if post["post_image"]:
                    st.image(post["post_image"], use_container_width=True)

                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("""
<div class="footer">
    <p class="footer-text">ShadowProof © 2026 — Dedicated to Every Woman's Digital Safety</p>
    <p class="footer-text" style="font-size: 0.75rem; margin-top: 4px;">Built with 💜 and AI</p>
</div>
""", unsafe_allow_html=True)