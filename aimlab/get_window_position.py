from win32gui import GetWindowText, EnumWindows, GetWindowRect

windows_list = []

# This fn will iterate every window opened in Windows
def enum_win(hwnd, result):
    win_text = GetWindowText(hwnd)
    windows_list.append((hwnd, win_text))

EnumWindows(enum_win, [])

def get_window_position(window_name):
    for (hwnd, win_text) in windows_list:
        if window_name in win_text.lower():
            game_hwnd = hwnd
            return GetWindowRect(game_hwnd)


if __name__ == '__main__':
    position = get_window_position('_tb')
    print(position)