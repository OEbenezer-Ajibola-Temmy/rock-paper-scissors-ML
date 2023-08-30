# This file contains helper functions for my main app

import mediapipe as mp
import tensorflow as tf 
import numpy as np 
import cv2 
import base64
from collections import Counter

def extract_landmarks(image):
    mp_hands = mp.solutions.hands.Hands(
        static_image_mode=True, max_num_hands=1, min_detection_confidence=0.5)
    #image = cv2.imread(image)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(image_rgb)
    print('results')
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        return hand_landmarks.landmark
    else:
        print("No image detected")
        return None
    

def preprocess_landmarks(landmarks, image_width, image_height):

    preprocessed_landmarks = []
    
    if landmarks:
        for landmark in landmarks:
            landmark_x = landmark.x * image_width
            landmark_y = landmark.y * image_height
            preprocessed_landmarks.extend([landmark_x, landmark_y, landmark.z])
            landmark_array = np.array(preprocessed_landmarks)
            landmark_array = np.expand_dims(landmark_array, axis=0)
        return landmark_array
    else:
        return "No image"


    


def predict_hand_gesture(landmarks):

    if landmarks != "No image":
        gestures = ["Rock", "Paper", "Scissors"]

        keras_model = tf.keras.models.load_model("./model2/")

        prediction = keras_model.predict(landmarks)
        predicted_class = np.argmax(prediction)
        gesture_label = gestures[predicted_class]
        return gesture_label
    else:
        return "No image"


def process_image(image_datas):
    results = []

    for image_data in image_datas:
        decoded_data = base64.b64decode(image_data)
        nparr = np.frombuffer(decoded_data, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        print(f"image from server : {img}")
        height, width, channels = img.shape

        landmarks = extract_landmarks(img)
        processed_landmarks = preprocess_landmarks(landmarks, width, height)
        prediction = predict_hand_gesture(processed_landmarks)

        results.append(prediction)
    print(results)
        
    count = Counter(results)
    print(count)

    most_common = count.most_common(1)


    if most_common[0][0] != "No image" and most_common:
        return most_common[0][0]
    elif most_common[0][1] == 3 and most_common[0][0] == "No image":
        return "No image"
    elif most_common[0][0] == "No image" and most_common[0][1] != 3:
        return count.most_common(2)[0][0]
    elif not most_common: 
        return results[1] if results[1] else results[2]




    
