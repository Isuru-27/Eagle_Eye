import cv2
import face_recognition

# Load the reference image for comparison
reference_img = cv2.imread("p2.jpg")
reference_rgb_img = cv2.cvtColor(reference_img, cv2.COLOR_BGR2RGB)
reference_encoding = face_recognition.face_encodings(reference_rgb_img)[0]

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to RGB for face recognition
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find face locations in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    
    if face_locations:
        # Encode the face in the frame
        frame_encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]

        # Compare the face encoding with the reference encoding
        result = face_recognition.compare_faces([reference_encoding], frame_encoding)

        # Print the result
        print("Result: ", result)

        # Draw rectangles around detected faces in the frame
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        
        # Display match result as text
        if result[0]:
            cv2.putText(frame, "Face Match", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Face Not Match", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
