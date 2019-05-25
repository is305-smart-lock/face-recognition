import face_recognition
import picamera
import numpy as np
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)
print("Loading known face image")
# 初始化已知人脸数据
known_face_encodings = []
# 伪代码
for image in sql
# 添加数据
known_face_encodings = known_face_encodings + [face_recognition.face_encodings(face_recognition.load_image_file( image )[0] ]
face_locations = []
face_encodings = []
face_names = []
while True:
    print("Capturing image.")
    #从摄像头中获取一帧图片
    camera.capture(output, format="rgb")
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)
    # 比对
    for face_encoding in face_encodings:  
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]: 
        print("I see someone in sql!")
