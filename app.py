import streamlit as st
import os
def load_css():
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -----------------------------
# Import Reader Functions
# -----------------------------
from utils.pdf_reader import read_pdf
from utils.doc_reader import read_docx
from utils.txt_reader import read_txt

# -----------------------------
# Import Prompts
# -----------------------------
from utils.prompts import ALL_NOTES_PROMPT

# -----------------------------
# Import Gemini Functions
# -----------------------------
import utils.ai_generator as ai

print("MODULE:", ai)
print("FILE:", ai.__file__)
print("DIR:", dir(ai))

generate_study_notes = ai.generate_study_notes
import sys
import os

print("=" * 60)
print("Python Executable:", sys.executable)
print("Current Directory:", os.getcwd())
print("=" * 60)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Study Notes Generator",
    page_icon="📚",
    layout="wide"
)
with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/artificial-intelligence.png",
        width=90
    )

    st.title("📚 AI Study Notes")

    st.caption("Smart Learning Assistant")

    st.markdown("---")

    st.subheader("✨ Features")

    st.success("📄 PDF Reader")
    st.success("📘 DOCX Reader")
    st.success("📃 TXT Reader")
    st.success("🤖 AI Summary")
    st.success("📝 Key Points")
    st.success("🎯 Flashcards")
    st.success("❓ Quiz Generator")

    st.markdown("---")

    st.subheader("👨‍💻 Tech Stack")

    st.write("🐍 Python")
    st.write("⚡ Streamlit")
    st.write("🤖 Google Gemini AI")
    st.write("📄 PyPDF2")
    st.write("📘 python-docx")

    st.markdown("---")

    

# -----------------------------
# Title
# -----------------------------
st.markdown("""
# 📚 AI Study Notes Generator

### 🤖 Smart AI Assistant for Students

Generate **Summary • Key Points • Flashcards • Quiz**

Upload your notes and let AI prepare your study material in seconds.
""")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📚 Upload Notes")

with col2:
    st.info("🤖 AI Processing")

with col3:
    st.info("📥 Download Results")

st.markdown("---")

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Study Material",
    type=["pdf", "docx", "txt"]
)

# -----------------------------
# If File Uploaded
# -----------------------------
if uploaded_file is not None:

    st.success("✅ File Uploaded Successfully!")

    # -----------------------------
    # File Information
    # -----------------------------
    st.markdown("## 📁 File Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(f"**📄 File Name**\n\n{uploaded_file.name}")

    with col2:
        st.info(f"**📦 File Type**\n\n{uploaded_file.type}")

    with col3:
        size = round(uploaded_file.size / 1024, 2)
        st.info(f"**📏 File Size**\n\n{size} KB")

    # -----------------------------
    # Create Upload Folder
    # -----------------------------
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    # Save Uploaded File
    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # -----------------------------
    # Read Uploaded File
    # -----------------------------
    extension = uploaded_file.name.split(".")[-1].lower()

    document_text = ""

    try:

        if extension == "pdf":
            document_text = read_pdf(file_path)

        elif extension == "docx":
            document_text = read_docx(file_path)

        elif extension == "txt":
            document_text = read_txt(file_path)

        else:
            st.error("❌ Unsupported File Format")

    except Exception as e:
        st.error(f"Error Reading File: {e}")

    # -----------------------------
    # Preview Document
    # -----------------------------
    if document_text:

        st.markdown("---")

        st.subheader("📄 Extracted Text")

        with st.expander("📄 Preview Uploaded Document", expanded=False):

            st.text_area(
        "",
        document_text,
        height=350
    )

        st.success("Document Read Successfully!")

        st.markdown("---")

        # -----------------------------
        # Generate Notes Button
        # -----------------------------
        st.markdown("## 🤖 AI Processing")

        if st.button("✨ Generate Study Notes"):

            progress = st.progress(0)

            status = st.empty()

            status.text("📄 Reading Document...")

            progress.progress(20)

            status.text("🤖 Connecting to Gemini AI...")

            progress.progress(40)

            status.text("📝 Generating Summary...")

            progress.progress(60)

            with st.spinner("Generating Study Notes..."):

                # Your AI code remains here
                # Create Prompts
                study_prompt = ALL_NOTES_PROMPT.format(
                document=document_text
                )

                # Generate AI Results
                study_notes = generate_study_notes(study_prompt)
                progress.progress(100)

                status.text("✅ Generation Completed")

            st.success("🎉 Study Notes Generated Successfully!")
            # ---------------------------------------
            # Document Statistics
            # ---------------------------------------

            word_count = len(document_text.split())

            char_count = len(document_text)

            line_count = len(document_text.splitlines())

            st.markdown("## 📊 Document Statistics")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("📄 Words", word_count)

            with col2:
                st.metric("🔤 Characters", char_count)

            with col3:
                st.metric("📑 Lines", line_count)

            st.markdown("---")
            st.markdown("---")

            # -----------------------------
            # Display Summary
            # -----------------------------
            # -----------------------------
            # Display Results in Tabs
            # -----------------------------

            st.markdown("## 📚 Generated Study Notes")

            st.markdown(study_notes)

            # -----------------------------
            # Combine All Notes
            # -----------------------------
            notes = study_notes


            # -----------------------------
            # Create generated_notes Folder
            # -----------------------------
            if not os.path.exists("generated_notes"):
                os.makedirs("generated_notes")

            # -----------------------------
            # Save Notes
            # -----------------------------
            output_filename = (
                os.path.splitext(uploaded_file.name)[0]
                + "_notes.txt"
            )

            output_path = os.path.join(
                "generated_notes",
                output_filename
            )

            with open(output_path, "w", encoding="utf-8") as file:
                file.write(notes)

            st.success("✅ Notes Saved Successfully!")
            st.markdown("---")

            st.subheader("📥 Export Your Study Notes")

            st.write(
                "Download the generated study notes and use them for revision anytime."
            )

            st.info(f"Saved File: generated_notes/{output_filename}")

            # -----------------------------
            # Download Button
            # -----------------------------
            st.download_button(
                label="📥 Download Study Notes",
                data=notes,
                file_name=output_filename,
                mime="text/plain"
            )

    else:
        st.warning("⚠️ No text could be extracted from the uploaded document.")
        
    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center;color:gray;">
            <h4>📚 AI Study Notes Generator</h4>
            <p>Developed using Python • Streamlit • Google Gemini AI</p>
        </div>
        """,
        unsafe_allow_html=True
    )
