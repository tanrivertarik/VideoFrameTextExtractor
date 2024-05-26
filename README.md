# VideoFrameTextExtractor

VideoFrameTextExtractor is a Python script designed to extract text from the last 5 seconds of a video and rename the video based on the extracted text. This script uses OpenCV for video processing and Tesseract OCR for text recognition.

## Features

- Extracts text from the last 5 seconds of a video.
- Renames the video file based on the extracted text.
- Configurable to extract specific patterns from the text.

## Requirements

- Python 3.x
- OpenCV
- Tesseract OCR
- pytesseract

## Installation

1. Install the required Python packages:
    ```bash
    pip install opencv-python pytesseract
    ```

2. Install Tesseract OCR:
    - [Windows](https://github.com/tesseract-ocr/tesseract#windows)
    - [macOS](https://github.com/tesseract-ocr/tesseract#macos)
    - [Linux](https://github.com/tesseract-ocr/tesseract#linux)

3. Configure the Tesseract executable path in the script:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

## Usage

1. Place your videos in a directory, e.g., `C:\videos`.
2. Modify the `video_directory` variable in the script to point to your directory.
3. Run the script:
    ```bash
    python VideoFrameTextExtractor.py
    ```

The script will process each `.mp4` video in the directory, extract the relevant text, and rename the video file accordingly.

## Note

This script can be adapted for various purposes where extracting and utilizing specific text from video frames is required.

## License

This project is licensed under the MIT License.
