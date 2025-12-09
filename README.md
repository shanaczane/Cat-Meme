# Cat Mood Cam

A fun real-time facial expression detector that mirrors your emotions with adorable cat memes! Using your webcam and MediaPipe face detection, this app displays different cat expressions based on your facial movements.

## Features

- **Expression Detection**: Uses MediaPipe Face Mesh for accurate facial landmark tracking
- **7 Different Cat Expressions**:
  - Default (neutral)
  - Shock (mouth open)
  - Wink (one eye closed)
  - Tongue (tongue out)
  - Angry (furrowed eyebrows)
  - Awkward (polite cat smile)
  - Happy (big smile)
- **Side-by-Side View**: See yourself and the cat reaction simultaneously

## Technologies Used

- Python 3.x
- OpenCV (cv2)
- MediaPipe
- NumPy

## Requirements
```bash
pip install opencv-python mediapipe numpy
```

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/shanaczane/Cat-Meme.git
cd Cat-Meme
```

2. Make sure you have the cat images in an `images/` folder:
   - default.jpg
   - shock.jpg
   - wink.jpg
   - tongue.jpg
   - angry.jpg
   - awkward.jpg
   - happy.jpg

3. Run the program:
```bash
python main.py
```

4. Press `ESC` to exit
