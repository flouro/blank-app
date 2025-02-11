import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(page_title="A Special Question", page_icon="❤️")  # Moved to top


def heart_shape():
    # Heart shape coordinates
    t = np.linspace(0, 2 * np.pi, 20)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    st.write("### 🤎 A Heart Full of Memories 🤎")

    images = ["photo_10_2025-02-11_18-27-25.jpg",
    "photo_11_2025-02-11_18-27-25.jpg",
    "photo_9_2025-02-11_18-27-25.jpg",
    "photo_8_2025-02-11_18-27-25.jpg",
    "photo_7_2025-02-11_18-27-25.jpg",
    "photo_6_2025-02-11_18-27-25.jpg",
    "photo_5_2025-02-11_18-27-25.jpg",
    "photo_4_2025-02-11_18-27-25.jpg",
    "photo_3_2025-02-11_18-27-25.jpg",
    "photo_2_2025-02-11_18-27-25.jpg",
    "photo_1_2025-02-11_18-27-25.jpg",
    "image.png",
    "image copy.png",
    "image copy 2.png","photo_8_2025-02-11_18-46-54.jpg",
    "photo_9_2025-02-11_18-46-54.jpg", 
    "photo_2_2025-02-11_18-46-54.jpg", 
    "photo_3_2025-02-11_18-46-54.jpg", 
    "photo_4_2025-02-11_18-46-54.jpg", 
    "photo_5_2025-02-11_18-46-54.jpg", 
    "photo_6_2025-02-11_18-46-54.jpg", 
    "photo_7_2025-02-11_18-46-54.jpg", 
    "photo_11_2025-02-11_18-46-54.jpg",
    "photo_12_2025-02-11_18-46-54.jpg", 
    "photo_10_2025-02-11_18-46-54.jpg"]
    img_count = len(images)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 15)
    ax.axis("off")

    for i in range(len(x)):
        img_index = i % img_count
        img = Image.open(images[img_index])

        # Resize image
        img = img.resize((50, 50))

        # Place images at heart coordinates
        ax.imshow(img, extent=[x[i]-2, x[i]+2, y[i]-2, y[i]+2], aspect='auto')

    st.pyplot(fig)

def main():
    if "verified" not in st.session_state:
        st.session_state.verified = False
    if "yes_clicked" not in st.session_state:
        st.session_state.yes_clicked = False
    
    if not st.session_state.verified:
        st.title("🔒 Mailys Check")
        st.write("Please enter your birthday to proceed.")
        
        day = st.selectbox("Day", [str(i).zfill(2) for i in range(1, 32)])
        month = st.selectbox("Month", [str(i).zfill(2) for i in range(1, 13)])
        year = st.selectbox("Year", [str(i) for i in range(1990, 2025)])
        
        if st.button("Submit"):
            if day == "14" and month == "12" and year == "2005":
                st.session_state.verified = True
            else:
                st.error("Oops! Wrong birthday. Try again.")
    elif not st.session_state.yes_clicked:
        st.title("🤎 Will You Be My Valentine? 🤎")
        st.image("picture1.jpg", use_column_width=True)
        st.write("You’ve unlocked this special message just for you! 🌹")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💖 Yes! 💕", key="yes", help="Say yes!"):
                st.session_state.yes_clicked = True
        with col2:
            if st.button("🤔 Maybe...", key="maybe", help="Think about it!"):
                st.warning("I’ll wait for your answer! 😘")
    else:
        st.title("Yeaaa! 🤎")
        heart_shape()
       

if __name__ == "__main__":
    main()
