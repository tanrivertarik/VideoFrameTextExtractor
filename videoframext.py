import cv2
import pytesseract
import re
import os

# Configure Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def clean_text(text):
    """Clean text by removing invalid characters."""
    return re.sub(r'[<>:"/\\|?*]', '', text)

def extract_text_from_frame(frame):
    """Extract text from a given frame using OCR."""
    text = pytesseract.image_to_string(frame, config='--psm 6')
    return text.strip()

def extract_target_text(text):
    """Extract target text from the given text based on a specific pattern."""
    match = re.search(r'urun-detay/(\d+)', text)
    if match:
        return match.group(1)
    return None

def extract_text_from_video(video_path):
    """Extract target text from the last 5 seconds of a video."""
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    duration = length / fps

    # Move to the last 5 seconds of the video
    time_to_set = (duration - 5) * 1000
    if time_to_set < 0:
        time_to_set = 0

    cap.set(cv2.CAP_PROP_POS_MSEC, time_to_set)
    ret, frame = cap.read()
    if not ret:
        print(f"Failed to read video: {video_path}")
        return None

    # Extract text from the entire frame
    h, w, _ = frame.shape
    cropped_frame = frame[int(h*0.0):int(h*1.0), int(w*0.0):int(w*1.0)]

    # Extract text from the cropped frame
    text = extract_text_from_frame(cropped_frame)
    
    # Debug: Print detected text
    print(f"Detected text: {text}")

    # Extract target text from the detected text
    target_text = extract_target_text(text)
    
    print(f"Extracted target text: '{target_text}' from video: {video_path}")

    cap.release()
    return target_text

def rename_videos_in_directory(directory):
    """Rename videos in the given directory based on extracted text."""
    for filename in os.listdir(directory):
        if filename.endswith(".mp4"):
            video_path = os.path.join(directory, filename)
            target_text = extract_text_from_video(video_path)
            if target_text:
                new_filename = f"{target_text}.mp4"
                new_path = os.path.join(directory, new_filename)
                try:
                    os.rename(video_path, new_path)
                    print(f"Renamed: {filename} to {new_filename}")
                except OSError as e:
                    print(f"Error renaming {filename} to {new_filename}: {e}")

# Execute the script
video_directory = r"C:\videos"  # Specify the directory containing the videos
rename_videos_in_directory(video_directory)
