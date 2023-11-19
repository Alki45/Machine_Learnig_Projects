import cv2  # Importing the OpenCV library
import cvlib as cv  # Importing the cvlib library for computer vision
from cvlib.object_detection import draw_bbox  # Importing the draw_bbox function for drawing bounding boxes

# Constants for distance calculation
KNOWN_WIDTH = 0.2  # Width of the object in meters (assuming known)
FOCAL_LENGTH = 500  # Focal length of the camera in pixels (assuming known)

video = cv2.VideoCapture(cv2.CAP_ANY)  # Initializing video capture from any available camera

while True:
    ret, frame = video.read()  # Reading a frame from the video capture

    if not ret:
        break  # Break the loop if no frame is captured

    bbox, label, conf = cv.detect_common_objects(frame)  # Detecting common objects in the frame
    output_image = draw_bbox(frame, bbox, label, conf)  # Drawing bounding boxes on the frame

    obstacle_detected = False
    obstacle_labels = ["person", "car", "chair"]  # Labels for specific obstacles

    for i, obstacle_label in enumerate(obstacle_labels):
        if obstacle_label in label:
            obstacle_detected = True
            print("Obstacle detected:", obstacle_label)

            # Confidence of the detected object
            confidence = conf[i]
            print("Confidence:", confidence * 100)

            # Distance calculation
            object_width = (
                    (bbox[i][2] - bbox[i][0]) + (bbox[i][3] - bbox[i][1])
            ) / ((bbox[i][0] + bbox[i][2] + bbox[i][3] + bbox[i][1]))  # Calculate width using the bounding box coordinates
            if object_width == 0:
                object_width = 1
            distance = (FOCAL_LENGTH) / object_width
            print("Distance (meters):", distance, bbox)
            print(bbox[i][0], bbox[i][1], bbox[i][2], bbox[i][3])

            # Side Of Obstacle
            x, y, w, h = bbox[i]
            frame_width = frame.shape[1]
            if x + w / 2 < frame_width / 2:
                obstacle_side = "Left"
            elif x + w / 2 > frame_width / 2:
                obstacle_side = "Right"
            else:
                obstacle_side = "Center"
            print("Obstacle side:", obstacle_side)

            # Perform specific actions based on obstacle type
            if obstacle_label == "person":
                print("Taking action for person obstacle...")
                # Implement your action here
            elif obstacle_label == "car":
                print("Taking action for car obstacle...")
                # Implement your action here
            elif obstacle_label == "chair":
                print("Taking action for chair obstacle...")
                # Implement your action here

            break

    cv2.imshow("Object Detection", output_image)  # Display the output frame with bounding boxes

    if cv2.waitKey(1) & 0xFF == ord("S"):
        break  # Break the loop if the "S" key is pressed

video.release()  # Release the video capture resources
cv2.destroyAllWindows()  # Close all OpenCV windows