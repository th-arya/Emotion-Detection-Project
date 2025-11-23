import cv2
from fer import FER
detector = FER(mtcnn=True)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = detector.detect_emotions(frame)
    if results:
        for face in results:
            (x, y, w, h) = face["box"]
            emotion, score = detector.top_emotion(frame)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, f"{emotion} ({score:.2f})", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)

    cv2.imshow("Emotion Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
