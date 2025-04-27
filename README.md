# M4A to MP3 Converter

![Python](https://img.shields.io/badge/language-python-blue)
![License](https://img.shields.io/badge/license-MIT-green)

This project provides a simple Python script to convert `.m4a` audio files into `.mp3` format using `pydub` and `ffmpeg`.

---

## Requirements

- Python 3.x
- `pydub` library
- `ffmpeg` installed on your system

---

## Setup Instructions

### 1. Install `ffmpeg`

You have two options:

#### Option 1: Download Manually

- Visit the official ffmpeg website: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- Download the **Essentials Build** for your operating system.
- Extract the archive and locate the `bin/` folder containing `ffmpeg.exe` and `ffprobe.exe`.
- *(Optional)* Add the `bin/` folder to your system `PATH` to access `ffmpeg` globally.

#### Option 2: Install via Winget (Windows)

If you are on Windows, you can install `ffmpeg` easily using:

```bash
winget install "FFmpeg (Essentials Build)"
```

### 2. Restart your Computer

After installing ffmpeg, restart your **terminal** or **Command Prompt** to update environment variables.
If ffmpeg is still not recognized, restart your computer once.

You can check if ffmpeg is properly installed with the following command:

```bash
ffmpeg -version
```

### 3. How to Run the Script
- Place your .m4a files inside the './Files/m4a' folder
- Run the script:

```bash
python convert_m4a_to_mp3.py
```

- The converted .mp3 files will appear in the './Files/mp3' folder.

### 4. Troubleshooting

Some .m4a files are not true .m4a containers but are raw AAC audio files mislabeled with a .m4a extension.
If you got an error, simply change this line:

```bash
audio = AudioSegment.from_file(m4a_path, format='m4a')
```
to this:

```bash
audio = AudioSegment.from_file(m4a_path, format='aac')
```

