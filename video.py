import cv2

# Playing video from file:
# cap = cv2.VideoCapture('vtest.avi')
# Capturing video from webcam:
cap = cv2.VideoCapture(0)

currentFrame = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Handles the mirroring of the current frame
    frame = cv2.flip(frame, 1)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Saves image of the current frame in jpg file
    # name = 'frame' + str(currentFrame) + '.jpg'
    # cv2.write(name, frame)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # To stop duplicate images
    if 0xFF != ord('q'):
        currentFrame += 1
        continue

    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
