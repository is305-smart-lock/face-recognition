import face_recognition
import picamera
import numpy as np
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)




# load files
print("Loading known face image")


ID_00_image = face_recognition.load_image_file("ID_00.jpg")
ID_00_encoding = face_recognition.face_encodings(ID_00_image)[0]
ID_01_image = face_recognition.load_image_file("ID_01.jpg")
ID_01_encoding = face_recognition.face_encodings(ID_01_image)[0]
known_face_encodings = [
    ID_00_encoding,
    ID_01_encoding
]
known_face_names = [
    "ID_00",
    "ID_01"
]

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
        name = "<Unknown Person>"

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
        print("I see someone named {}!".format(name))
