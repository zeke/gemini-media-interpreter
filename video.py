from google import genai
from google.genai import types
import os
from time import sleep
import sys
import argparse

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY',None)
MODEL_ID = "gemini-2.5-flash-preview-05-20"
client = genai.Client(api_key=GEMINI_API_KEY)

parser = argparse.ArgumentParser(description="Analyze a video with Gemini")
parser.add_argument("video_path", help="Path to the video file")
parser.add_argument("--prompt", type=str, default="prompt.md", help="Path to the prompt file (default: prompt.md)")
args = parser.parse_args()

video_path = args.video_path
prompt_path = args.prompt

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

with open(prompt_path, "r") as f:
    prompt = f.read()

print("\nAnalyzing video...")
video_part = types.Part.from_uri(file_uri=video_file_id.uri, mime_type=video_file_id.mime_type)

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[prompt, video_part]
)

print(response.text)