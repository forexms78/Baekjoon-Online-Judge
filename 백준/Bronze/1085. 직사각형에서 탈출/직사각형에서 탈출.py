x,y,w,h = map(int,input().split())

cnt1 = w - x
cnt2 = h - y

move = min(cnt1,cnt2,x,y)

print(move)

