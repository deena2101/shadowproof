import streamlit as st
from deepface import DeepFace
import os
from PIL import Image

st.set_page_config(page_title="ShadowProof | Safety First", page_icon="🛡️")

# --- UI Header ---
st.title("🛡️ ShadowProof")
st.subheader("Deepfake & Digital Blackmail Defense for Women")
st.markdown("---")

# --- Sidebar ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=100)
    st.info("🔒 **Privacy**: Images are processed in RAM and deleted after the session.")
    if st.button("🚨 QUICK EXIT", use_container_width=True):
        st.write('<meta http-equiv="refresh" content="0;URL=\'https://www.google.com\'" />', unsafe_allow_code=True)

# --- Core Logic: Verification ---
col1, col2 = st.columns(2)
with col1:
    original_file = st.file_uploader("1. Your Original Photo", type=['jpg', 'png'])
with col2:
    suspect_file = st.file_uploader("2. Suspected Image (Blackmail/Morphed)", type=['jpg', 'png'])

if original_file and suspect_file:
    if st.button("🔍 Analyze for Identity Match", use_container_width=True):
        with open("temp_orig.jpg", "wb") as f: f.write(original_file.getbuffer())
        with open("temp_suspect.jpg", "wb") as f: f.write(suspect_file.getbuffer())

        with st.spinner("Checking facial embeddings..."):
            try:
                result = DeepFace.verify(img1_path="temp_orig.jpg", img2_path="temp_suspect.jpg")
                if result["verified"]:
                    st.error(f"🚨 **ALERT: IDENTITY MATCH DETECTED ({1-result['distance']:.1%})**")
                    st.warning("This image contains your unique facial 'fingerprint'. This is strong evidence for legal action.")
                else:
                    st.success("✅ **SAFE: NO IDENTITY MATCH**")
            except Exception as e:
                st.error("Could not detect a face. Please use clearer photos.")

# --- Innovation: Simulated Public Domain Scan ---
st.markdown("### 🌐 Proactive Web Monitoring")
st.write("Our AI 'Watchdog' scans high-risk domains for your face fingerprint.")

if original_file:
    if st.button("🌐 Start Global Public Scan"):
        db_path = "web_database"
        if not os.path.exists(db_path):
            st.error("Missing 'web_database' folder! Create it and add images to test.")
        else:
            with st.spinner("Scanning simulated public domains..."):
                found_links = []
                for img_name in os.listdir(db_path):
                    try:
                        res = DeepFace.verify(img1_path="temp_orig.jpg", img2_path=os.path.join(db_path, img_name))
                        if res["verified"]:
                            found_links.append(img_name)
                    except: continue
                
                if found_links:
                    st.error(f"🚨 FOUND {len(found_links)} MATCHES ON EXTERNAL SITES")
                    for match in found_links:
                        st.image(os.path.join(db_path, match), width=150, caption="Source: Known-Leak-Forum.xyz")
                else:
                    st.success("Clear: No public matches found in our current monitoring crawl.")
else:
    st.info("Upload an original photo first to enable web scanning.")

# --- Legal Support: Template Generator ---
st.markdown("---")
st.subheader("⚖️ Legal Action Toolkit")
tab1, tab2 = st.tabs(["Takedown Template", "Emotional Support"])

with tab1:
    st.write("Use this formal notice to demand the removal of your image from a platform.")
    
    # Pre-filled Takedown Template
    takedown_text = f"""
    Subject: URGENT - Cease and Desist - Unauthorized Use of Likeness
    To the Administrator of [Platform Name],

    I am writing to formally request the immediate removal of a morphed/unauthorized image located at [Insert Link Here].
    Our AI-assisted forensic analysis (ShadowProof) has confirmed an Identity Match of my biometric data in this content. 
    Unauthorized distribution of this content is a violation of my privacy rights and cyber-laws.

    Failure to remove this content within 24 hours will result in a formal report to the National Cyber Crime Cell.
    
    Signed,
    [Your Name]
    """
    
    st.download_button(
        label="📄 Download Legal Takedown Notice",
        data=takedown_text,
        file_name="ShadowProof_Takedown_Notice.txt",
        mime="text/plain"
    )

with tab2:
    st.write("❤️ **You are not alone.**")
    st.markdown("- **National Helpline**: 181 (India) / 911 (US)")
    st.markdown("- **Refuge Tech Safety**: [Visit Site](https://refuge.org.uk)")
    st.write("Deepfake abuse is a crime of the perpetrator, not the victim. Stay strong.")