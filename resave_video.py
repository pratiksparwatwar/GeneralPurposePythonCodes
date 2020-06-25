import cv2
import numpy

video_capture = cv2.VideoCapture("input.mp4")
fps = video_capture.get(cv2.CAP_PROP_FPS)
w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))


fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("output.mp4", fourcc, fps, (w, h))

while True:
    ret, frame = video_capture.read()  # frame shape 640*480*3
    if ret != True:
        break
    out.write(frame)

video_capture.release()
out.release()
cv2.destroyAllWindows()
    
