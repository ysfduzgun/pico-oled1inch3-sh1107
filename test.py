from machine import Pin
from picoled import OLED_1inch3
from time import sleep

# init oled
DC, RST, MOSI, SCK, CS = 8, 12, 11, 10, 9
OLED = OLED_1inch3(DC, RST, MOSI, SCK, CS)
keyA = Pin(15,Pin.IN,Pin.PULL_UP)
keyB = Pin(17,Pin.IN,Pin.PULL_UP)
BLACK=0x0000
WHITE=0xffff

def welcome():
    OLED.fill(BLACK)
    OLED.fill_rect(0,0,128,32,OLED.white)
    OLED.text("Hello World",5,12,OLED.black)
    OLED.fill_rect(0,28,128,2,OLED.black)

    OLED.fill_rect(0,34,128,2,OLED.white)
    OLED.text("With Pic-O-LED",5,46,OLED.white)


if __name__=='__main__':


    while(1):
        if keyA.value() == 0 and keyB.value() == 0:
            OLED.fill(BLACK)
            OLED.text("DOUBLE KILL :)",5,28,OLED.white)
        elif keyA.value() == 0:
            OLED.text("A",119,2,OLED.black)
        elif keyB.value() == 0:
            OLED.text("B",119,2,OLED.black)
        else:
            OLED.fill_rect(119,0,128,10,OLED.white)
            welcome()
        OLED.show()

    sleep(1)
