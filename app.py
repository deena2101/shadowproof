from deepface import DeepFace
import os

def run_shadowproof():
    # 1. Define the file names
    img1 = "original.jpg"
    img2 = "suspect.jpg"

    # 2. Check if the images actually exist in the folder
    if not os.path.exists(img1) or not os.path.exists(img2):
        print("❌ Error: I can't find 'original.jpg' or 'suspect.jpg' in your folder.")
        print("Make sure you dragged them into the VS Code sidebar!")
        return

    print("🧠 ShadowProof AI is analyzing the facial embeddings...")

    try:
        # 3. This is the 'Magic' line. 
        # It detects the face, creates the numerical fingerprint, and compares them.
        result = DeepFace.verify(
            img1_path = img1, 
            img2_path = img2, 
            model_name = "VGG-Face",
            distance_metric = "cosine"
        )

        # 4. Extracting the data
        is_match = result["verified"]
        score = result["distance"] # In cosine similarity, 0 is identical, 1 is opposite

        print("\n" + "="*30)
        if is_match:
            print("🚨 ALERT: IDENTITY MATCH DETECTED")
            print("Confidence Level: HIGH")
        else:
            print("✅ SAFE: NO MATCH FOUND")
            print("The faces appear to belong to different individuals.")
        
        # Explain the 'Distance' in human terms
        # 0.40 is the standard threshold for VGG-Face
        print(f"Similarity Distance: {score:.4f}") 
        print("="*30)

    except Exception as e:
        print(f"⚠️ An error occurred during scanning: {e}")

if __name__ == "__main__":
    run_shadowproof()