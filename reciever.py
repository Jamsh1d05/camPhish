from flask import *
import cv2

app = Flask(__name__)

@app.route('/capture-photo')
def capture_photo():
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        return 'Cannot access the camera'

    ret, frame = camera.read()

    if not ret:
        return 'Failed to capture image'

    camera.release()

    photo_filename = 'captured_photo.jpg'
    cv2.imwrite(photo_filename, frame)
    
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
