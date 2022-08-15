import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.hands()

i =0 
while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
    
# def returnCameraIndexes():
#     # checks the first 10 indexes.
#     index = 0
#     arr = []
#     i = 10
#     while i > 0:
#         cap = cv2.VideoCapture(index)
#         if cap.read()[0]:
#             arr.append(index)
#             cap.release()
#         index += 1
#         i -= 1
#     return arr

# print(returnCameraIndexes)