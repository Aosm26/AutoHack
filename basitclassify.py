from ultralytics import YOLO

file_path = "C:\\Users\\alios\\Desktop\\Desktop\\AutoHack\\arabakaza.jpeg"

model = YOLO('best.pt')

result = model.predict(file_path, save=True)

print(result[0].probs.top1)