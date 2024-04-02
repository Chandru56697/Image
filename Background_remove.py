import streamlit as st
from PIL import Image
from rembg import remove

def remove_background(image):
    try:
        img = Image.open(image)
        st.image(img, caption="Uploaded Image", use_column_width=True)
        st.write("Processing...")

        # Remove background
        result = remove(img)

        # Display result
        st.image(result, caption="Background Removed", use_column_width=True)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def main():
    st.title("Background Remover App")
    st.write("Upload an image and I'll remove the background for you!")

    # File uploader
    file = st.file_uploader("Choose image...", type=["jpg", "png", "jpeg","webp"])

    if file is not None:
        remove_background(file)

if __name__ == '__main__':
    main()
    
    