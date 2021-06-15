import cv2
import time

print(cv2.__file__) 
CONFIDENCE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.45
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]



net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)


net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

model = cv2.dnn_DetectionModel(net)
#model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)
model.setInputParams(size=(608, 608), scale=1/255, swapRB=True)
#delay=1
vc = cv2.VideoCapture(0)
while cv2.waitKey(1) < 1:
#    (grabbed, frame) = vc.read()
#    if not grabbed:
#        exit()

#while(True):
    ret, frame = vc.read()
    #if not grabbed:
    #    exit()    
    #cv2.imshow('frame',frame)
    start = time.time()
    classes, scores, boxes = model.detect(frame, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    end = time.time()

    start_drawing = time.time()
    for (classid, score, box) in zip(classes, scores, boxes):
        color = COLORS[int(classid) % len(COLORS)]
        label = "%s : %f" % (class_names[classid[0]], score)
        cv2.rectangle(frame, box, color, 2)
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    end_drawing = time.time()
    
    fps_label = "FPS: %.2f (excluding drawing time of %.2fms)" % (1 / (end - start), (end_drawing - start_drawing) * 1000)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("detections", frame)

    #動画保存ON/OFF 描写出力開始に作成する動画ファイルの削除(空の動画ファイル)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

vc.release()
cv2.destroyWindow("detections")
