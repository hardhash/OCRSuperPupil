class CFG():
    grabWidth = 340 # 截图的宽度
    grabHeight= 15 # 截图的长度
    offSetY = 220   # 截图向下偏移值
    det_path = './en_PP-OCRv3_det_infer'  # 轻量化检测模型的路径
    rec_path = './en_PP-OCRv3_rec_infer'  # 轻量化检测模型的路径
    start_x, start_y = 1200, 550 # 绘制大小等于符号时的起点位置
