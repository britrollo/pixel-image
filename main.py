import cv2

def blockColor(img, block_size):
    dim = block_size**2
    (tb, tg, tr) = (0, 0, 0)
    for x in range(block_size):
        for y in range(block_size):
            (b, g, r) = img[y, x]
            tb += b
            tg += g
            tr += r
    return (tb//dim, tg//dim, tr//dim)

file_name = input("Enter file name: ")
img = cv2.imread(file_name)
block_size = int(input("Enter block size: "))

(h, w) = img.shape[:2]

if(h % block_size != 0 or w % block_size != 0):
    h = h - (h % block_size)
    w = w - (w % block_size)
    dim = (w, h)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

for x in range(0, w, block_size):
    for y in range(0, h, block_size):
        (b, g, r) = blockColor(img[y:(y+block_size),x:(x+block_size)], block_size)
        img[y:(y+block_size),x:(x+block_size)] = (b, g, r)


cv2.imshow('image', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

