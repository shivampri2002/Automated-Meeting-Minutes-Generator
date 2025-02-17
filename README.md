# 🎙️ FastAPI Audio & Text Summarizer

A powerful FastAPI-based application that transcribes audio into text and summarizes both audio transcripts and raw text using the Gemini API. This project ensures efficient processing, user-friendly API endpoints, and seamless integration with a Streamlit frontend.

## 🌐 Live Demo
🔗 **Live Site URL:** [[https://automated-meeting-minutes-generator.streamlit.app/](https://automated-meeting-minutes-generator.streamlit.app/)]

![image](https://github.com/user-attachments/assets/29b4c84b-7949-48e8-b1b2-c85845ea0733)
![image](https://github.com/user-attachments/assets/04b32830-eb6d-4ca1-a6cc-134602c0cf9f)
![image](https://github.com/user-attachments/assets/142f48c1-b2b2-4a58-9366-d4d4e61eb5e8)
![image](https://github.com/user-attachments/assets/4073f353-6608-4ee3-b6fb-819f3b14d6de)



---

## 🚀 Features
- 📜 **Transcribe Audio**: Convert MP3/WAV files into text using Whisper AI.
- ✂️ **Summarize Text**: Use the Gemini API to generate concise summaries.
- 🎙️ **Transcribe & Summarize**: Automatically process and summarize audio in one step.
- ✅ **File Validation**: Supports only MP3 & WAV formats, and enforces a 10MB & 5-minute limit.
- 📡 **FastAPI Backend**: Efficient & scalable backend built with FastAPI & Uvicorn.
- 💻 **Streamlit Frontend**: A clean and intuitive UI for interacting with the API.

---

## 📁 Project Structure
```
📂 FastAPI-Audio-Summarizer
│── 📂 backend
│   ├── main.py  # FastAPI server implementation
│   ├── requirements.txt  # Python dependencies
│   ├── .env  # API Keys (excluded in .gitignore)
│── 📂 frontend
│   ├── app.py  # Streamlit frontend
│   ├── requirements.txt  # Dependencies for frontend
│── .gitignore
│── README.md
```

---

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone [https://github.com/shivampri2002/Automated-Meeting-Minutes-Generator.git](https://github.com/shivampri2002/Automated-Meeting-Minutes-Generator.git)
cd Automated-Meeting-Minutes-Generator
```
### 2️⃣ Set Up Backend (FastAPI)
```sh
cd backend
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3️⃣ Set Up Frontend (Streamlit)
```sh
cd ../frontend
pip install -r requirements.txt
```

---

## 🏃 Running the Application
### Start the FastAPI Server
```sh
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```
### Start the Streamlit Frontend
```sh
cd frontend
streamlit run app.py
```

---

## 🔌 API Endpoints
### 🎤 **Transcribe Audio**
- **POST** `/transcribe/`
- **Request**: Upload an `mp3/wav` file.
- **Response**:
```json
{
  "transcript": "This is the transcribed text."
}
```

### ✍️ **Summarize Text**
- **POST** `/summarize/`
- **Request**:
```json
{
  "text": "This is a long paragraph that needs summarization."
}
```
- **Response**:
```json
{
  "summary": "This is a summary."
}
```

### 🔄 **Transcribe & Summarize**
- **POST** `/transcribe_and_summarize/`
- **Request**: Upload an `mp3/wav` file.
- **Response**:
```json
{
  "transcript": "Full transcript here.",
  "summary": "Summarized version here."
}
```

---

## ☁️ Deployment on Render
1. Push your code to GitHub.
2. Create a **New Web Service** on [Render](https://render.com).
3. Set up the following:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4`
4. Add necessary **environment variables**.
5. Deploy and get your **Live API URL**.

---

## 🤝 Contributing
We welcome contributions! Feel free to fork this repository, submit pull requests, or report issues.

---

## 📜 License
This project is licensed under the MIT License.
