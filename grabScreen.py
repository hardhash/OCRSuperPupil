import pyautogui as pg
import matplotlib.pyplot as plt
from config import CFG
import numpy as np
from PIL import Image

def getScreen(width=CFG.grabWidth, height=CFG.grabHeight, offSetY=0):
    """
    默认把app放在屏幕右侧
    :param width: 截图的宽度，根据自己显示器尺寸调整
    :param height: 截图的长度，根据自己显示器尺寸调整
    :param offSetY: 截图y轴起点向下偏移offSetY，默认为0，表示从顶部开始截
    :return: 截图图像
    """
    # 获取屏幕尺寸
    screen_width, screen_height = pg.size()
    # 指定左上角坐标
    left_up_x = screen_width - width
    left_up_y = offSetY
    # 指定右下角坐标
    right_but_x = screen_width
    right_but_y = height + offSetY
    screen = pg.screenshot(region=(left_up_x, left_up_y, right_but_x, right_but_y))
    new_size = (width, height*20)
    img_np = np.array(screen.resize(new_size))
    height, width = img_np.shape[:2]
    upper_half_np = img_np[:height // 2, :]
    mid_point = width // 2
    left_half_np = upper_half_np[:, 40:mid_point-15]
    right_half_np = upper_half_np[:, mid_point+15:-40]
    left_half_img = Image.fromarray(left_half_np)
    right_half_img = Image.fromarray(right_half_np)

    return left_half_img, right_half_img
def show_img(img):
    """
    截图可视化
    """
    plt.imshow(img[0])
    plt.imshow(img[1])
    plt.show()

if __name__ == '__main__':
    show_img(getScreen(offSetY=CFG.offSetY))