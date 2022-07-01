import pygame
import random
pygame.init()

class drawoutput:
    black = 0, 0, 0
    white = 255, 255, 255
    red = 255, 0, 0
    green = 0, 255, 0
    blue = 0, 0, 255
    background = white
    color_bar = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    refer_line_hori=100
    refer_line_ver=150
    sort=False
    fontt=pygame.font.SysFont('comicsans',25)
    lagre_font=pygame.font.SysFont('comicsans',40)

    def __init__(self,arr,height,width):
        self.height=height
        self.width=width
        self.window=pygame.display.set_mode((width,height))
        pygame.display.set_caption("My SORTING SIMULATOR")
        self.set_arr(arr)

    def set_arr(self,arr):
        self.arr=arr
        self.mi=min(arr)
        self.mx=max(arr)
        self.block_wid=round((self.width-self.refer_line_hori)/len(arr))
        self.block_hig=round((self.height-self.refer_line_ver)/(self.mx-self.mi))
        self.start_x=self.refer_line_hori

def draw(draw_bar,color_positions={}):
    draw_bar.window.fill(draw_bar.background)
    ctrls=draw_bar.fontt.render("R-reset | S-selection sort",1,draw_bar.black)
    draw_bar.window.blit(ctrls,((draw_bar.width/2)-(ctrls.get_width()/2),8))
    sort_ing=draw_bar.fontt.render("I-insertion sort | B-bubble sort",1,draw_bar.black)
    draw_bar.window.blit(sort_ing,((draw_bar.width/2)-(sort_ing.get_width()/2),32))
    draw_arr(draw_bar,color_positions)
    pygame.display.update()

def draw_arr(draw_bar,color_positions={}):
    arr=draw_bar.arr
    #print("the arr is: ", arr)
    for i, data in enumerate(arr):
        x=draw_bar.start_x+(i*draw_bar.block_wid)
        y=draw_bar.height-((data-draw_bar.mi)*draw_bar.block_hig)
        col=draw_bar.color_bar[i%3]
        if i in color_positions:
            col=color_positions[i]
        pygame.draw.rect(draw_bar.window,col,(x,y,draw_bar.block_wid,draw_bar.height))

def generate_arr():
    arr=[]
    for i in range(50):
        data=random.randint(1,100)
        arr.append(data)
    return arr

def bubble_sort(draw_bar):
    arr=draw_bar.arr
    timer=pygame.time.Clock()
    for i in range(len(arr)-1):
        for j in range(len(arr)-(1+i)):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                draw(draw_bar,{j: draw_bar.blue,j+1:draw_bar.green})
                timer.tick(10)
    return arr

def insertion_sort(draw_bar):
    arr=draw_bar.arr
    timer=pygame.time.Clock()
    for i in range(1,len(arr)):
        key=arr[i]
        while True:
            if i>0 and arr[i-1]>key:
                arr[i]=arr[i-1]
                i=i-1
                arr[i]=key
                draw(draw_bar,{i-1: draw_bar.blue, i: draw_bar.green})
                timer.tick(10)
            else:
                break
    return arr

def selection_sort(draw_bar):
    arr=draw_bar.arr
    timer=pygame.time.Clock()
    for i in range(0,len(arr)):
        ind=i
        for j in range(i+1,len(arr)):
            if arr[ind]>arr[j]:
                ind=j
        arr[i],arr[ind]=arr[ind],arr[i]
        draw(draw_bar,{ind: draw_bar.blue,i:draw_bar.green})
        timer.tick(4)
    return arr

def main():
    bo_ol=True
    sort=False
    timer=pygame.time.Clock()
    arr=generate_arr()
    draw_bar=drawoutput(arr,600,800)
    while bo_ol:
        timer.tick(10)
        draw(draw_bar)
        for input in pygame.event.get():
            if input.type==pygame.QUIT:
                bo_ol=False
            if input.type!=pygame.KEYDOWN:
                continue
            if input.key==pygame.K_r:
                arr=generate_arr()
                draw_bar.set_arr(arr)
                sort=False
            elif input.key==pygame.K_b and sort==False:
                sort=True
                bubble_sort(draw_bar)
            elif input.key==pygame.K_i and sort==False:
                sort = True
                insertion_sort(draw_bar)
            elif input.key==pygame.K_s and sort==False:
                sort=True
                selection_sort(draw_bar)
    pygame.quit()

if __name__=="__main__":
    main()