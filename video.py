from google import genai
from google.genai import types
import os
from time import sleep
import sys

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY',None)
MODEL_ID = "gemini-2.5-flash-preview-05-20"
client = genai.Client(api_key=GEMINI_API_KEY)

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <video_path>", file=sys.stderr)
    sys.exit(1)
video_path = sys.argv[1]

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


prompt = """
    Generate a markdown summary of the following video.

    Create the following sections, each with an H2 heading:

    - Title: A sentence-case title for the video
        - Use "Sentence case", not "Title case".
        - Write 3 of these.
    
    - TLDR: A very short summary of the video.
        - Write it in a way that explains what this video will teach you to do.
        - 10 words or less.
        - Write 3 of these.

    - One-paragraph summary:
        - Just a few sentences.
        - Write 3 of these.
        - Explain what can be learned or gained from the video.

    - TOC: A YouTube-style table of contents with timestamps.
        Example:
        0:00 Creating a Snake object
        3:00 Adding keyboard control
        5:20 Grid and world constraints

    - Transcript: A verbatim transcript of the video. Do not include timestamps.

    - Clean transcript: A cleaned-up transcript of the video
        - Remove filler words and non-essential words.
        - Proper nouns and product names should be capitalized.

"""

print("\nAnalyzing video...")
video_part = types.Part.from_uri(file_uri=video_file_id.uri, mime_type=video_file_id.mime_type)

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[prompt, video_part]
)

print(response.text)