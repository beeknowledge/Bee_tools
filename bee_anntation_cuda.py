import cv2
import time
import csv

print(cv2.__file__) 
CONFIDENCE_THRESHOLD = 0.25
NMS_THRESHOLD = 0.3
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []

    
with open("coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]



#net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
#net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)


#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

model = cv2.dnn_DetectionModel(net)

model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

img = cv2.imread("test.jpg")
img_base = img#ベース画像
v_height, v_width, _channels = img.shape


classes, scores, boxes = model.detect(img, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)

annotation = []                    
for (classid, score, box) in zip(classes, scores, boxes):
    color = COLORS[int(classid) % len(COLORS)]
    label = "%s : %f" % (class_names[classid[0]], score)
    print(box)
    
    x, y, w, h = box
    cv2.rectangle(img, (x, y, w, h), color, 2)

    center_x= round((w/2 + x)/v_width, 6)
    center_y = round((h/2 + y)/v_height, 6)
    print((w/2 + x),(h/2 + y ))
    

    y_width = round((w)/v_width, 6)
    y_height = round(h/v_height, 6)
    print(w,h)
    
    classCounter = str(classid[0])
    hhh = str(classid[0]) + ' ' + str(center_x) + ' ' + str(center_y) + ' ' + str(y_width) + ' ' + str(y_height)
    cv2.putText(img, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    annotation.append([hhh])
    print(hhh)


with open('test.txt', 'w') as fout:
    writer = csv.writer(fout)
    writer.writerows(annotation)
    fout.close


cv2.imwrite("out.jpg",img)
cv2.imshow("detections", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

