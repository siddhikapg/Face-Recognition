import face_recognition
from PIL import Image

image = face_recognition.load_image_file("us.jpg")
face_locations = face_recognition.face_locations(image)

print(" I found faces in this pic",len(face_locations))

i = 0

for location in face_locations:
    top, right, bottom, left = location
    print(" A face located at pixel location Top: {}, Right: {}, Left: {}".format(top, left, bottom, right))

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save("face-{}.jpg".format(i))
    i = i + 1