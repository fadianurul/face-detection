import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#deteksi wajah

    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
        cv2.putText (frame,'wajah', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 2,(0, 255, 0), 5)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.putText (frame,'Terhitung Wajah : ' + str(len(face)), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0, 255, 0), 2)
    cv2.imshow('wajah', frame)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
