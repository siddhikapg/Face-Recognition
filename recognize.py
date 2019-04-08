import face_recognition

image = face_recognition.load_image_file("people/saket.jpg")


#face_locations = face_recognition.face_locations(image)
#top, right, bottom, left = face_locations
#face_image = image[top:bottom, left:right]


unknown_image = face_recognition.load_image_file("group2.jpg")

sid_encoding = face_recognition.face_encodings(image)[0]

unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces(sid_encoding,[unknown_encoding])

print(results)