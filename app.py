from config import CFG
from writeAnswer import drawAns
from greaterThan import ocrResult, leftOrRight
from paddleocr import PaddleOCR
import time

if __name__ == '__main__':
    idx = 10
    model = PaddleOCR(
                     # det_model_dir=CFG.det_path,
                     rec_model_dir=CFG.rec_path,
                     use_angle_cls=True,
                     lang='en'
                     )
    for i in range(idx):
        left, right = ocrResult(model=model)
        print(f'left number is {left}, right number is {right}, 结果：{leftOrRight(left, right)}')
        drawAns(leftOrRight(left, right))
        time.sleep(0.023)

