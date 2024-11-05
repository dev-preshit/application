import cv2
import face_recognition
import os
import csv
from datetime import datetime

# Load known face encodings and their names
known_face_encodings = []
known_face_names = []

# Load images from the database folder
database_folder = 'D:/git/faces'
for filename in os.listdir(database_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(database_folder, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        name = os.path.splitext(filename)[0]  # Use the filename (without extension) as the name
        known_face_names.append(name)

# Initialize video capture
cam_on = cv2.VideoCapture(0)

# CSV file setup
with open('recognition_log.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Time"])

    while True:
        check_f, video = cam_on.read()
        if not check_f:
            print("Something went wrong")
            break

        # Convert the frame from BGR to RGB for face_recognition
        rgb_frame = cv2.cvtColor(video, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Compare the detected face with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match is found, get the name
            if True in matches:
                match_index = matches.index(True)
                name = known_face_names[match_index]

                # Log the name and timestamp
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([name, current_time])

            # Draw a box around the face and label it
            top, right, bottom, left = face_location
            cv2.rectangle(video, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(video, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display the video frame
        cv2.imshow("Camera", video)

        if cv2.waitKey(1) == ord("a"):
            break

# Release resources
cam_on.release()
cv2.destroyAllWindows()
