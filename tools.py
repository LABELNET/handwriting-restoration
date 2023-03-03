import math

c1 = [20,20]
c1r = 10

c2 = [60,60]
c2r = 20 

d = math.sqrt((abs(c1[0]-c2[0])**2)+abs(c1[1]-c2[1])**2)
aplha = math.acos(abs(c1r-c2r)/d)

print(d,aplha)

hpq = math.atan((abs(c1[1]-c2[1])/abs(c1[0]-c2[0])))

hpb = hpq + aplha
hpc = hpq - aplha
print(hpq,hpb)

x3 = c1[0] + c1r * math.cos(hpb)
y3 = c1[1] + c1r * math.sin(hpb)



x4 = c2[0] + c2r * math.cos(hpb)
y4 = c2[1] + c2r * math.sin(hpb)

print((x3,y3),(x4,y4))

x5 = c1[0] + c1r * math.cos(hpc)
y5 = c1[1] + c1r * math.sin(hpc)


x6 = c2[0] + c2r * math.cos(hpc)
y6 = c2[1] + c2r * math.sin(hpc)

print((x5,y5),(x6,y6))


img = np.ones([100, 100, 3], dtype=np.uint8) * 255
# c1
cv2.circle(img, (c1[0],c1[1]), c1r, color=(255, 0, 0),lineType=4)
cv2.circle(img, (c1[0],c1[1]), 0, color=(255, 0, 0))
# c2
cv2.circle(img, (c2[0],c2[1]), c2r, color=(0, 255, 0),lineType=4)
cv2.circle(img, (c2[0],c2[1]), 0, color=(0, 255, 0))
# 切线 1
cv2.line(img,(int(x3),int(y3)),(int(x4),int(y4)),color=(0, 0, 0))
cv2.line(img,(int(x5),int(y5)),(int(x6),int(y6)),color=(0, 0, 0))
plt.imshow(img)
plt.figure('image')
plt.show()