import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r'C:\Users\blankblack\Desktop\haar-cascade-files-master\haar-cascade-files-master\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\blankblack\Desktop\haar-cascade-files-master\haar-cascade-files-master\haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret:
            cv2.imshow("My Window", gray)
            faces = face_cascade.detectMultiScale(frame)
            for face in faces:
             x, y, w, h = face
             frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

             roi_gray = gray[y:(y + h), x:(x + w)]
             roi_color = frame[y:(y + h), x:(x + w)]
             eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
            for (x_eye, y_eye, w_eye, h_eye) in eyes:
                cv2.rectangle(roi_color, (x_eye, y_eye), (x_eye + w_eye, y_eye + h_eye), (0, 0, 255), 3)
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
            for (x_eye, y_eye, w_eye, h_eye) in eyes:
                cv2.rectangle(roi_color, (x_eye, y_eye), (x_eye + w_eye, y_eye + h_eye), (0, 0, 255), 3)

    cv2.imshow("Image", frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
