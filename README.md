# Real-time Face Recognition with OpenCV and Face Recognition Library(# Eagle_Eye)

This Python script demonstrates real-time face recognition using OpenCV and the Face Recognition library. It compares the face captured from a webcam feed with a reference image loaded from a file.

## Prerequisites

Make sure you have the following libraries installed:

- OpenCV (`pip install opencv-python`)
- Face Recognition (`pip install face_recognition`)

## Usage

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the directory:

    ```bash
    cd <repository-folder>
    ```

3. Run the Python script:

    ```bash
    python face_recognition.py
    ```

4. A window will open showing the webcam feed. When a face is detected, the script will compare it with the reference image. If a match is found, it will display "Face Match" in green text; otherwise, it will display "Face Not Match" in red text.

## Notes

- The reference image for comparison should be named `p2.jpg` and placed in the same directory as the script.
- Press the 'q' key to exit the script.

## Author

[Your Name](https://github.com/Isuru-27)

