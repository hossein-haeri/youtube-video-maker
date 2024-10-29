
# Audio to Video Converter

This application converts audio files into video files by adding a fixed cover image. It is designed to create videos that can be uploaded to platforms like YouTube, where each video has a chosen resolution, a black background (if needed), and the audio playing along with a static image.

## Features
- Supports audio files (`.mp3`, `.wav`) and image files (`.png`, `.jpg`, `.jpeg`).
- Offers common video resolutions, including 1080p, 720p, 480p, and 360p.
- Automatically resizes the image to fit the chosen resolution, centering it with a black background if the aspect ratio differs.
- Shows a progress bar during conversion.

## Prerequisites
- **Python 3.7 or higher**
- **moviepy**: Library for video processing.
- **tkinter**: Library for the graphical interface (usually comes pre-installed with Python).

To install `moviepy`, run the following command:
```bash
pip install moviepy
```

### Additional Requirement: FFmpeg
The application requires **FFmpeg** to handle video and audio encoding. FFmpeg is free to download and install.

#### To Install FFmpeg:
1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
2. Follow the instructions to add FFmpeg to your system PATH so `moviepy` can access it.

## How to Run the Application

1. **Clone or download** this repository to your computer.
2. Open a terminal or command prompt in the project directory.
3. Run the following command:
   ```bash
   python youtube_video_maker.py
   ```

## How to Use the Application

1. **Select Audio Files**: Click the "Browse Audio Files" button and choose one or more audio files to convert.
2. **Select Cover Image**: Click the "Browse Cover Image" button and select an image to use as the video cover.
3. **Choose Output Directory**: Click "Browse Output Directory" to select where the videos should be saved.
4. **Select Resolution**: Use the dropdown menu to choose the desired video resolution (e.g., 1080p).
5. **Convert**: Click "Convert to Videos" to start the conversion process. The progress bar will show the current progress.

## Notes
- The created videos will have the same duration as the audio files.
- The videos are saved in `.mp4` format, suitable for YouTube and other video platforms.

---
**Created by Hossein Haeri**
