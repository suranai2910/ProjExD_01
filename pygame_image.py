import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg") # 練習1
    bg_img2 = pg.transform.flip(bg_img,True,False)
    tori_img = pg.image.load("ex01/fig/3.png") #練習２
    tori_img = pg.transform.flip(tori_img, True, False) #練習２
    tori_imgs = [tori_img, pg.transform.rotozoom(tori_img,2,1.0),
                 pg.transform.rotozoom(tori_img,4,1.0), pg.transform.rotozoom(tori_img,6,1.0),
                 pg.transform.rotozoom(tori_img,8,1.0),pg.transform.rotozoom(tori_img,10,1.0),
                 pg.transform.rotozoom(tori_img,8,1.0),pg.transform.rotozoom(tori_img,6,1.0),
                 pg.transform.rotozoom(tori_img,4,1.0),pg.transform.rotozoom(tori_img,2,1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr%3200) #練習６
        screen.blit(bg_img, [x, 0]) #練習６
        screen.blit(bg_img2, [1600+x,0]) #練習６
        screen.blit(bg_img, [3200+x, 0])
        screen.blit(tori_imgs[tmr%10], [300,200]) #練習５
        pg.display.update()
        tmr += 1        
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()