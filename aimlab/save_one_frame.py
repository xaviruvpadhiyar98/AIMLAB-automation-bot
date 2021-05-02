from cv2 import imwrite
from random import randint

def save_one_frame(image):
    f_name = './screenshots/'+str(randint(0,2000000))+'.png'
    imwrite(f_name, image)

if __name__ == '__main__':
    save_one_frame()