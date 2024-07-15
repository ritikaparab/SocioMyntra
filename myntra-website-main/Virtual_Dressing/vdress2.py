import numpy as np
import cv2
from PIL import Image

def run():
    # multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
    
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # set Width
    cap.set(4, 480)  # set Height

    while True:
        ret, img = cap.read()
        if not ret:
            break  # If frame not captured properly, exit the loop

        roi = np.zeros_like(img)  # setting the shape for the image
        output = np.zeros_like(img)  # setting the shape for the image
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
        
        d2 = Image.open("myntra-website-main\Virtual_Dressing\whiteshirt.png").convert('RGBA')

        for (x, y, w, h) in faces:
            roi = img[y + 80:y + h + 260, x - 80:x + w + 80]
            output = img.copy()
            
            try:
                d2 = d2.resize((w + 150, h + 180), Image.Resampling.LANCZOS)

                pilim = Image.fromarray(roi)
                pilim.paste(d2, box=(0, 10), mask=d2)
                roi = np.array(pilim)  # roi ma virtual dress banyo

            except Exception as e:
                print(f"Error: {e}")
                pass

            output[y + 80:y + h + 260, x - 80:x + w + 80] = roi

        cv2.imshow('Virtual Dressing', output)
        
        k = cv2.waitKey(30) & 0xff
        if k == ord('q'):  # press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

#return "Virtual Dressing script executed successfully!"

#Example of how to call the run function (uncomment to test directly)
if __name__ == "__main__":
    run()
