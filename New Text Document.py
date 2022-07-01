def merge_sort(draw_bar,arr,s,e):
    if e-s>=1:
        timer = pygame.time.Clock()
        mid=(s+e)//2
        l_arr=[]
        r_arr=[]
        for i in range(s,mid):
            l_arr.append(arr[i])
        for i in range(mid+1,e):
            r_arr.append(arr[i])
        merge_sort(draw_bar,l_arr,s,mid)
        merge_sort(draw_bar,r_arr,mid+1,e)
        l=r=0
        a=s
        while l<len(l_arr) and r<len(r_arr):
            if l_arr[l]>r_arr[r]:
                arr[a]=r_arr[r]
                r=r+1
            else:
                arr[a]=l_arr[l]
                l=l+1
            a=a+1
            draw(draw_bar,{l: draw_bar.blue,r: draw_bar.green})
            timer.tick(10)
        while r<len(r_arr):
            arr[a] = r_arr[r]
            r = r + 1
            a=a+1
            draw(draw_bar, {r: draw_bar.green})
            timer.tick(10)
        while l<len(l_arr):
            arr[a] = l_arr[l]
            l = l + 1
            a=a+1
            draw(draw_bar, {l: draw_bar.blue})
            timer.tick(10)
    return arr

elif event.key == pygame.K_m and sort == False:
sort = True
v = draw_bar.arr
merge_sort(draw_bar, v, 0, len(v) - 1)