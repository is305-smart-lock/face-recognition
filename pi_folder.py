import face_recognition
import picamera
import os
import numpy as np
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)




# load files
print("Loading known face image")

load_path="/home/pi/Desktop/photo/"

known_face_encodings = []

for item in os.listdir(load_path):
    src=os.path.join(load_path,item)
    known_face_encodings = known_face_encodings + [face_recognition.face_encodings(face_recognition.load_image_file(src))[0]]


face_locations = []
face_encodings = []
face_names = []
while True:
    print("Capturing image.")
    # 以numpy array的数据结构从picamera摄像头中获取一帧图片
    camera.capture(output, format="rgb")

    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # 将每一个人脸与已知样本图片比对
    for face_encoding in face_encodings:
      
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
        
            print("I see someone in folder!")
