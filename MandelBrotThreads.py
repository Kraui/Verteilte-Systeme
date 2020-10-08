import threading
from PIL import Image

w = 512 
h = 512
image = Image.new("RGB", (w, h))
wh = w * h
maxIt = 256 
xa = -2.0
xb = 1.0
ya = -1.5
yb = 1.5
xd = xb - xa
yd = yb - ya
numThr = 5 

class ManFrThread(threading.Thread): 
    def __init__ (self, k):
          self.k = k
          threading.Thread.__init__(self)
    def run(self):
        for i in range(k, wh, numThr):
            kx = i % w
            ky = int(i / w)
            a = xa + xd * kx / (w - 1.0)
            b = ya + yd * ky / (h - 1.0)
            x = a
            y = b
            for kc in range(maxIt):
                x0 = x * x - y * y + a
                y = 2.0 * x * y + b
                x = x0                
                if x * x + y * y > 4:
                    red = (kc % 8) * 32
                    green = (16 - kc % 16) * 16
                    blue = (kc % 16) * 16
                    global image
                    image.putpixel((kx, ky), (red, green, blue))
                    break

if __name__ == "__main__":
    tArr = []
    for k in range(numThr):
        tArr.append(ManFrThread(k))
    for k in range(numThr): 
        tArr[k].start()
    for k in range(numThr):
        tArr[k].join()
    image.save("MandelbrotFractal.png", "PNG")
    image.show()