from yolov5.detect import run
import time
start = time.time()
weight = True

result_bool = run(weights='./best.pt', source='./Test (203).jpg', project='./result', nosave=False)

'''
while 1:
    result_bool = run('./best.pt', './Test (204).jpg', project='./result', nosave=True)
    print(result_bool)
    print("time :", time.time() - start)

    if weight:
        weight = False
        continue
    else:
        weight = True
        result_bool = run(weights='./best.pt', source='./Test (204).jpg', project='./result', nosave=False)
        break
'''