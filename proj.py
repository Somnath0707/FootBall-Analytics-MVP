from ultralytics import YOLO

model1 = YOLO('models/best.pt');

reuslt = model1.predict('/Users/somnathghorpade/Desktop/Project/input_videos/08fd33_4.mp4',save = True)
print(reuslt[0])
print('=====================================================')
for box in reuslt[0].boxes:
    print(box)
