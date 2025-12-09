import cv2
import mediapipe as mp
import numpy as np

# Cat Images
cat_default = cv2.imread("images/default.jpg")
cat_shock = cv2.imread("images/shock.jpg")
cat_wink = cv2.imread("images/wink.jpg")
cat_tongue = cv2.imread("images/tongue.jpg")
cat_angry = cv2.imread("images/angry.jpg")
cat_awkward = cv2.imread("images/awkward.jpg")
cat_happy = cv2.imread("images/happy.jpg")

# Resize cat images once
def resize_img(img, size=(480, 480)):
    return cv2.resize(img, size)

cat_default = resize_img(cat_default)
cat_shock = resize_img(cat_shock)
cat_wink = resize_img(cat_wink)
cat_tongue = resize_img(cat_tongue)
cat_angry = resize_img(cat_angry)
cat_awkward = resize_img(cat_awkward)
cat_happy = resize_img(cat_happy)

# Initialize Face Mesh
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

def get_expression(landmarks):
    # Mouth Landmarks
    upper_lip = landmarks[13]
    lower_lip = landmarks[15]
    left_mouth = landmarks[61]
    right_mouth = landmarks[291]

    mouth_height = abs(upper_lip.y - lower_lip.y)
    mouth_width = abs(left_mouth.x - right_mouth.x)

    # Eye Landmarks
    left_eye_top = landmarks[159]
    left_eye_bottom = landmarks[145]
    left_eye_open = abs(left_eye_top.y - left_eye_bottom.y)

    right_eye_top = landmarks[386]
    right_eye_bottom = landmarks[374]
    right_eye_open = abs(right_eye_top.y - right_eye_bottom.y)

    # Eyebrow Landmarks
    left_eyebrow = landmarks[70]
    right_eyebrow = landmarks[300]
    left_eye_inner = landmarks[133]
    right_eye_inner = landmarks[362]
    
    left_brow_distance = abs(left_eyebrow.y - left_eye_inner.y)
    right_brow_distance = abs(right_eyebrow.y - right_eye_inner.y)
    
    if left_brow_distance < 0.035 and right_brow_distance < 0.035:
        return "angry"
    if mouth_width > 0.15 and mouth_height < 0.015:
        return "awkward"
    if mouth_height > 0.02 and mouth_width > 0.12:
        return "happy"
    if mouth_height > 0.04 and mouth_height > mouth_width * 0.4:
        return "tongue"
    if mouth_height > 0.02:
        return "shock"
    if left_eye_open < 0.02 or right_eye_open < 0.02:
        return "wink"

    return "default"

# Open WebCam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb)

    current_expression = "default"

    if result.multi_face_landmarks:
        for face in result.multi_face_landmarks:
            landmarks = face.landmark
            current_expression = get_expression(landmarks)
            
            print(f"Detected: {current_expression}", end='\r')

   # Cat Image Display
    if current_expression == "shock":
        img_to_show = cat_shock
    elif current_expression == "wink":
        img_to_show = cat_wink
    elif current_expression == "tongue":
        img_to_show = cat_tongue
    elif current_expression == "angry":
        img_to_show = cat_angry
    elif current_expression == "awkward":
        img_to_show = cat_awkward
    elif current_expression == "happy":
        img_to_show = cat_happy
    else:
        img_to_show = cat_default

    # Resize webcam feed to match cat image
    frame_resized = cv2.resize(frame, (480, 480))

    # Combine webcam and cat image side by side
    combined = np.hstack((frame_resized, img_to_show))
    cv2.imshow("Cat Mood Cam", combined)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
print("\nCat Mood Cam closed.")