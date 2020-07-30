"""
    CSV出力した画像データが正しいか否かを判断するために、
    一部を画像データとして出力してみます.
"""

with open("./csv/train-images.csv") as f:
    images = f.read().split("\n")

for i, image in enumerate(images[:10]):
    with open("./image/%d.pgm" % i, "w") as f:
        s = "P2 28 28 255\n"
        s += " ".join(image.split(","))
        f.write(s)
