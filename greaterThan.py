from paddleocr import PaddleOCR
from grabScreen import getScreen
from config import CFG
import numpy as np

def ocrResult(model):
    """ocr函数，识别题目
    :param det_path: 检测模型路径
    :param rec_path: 识别模型路径
    :return: 题目左侧数字和右侧数字
    """
    ocr = model
    nums = []
    left_img, right_img = np.array(getScreen(offSetY=CFG.offSetY))
    left_result = ocr.ocr(left_img, cls=True)
    right_result = ocr.ocr(right_img, cls=True)

    for line in left_result[0]:
        nums.append(line[1][0])
    for line in right_result[0]:
        nums.append(line[1][0])

    left, right = nums[0], nums[1]
    left = int(left)
    right= int(right)
    return left, right

def leftOrRight(left, right):
    """比大小函数
    :param left: 左侧数字
    :param right: 右侧数字
    :return: left>right则返回1，left<right则返回0，left=right则返回-1
    """
    if left == right:
        return -1
    elif left < right:
        return 0
    elif left > right:
        return 1

if __name__ == '__main__':
    model = PaddleOCR(
                     # det_model_dir=CFG.det_path,
                     rec_model_dir=CFG.rec_path,
                     use_angle_cls=True,
                     lang='en'
                     )
    left, right = ocrResult(model=model)
    print(f'left number is {left}, right number is {right}, 结果：{leftOrRight(left, right)}')