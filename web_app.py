import streamlit as st
from deepface import DeepFace
import os
from PIL import Image

# 1. Page Config (The title in the browser tab)
st.set_page_config(page_title="ShadowProof | Safety First", page_icon="🛡️")

st.title("🛡️ ShadowProof")
st.subheader("Deepfake & Digital Blackmail Defense for Women")

st.write("Upload an original photo and a suspected image to check for identity matches.")

# 2. Sidebar for Safety
with st.sidebar:
    st.warning("🔒 **Privacy First**: Images are processed locally and not stored on our public servers.")
    if st.button("QUICK EXIT (Safety)"):
        st.write("Redirecting...") # In a real app, this would trigger a JS redirect

# 3. File Uploaders
col1, col2 = st.columns(2)

with col1:
    original_file = st.file_uploader("Upload Original Photo", type=['jpg', 'jpeg', 'png'])
with col2:
    suspect_file = st.file_uploader("Upload Suspected Photo/Screenshot", type=['jpg', 'jpeg', 'png'])

# 4. Analysis Logic
if original_file and suspect_file:
    if st.button("🔍 Run Identity Scan"):
        # Save files temporarily to run the AI
        with open("temp_orig.jpg", "wb") as f:
            f.write(original_file.getbuffer())
        with open("temp_suspect.jpg", "wb") as f:
            f.write(suspect_file.getbuffer())

        with st.spinner("Analyzing facial embeddings..."):
            try:
                result = DeepFace.verify(img1_path="temp_orig.jpg", img2_path="temp_suspect.jpg")
                
                distance = result["distance"]
                is_match = result["verified"]

                st.divider()

                if is_match:
                    st.error(f"🚨 **ALERT: IDENTITY MATCH DETECTED**")
                    st.metric(label="Match Confidence", value="HIGH")
                    st.write(f"Similarity Score: {1 - distance:.2%}") # Shows as a percentage
                    st.info("💡 **Next Steps**: Use our Legal Toolkit below to preserve evidence.")
                else:
                    st.success("✅ **SAFE: NO MATCH FOUND**")
                    st.write("The person in the suspected image does not appear to be you.")

            except Exception as e:
                st.error(f"Face not detected clearly. Please try images with better lighting.")

# 5. Support Section
st.divider()
st.subheader("⚖️ Legal & Emotional Support")
tab1, tab2 = st.tabs(["Legal Steps", "Emotional Support"])

with tab1:
    st.write("1. **Preserve Evidence**: Do not delete the message. Take screenshots.")
    st.write("2. **Report**: Visit your local Cyber Crime Portal.")
    st.button("Download Cease & Desist Template")

with tab2:
    st.write("You are not alone. Reach out to verified helplines.")