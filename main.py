from aimlab.get_center_coordinates import get_center_coordinates
from aimlab.mouse import Mouse, get_cursor_position, left_click
from aimlab.key_check import key_check
from aimlab.negate import negate
from aimlab.start import start
from time import sleep


start()
mouse = Mouse()

while True:

    if key_check() == "H":
        print("Ending")
        break

    centers = get_center_coordinates()

    for target_x, target_y in centers:
        cursor_x, cursor_y = get_cursor_position()
        dx, dy = cursor_x - target_x, cursor_y - target_y
        ndx, ndy = negate(dx), negate(dy)

        mouse.move_mouse((ndx,dy));sleep(0.01)
        left_click();sleep(0.001)
        mouse.move_mouse((dx, ndy));sleep(0.01)

