# 📚 AI Study Notes Generator

An AI-powered application that converts study materials into easy-to-understand study notes using Google Gemini AI.

---

## 🚀 Features

- 📄 Read PDF files
- 📘 Read DOCX files
- 📃 Read TXT files
- 🤖 Generate AI Summary
- 📝 Extract Key Points
- 🎯 Generate Flashcards
- ❓ Generate Quiz Questions
- 📥 Download Study Notes

---

## 🛠 Technologies Used

- Python
- Streamlit
- Google Gemini AI
- PyPDF2
- python-docx
- python-dotenv

---

## 📂 Project Structure

```
AI-Study-Notes-Generator/
│
├── assets/
│   └── style.css
│
├── utils/
│   ├── ai_generator.py
│   ├── pdf_reader.py
│   ├── doc_reader.py
│   ├── txt_reader.py
│   └── prompts.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/SaiNikhithaGudla/AI-Study-Notes-Generator.git
```

Move into the project folder

```bash
cd AI-Study-Notes-Generator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Screenshots will be added soon.

---

## 📈 Future Improvements

- PDF Export
- Dark Mode
- Multiple Language Support
- Chat with Notes
- Voice Support

---

## 👩‍💻 Developer

Sai Nikhitha Gudla
