import streamlit as st
from storygenerator import generate_story_from_images
from PIL import Image


st.title("AI story generator from images")
st.markdown("Upload 1 to 10 images,choose an style and let AI write and narrate an story for you.")

with st.sidebar:
    st.header("Controls")   

    # Sidebar option to upload images
    uploaded_files= st.file_uploader(
        "Upload  your images...",
        type=["png","jpg","jpeg"],
        accept_multiple_files=True
    )

    #selecting an story style   
    story_style= st.selectbox(  
        "choose a story style",
        ("Comedy", "Thriller", "Fairy Tale", "Sci-Fi", "Mystery")
    )


    # Button to generate story
    generate_button = st.button("Generate Story and Narration", type="primary")

# MAIN LOGIC
if generate_button:
    if not uploaded_files:
        st.warning("Please upload atlest 1 image.")
    elif len(uploaded_files)>10:
        st.warning("Please upload an maximum of 10 images.")
    else:
        with st.spinner("The AI is writing  and narrating your story..... This may take few moments."):
            try:
                pil_images= [Image.open(uploaded_file) for uploaded_file in  uploaded_files]
                st.subheader("Your visual Inspiration:")
                image_columns= st.columns(len(pil_images))

                for i ,image in enumerate(pil_images):
                    with image_columns[i]:
                        st.image(image, use_container_width=True)

                generate_story = generate_story_from_images(pil_images, story_style)
                generate_story= generate_story_from_images(pil_images, story_style)
                if "Error" in generate_story or "failed" in generate_story or"API key" in generate_story:
                    st.error(generate_story)
                else:
                    st.subheader(f"Your {story_style} story: ")
                    st.success(generate_story)

            except Exception as e:
               st.error(f"An application error occurred {e}")
