import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

with mp_pose.Pose(
    static_image_mode=True) as pose:
    
    image = cv2.imread("camiseta_bobEsponja.JPG")
    height,width, _ = image.shape # Obtenemos las dimensiones de la imagen
    image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # Transformamos la imagen a formato rgb
    
    # Mostramos los 33 putos que nos ofrece mediapipe pose
    results = pose.process(image_rgb)
    print("Pose landmarks: ",results.pose_landmarks)
    
    # Dibujamos los puntos de referencia y conexiones:
    
    # Primero comprobamos que existen puntos de referencia
    if results.pose_landmarks is not None:
        print(int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x*width))
        x1=int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x*width)
        y1=int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y*height)
        
        x2=int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x*width)
        y2=int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y*height)
        
        x3=int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x*width)
        y3=int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y*height)
        
        x4=int(results.pose_landmarks.landmark[11].x*width)
        y4=int(results.pose_landmarks.landmark[11].y*height)
        
        x5=int(results.pose_landmarks.landmark[13].x*width)
        y5=int(results.pose_landmarks.landmark[13].y*height)
        
        x6=int(results.pose_landmarks.landmark[15].x*width)
        y6=int(results.pose_landmarks.landmark[15].y*height)        
        
        cv2.line(image,(x1,y1),(x2,y2),(255,255,255),3)
        cv2.line(image,(x2,y2),(x3,y3),(255,255,255),3)
        cv2.line(image,(x4,y4),(x5,y5),(255,255,255),3)
        cv2.line(image,(x5,y5),(x6,y6),(255,255,255),3)
        cv2.circle(image,(x1,y1),6,(128,0,255),-1)
        cv2.circle(image,(x2,y2),6,(128,0,255),-1)
        cv2.circle(image,(x3,y3),6,(128,0,255),-1)
        cv2.circle(image,(x4,y4),6,(255,191,0),-1)
        cv2.circle(image,(x5,y5),6,(255,191,0),-1)
        cv2.circle(image,(x6,y6),6,(255,191,0),-1)
        
        
        
        '''
        mp_drawing.draw_landmarks(image,results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(128,0,250), thickness=2, circle_radius=3),
            mp_drawing.DrawingSpec(color=(255,255,255),thickness=2))
        '''
        
    cv2.imshow("Image",image)
    cv2.waitKey(0)
cv2.destroyAllWindows()