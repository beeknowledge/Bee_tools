# -*- coding: utf-8 -*-

import cv2

cap = cv2.VideoCapture("MVI_2745.MP4") # 動画を読み込む
video_frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) # フレーム数を取得する
video_fps = cap.get(cv2.CAP_PROP_FPS) # フレームレートを取得する
video_len_sec = video_frame_count / video_fps # 長さ（秒）を計算する
print(video_len_sec) # 長さ（秒）を出力する
allFrame = video_len_sec*video_fps
print("allframe=",video_frame_count)
frameNum = 0
numsec = 0
frames = 0
sec = 0

while(True):
    ret, frame = cap.read()
    frames = frames + 1
    numsec = frames/video_fps
    #print(numsec)
    
    if numsec >= 1.0:
        sec = sec + 1
        frames = 0
        numsec = 0
        #print(sec)
        
    
    
    cv2.putText(frame, str(sec) + ":" + str(frames),(0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
