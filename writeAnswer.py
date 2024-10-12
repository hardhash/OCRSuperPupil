import pyautogui as pg
from config import CFG

def drawAns(result, start_x=CFG.start_x, start_y=CFG.start_y):
    if result == -1:
        x0, y0 = start_x, start_y
        x1, y1 = start_x + 20, start_y
        x2, y2 = start_x, start_y + 20
        x3, y3 = start_x + 20, start_y + 20

        pg.moveTo(x0, y0)
        pg.mouseDown(button='left')
        pg.dragTo(x1, y1, 0.01, button='left', mouseDownUp=True)
        pg.mouseUp(button='left')

        pg.moveTo(x2, y2)
        pg.mouseDown(button='left')
        pg.dragTo(x3, y3, 0.01, button='left', mouseDownUp=True)
        pg.mouseUp(button='left')

    elif result == 0:
        x0, y0 = start_x, start_y
        x1, y1 = start_x - 40, start_y + 20
        x2, y2 = start_x, start_y + 40
        pg.moveTo(x0, y0)
        pg.mouseDown(button='left')
        pg.dragTo(x1, y1, 0.01, button='left', mouseDownUp=True)
        pg.dragTo(x2, y2, 0.01, button='left', mouseDownUp=True)
        pg.mouseUp(button='left')

    elif result == 1:
        x0, y0 = start_x, start_y
        x1, y1 = start_x + 40, start_y + 20
        x2, y2 = start_x, start_y + 40
        pg.moveTo(x0, y0)
        pg.mouseDown(button='left')
        pg.dragTo(x1, y1, 0.01, button='left', mouseDownUp=True)
        pg.dragTo(x2, y2, 0.01, button='left', mouseDownUp=True)
        pg.mouseUp(button='left')

if __name__ == '__main__':
    drawAns(1)
