import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    codes = decode(frame)
    for code in codes:
        print("QR Code Data:", code.data.decode())
        cv2.rectangle(frame, (code.rect.left, code.rect.top),
                      (code.rect.left + code.rect.width, code.rect.top + code.rect.height),
                      (0, 255, 0), 2)
    cv2.imshow("QR Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
