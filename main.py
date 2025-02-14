import pygame
import random
#1. 게임 초기화
pygame.init()

#2. 게임창 옵션 설정
size=[400, 900]
screen=pygame.display.set_mode(size)

title="My Game"
pygame.display.set_caption(title)
 
#3. 게임 내 필요한 설정
clock=pygame.time.Clock()

class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self,address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else :
            self.img = pygame.img.load(address)
            self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img,(sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x,self.y))

ss = obj()
ss.put_img("image/ss.png")
ss.change_size(80,80)
ss.x = round(size[0]/2) -  round(ss.sx/2)
ss.y = ss_y = size[1] - ss.sy - 80
ss.move = 7




#ss = pygame.image.load("image/ss.png").convert_alpha()
#ss = pygame.transform.scale(ss,(80, 80))
#ss_sx, ss_sy = ss.get_size()
#ss_x = round(size[0]/2) -  round(ss_sx/2)
#ss_y = size[1] - ss_sy - 80
left_go = False
right_go = False
space_go = False

m_list = []
a_list = []
#리스트는 꼭 while문 밖에서 초기화!

black = (0,0,0)
white =(255,255,255)
k=0

#4. 메인 이벤트
SB=0
while SB==0:

    #4-1. FPS 설정
    clock.tick(60)

    #4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            SB=1
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False
    
    #4-3. 입력, 시간에 따른 변화
    if left_go == True:
        ss.x -= ss.move
        if ss.x <= 0:
            ss.x = 0
    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0]-ss.sx:
            ss.x = size[0]-ss.sx

    if space_go == True and k % 6 == 0:
        mm = obj()
        mm.put_img("image/bullet.png")
        mm.change_size(15,20)
        mm.x = round(ss.x + ss.sx/2-mm.sx/2)
        mm.y = ss.y - mm.sy - 10
        mm.move = 20
        m_list.append(mm)
    k += 1
    d_list = []
    for i in range(len(m_list)):
        m = m_list[i]
        m.y -= m.move
        if m.y <= -m.sy:
            d_list.append(i)
    for d in d_list:
        del m_list[d]
        
    if random.random() > 0.98:
        aa = obj()
        aa.put_img("image/alien.png")
        aa.change_size(40,40)
        aa.x = random.randrange(0, size[0]-aa.sx-round(ss.sx/2)-round(ss.sx/2))
        aa.y = 10
        aa.move = 1
        a_list.append(aa)
    d_list = [] #초기화 해야함.
    for i in range(len(a_list)):
        a = a_list[i]
        a.y += a.move
        if a.y >= size[1]:
            d_list.append(i)
    for d in d_list:
        del m_list[d]

    #4-4. 그리기
    screen.fill(black)
    ss.show()
    for m in m_list:
        m.show()
    for a in a_list:
        a.show()
    #screen.blit(ss, (ss_x,ss_y))

    #4-5. 업데이트
    pygame.display.flip()

#5. 게임 종료
pygame.quit()