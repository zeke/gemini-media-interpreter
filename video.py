from google import genai
from google.genai import types
import os
from time import sleep
import sys
import argparse
from urllib.parse import urlparse

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY',None)
client = genai.Client(api_key=GEMINI_API_KEY)

parser = argparse.ArgumentParser(description="Analyze a video with Gemini")
parser.add_argument("video_path", help="Path to the video file or YouTube URL")
parser.add_argument("--prompt", type=str, default="prompt.md", help="Path to the prompt file (default: prompt.md)")
parser.add_argument("--model", type=str, default="gemini-2.5-flash-preview-05-20", help="Gemini model to use (default: gemini-2.5-flash-preview-05-20)")
args = parser.parse_args()

video_path = args.video_path
prompt_path = args.prompt
MODEL_ID = args.model

print(f"Using Gemini model: {MODEL_ID}")

def is_youtube_url(url):
    try:
        parsed = urlparse(url)
        return parsed.netloc in ["www.youtube.com", "youtube.com", "youtu.be"]
    except Exception:
        return False

if is_youtube_url(video_path):
    print(f"Using YouTube video: {video_path}")
    video_part = genai.types.Part(
        file_data=genai.types.FileData(file_uri=video_path)
    )
else:
    print(f"Uploading video: {video_path}")
    video_file_id = client.files.upload(file=video_path)

    def wait_for_file_ready(file_id):
        while file_id.state == "PROCESSING":
            sleep(0.2)
            file_id = client.files.get(name=file_id.name)
            print(".", file=sys.stderr, end="", flush=True)
            wait_for_file_ready(file_id)
        return file_id

    video_file_id = wait_for_file_ready(video_file_id)
    video_part = types.Part.from_uri(file_uri=video_file_id.uri, mime_type=video_file_id.mime_type)

with open(prompt_path, "r") as f:
    prompt = f.read()

print("\nAnalyzing video...")

try:
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[prompt, video_part]
    )
    print(response.text)
except Exception as e:
    import traceback
    print("\nAn error occurred:", file=sys.stderr)
    print(f"Type: {type(e)}", file=sys.stderr)
    print(f"Attributes: {e.__dict__}", file=sys.stderr)
    traceback.print_exc()
    print("\nFull error details:", file=sys.stderr)
    print(str(e), file=sys.stderr)