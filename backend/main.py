import os
import tempfile
from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import assemblyai as aai
import my_constants


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")


genai.configure(api_key=GEMINI_API_KEY)
aai.settings.api_key = ASSEMBLYAI_API_KEY

transcriber = aai.Transcriber()
model = genai.GenerativeModel("gemini-2.0-flash")


app = FastAPI(
    title="Automated Meeting Minute Generator Server",
    description="Server using Generative Ai",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class TextRequest(BaseModel):
    text: str


def transcribe_audio(file_path: str) -> str:
    """Transcribes audio using Whisper."""
    print(file_path)
    transcript = transcriber.transcribe(file_path)
    return transcript.text


def summarize_text(text: str) -> str:
    """Summarizes text using Gemini API."""
    # prompt = f"Summarize the following text:\n{text}"
    prompt = my_constants.GEMINI_PROMPT.format(text)
    response = model.generate_content(prompt)
    return response.text if response else "Summarization failed."


# def validate_audio(file: UploadFile):
#     """Validates that the audio file is within the length limit."""
#     if file.content_type not in ["audio/mpeg", "audio/wav"]:
#         raise HTTPException(status_code=400, detail="Unsupported audio format.")
#     # Save temporarily to check duration
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
#         temp_audio.write(file.file.read())
#         temp_audio_path = temp_audio.name
#     file_size_bytes = os.path.getsize(temp_audio_path)
#     file_size_mb = file_size_bytes / (1024 * 1024)
#     # os.remove(temp_audio_path)
#     if file_size_mb > 10:
#         raise HTTPException(status_code=400, detail="Audio file exceeds 10mb limit.")


# @app.post("/transcribe/")
# async def transcribe_audio_file(file: UploadFile = File(...)):
#     validate_audio(file)
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
#         temp_audio.write(file.file.read())
#         temp_audio_path = temp_audio.name
#     transcript = transcribe_audio(temp_audio_path)
#     os.remove(temp_audio_path)
#     return {"transcript": transcript}

def validate_audio(file: UploadFile):
    """Validates that the audio file is within the length and size limit."""
    if file.content_type not in ["audio/mpeg", "audio/wav"]:
        raise HTTPException(
            status_code=400, detail="Unsupported audio format.")

    temp_dir = os.path.join(tempfile.gettempdir(), "custom_ammg")
    os.makedirs(temp_dir, exist_ok=True)
    temp_audio_path = os.path.join(temp_dir, file.filename)

    with open(temp_audio_path, "wb") as temp_audio:
        temp_audio.write(file.file.read())

    file_size_bytes = os.path.getsize(temp_audio_path)
    file_size_mb = file_size_bytes / (1024 * 1024)

    if file_size_mb > 10:
        os.remove(temp_audio_path)
        raise HTTPException(
            status_code=400, detail="Audio file exceeds 10MB limit.")

    return temp_audio_path


@app.post("/transcribe/")
async def transcribe_audio_file(file: UploadFile = File(...)):
    temp_audio_path = validate_audio(file)
    transcript = transcribe_audio(temp_audio_path)
    os.remove(temp_audio_path)
    return {"transcript": transcript}


@app.post("/summarize/")
async def summarize_text_route(request: TextRequest):
    summary = summarize_text(request.text)
    return {"summary": summary}


@app.post("/transcribe_and_summarize/")
async def transcribe_and_summarize(file: UploadFile = File(...)):
    temp_audio_path = validate_audio(file)
    transcript = transcribe_audio(temp_audio_path)
    summary = summarize_text(transcript)
    os.remove(temp_audio_path)
    return {"transcript": transcript, "summary": summary}
