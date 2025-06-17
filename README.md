# 🍿 Gemini media interpreter

This is a simple Python script that uses Google's Gemini API to extract data from video and audio files.

Cobbled together at [AI Engineer World's Fair 2025](https://www.ai.engineer/), using code from [this workshop](https://github.com/philschmid/gemini-2.5-ai-engineering-workshop) by [@philschmid](https://github.com/philschmid). 🙏

---

It can interpret:

- Audio files on your computer
- Video files on your computer
- YouTube videos

---

It generates:

- A title 
- A TLDR
- A one-paragraph summary
- A table of contents
- A transcript
- A cleaned-up transcript

## Usage

Get a Google Gemini API key at [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

Set the `GEMINI_API_KEY` environment variable:

```sh
export GEMINI_API_KEY=YOUR_API_KEY
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run the script:

```sh
python video.py <video_path_or_youtube_url>
```

You can provide either a path to a local audio or video file or a YouTube URL as the first argument.

By default, the script uses the prompt in `prompt.md`. You can specify a custom prompt file with the `--prompt` flag:

```sh
python video.py <video_path_or_youtube_url> --prompt custom_prompt.md
```

You can also specify which Gemini model to use with the `--model` flag (default: `gemini-2.5-flash-preview-05-20`):

```sh
python video.py <video_path_or_youtube_url> --model gemini-2.5-pro-preview-06-05
```

See the list of available models here: [Gemini API Models](https://ai.google.dev/gemini-api/docs/models)

## Examples

Analyze a local audio file (mp3, m4a, etc):

```sh
python video.py sample.m4a
```

Analyze a local video file (mp4, mov, etc):

```sh
python video.py sample.mov
```

Analyze a YouTube video directly by URL:

```sh
python video.py "https://www.youtube.com/watch?v=dwgmfSOZNoQ"
```

## Example output

```
## Title

*   Extracting video metadata: an initial problem.
*   A brief introduction to video metadata challenges.
*   Understanding metadata loss in video uploads.

## TLDR

*   Learn about metadata loss when uploading videos.
*   Discover issues preserving video effects online.
*   Identify challenges in video metadata retention.

## One-paragraph summary

This video provides a brief, introductory look into the concept of extracting video metadata. The speaker shares his experience recording a video for his team using OBS, an open-source software, to add various visual enhancements like a green screen. He then highlights a common challenge: when these videos are uploaded to platforms like Loom, the added visual "bells and whistles" (metadata) often fail to transfer. This short clip effectively sets the stage by introducing the problem of metadata degradation in video sharing, signaling the speaker's intention to explore solutions for extraction and preservation.

This video serves as an initial segment, introducing the topic of video metadata extraction by illustrating a practical problem. The speaker explains how he utilized OBS to create a video with specific visual effects, but found that upon uploading it to Loom, these enhancements were lost. Viewers can gain an understanding of the common issue where valuable visual metadata isn't retained across different platforms, highlighting the need for methods to extract and manage such information effectively.

In this short introductory video, the presenter discusses the upcoming topic of extracting video metadata. He recounts how he created a video using OBS to incorporate advanced visual elements like a green screen. The main point conveyed is that when this video was subsequently uploaded to Loom, the specific visual metadata he had added was not preserved. This segment therefore clarifies a key challenge in video content management: ensuring that embedded information and visual effects remain intact when shared across different video platforms.

## TOC

0:00 Introduction to video metadata extraction
0:07 Recording videos with OBS with special effects
0:29 The problem of metadata loss on video platforms
0:44 Speaker restarts video

## Transcript

Hey all you cool cats and kittens, I want to show you how to extract metadata from videos. So today, earlier today, I recorded this video for the team about our client libraries bake-off. And I wanted to add some bells and whistles to it using a green screen and stuff, so I used a product called OBS, which is an open source, uh, piece of software that you install on your Mac for recording. Um, so that's cool. But the thing that's not cool is when I upload that video to Fern, which is the sort of, uh, website that we use to share videos. You don't get any of the cool, um, bells and whistles that come with Fern. Or, did I say Fern? I meant Loom. I'm going to start over.

## Clean transcript

Hey all you cool cats and kittens, I want to show you how to extract metadata from videos. Earlier today, I recorded this video for the team about our client libraries bake-off. I added bells and whistles using a green screen. I used OBS, an open-source software you install on your Mac for recording. That's cool. The thing that's not cool is when I upload that video to Loom, the website we use to share videos, you don't get any of the cool bells and whistles that come with Loom. I meant Loom. I'm going to start over.