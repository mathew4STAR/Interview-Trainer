from re import L
import cv2
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
cap = cv2.VideoCapture(0)

LEFT_EYE = [ 362, 382, 381, 381, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]
with mp_face_mesh.FaceMesh(max_num_faces = 1, refine_landmarks = True, min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as face_mesh:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        img_height, img_width  = frame.shape[:2]
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)
        if results.multi_face_landmarks:
            # print(results.multi_face_landmarks)
            mesh_points = np.array([np.multiply([p.x, p.y], [img_width, img_height]).astype(int) for p in results.multi_face_landmarks[0].landmark])
            #print(mesh_points.shape)
            cv2.polylines(frame, [mesh_points[LEFT_EYE]], True, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.polylines(frame, [mesh_points[RIGHT_EYE]], True, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.polylines(frame, [mesh_points[LEFT_IRIS]], True, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.polylines(frame, [mesh_points[RIGHT_IRIS]], True, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow('Eye Tracker', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()