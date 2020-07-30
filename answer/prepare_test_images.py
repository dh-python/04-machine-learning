"""
    MNISTファイル(gzip)を、CSVファイルに変換します.
    対象 : テストデータ : 画像
"""
import struct
import gzip

fpath = "./mnist/t10k-images-idx3-ubyte.gz"
with gzip.open(fpath, "rb") as f:
    magic_number, img_count = struct.unpack(">II", f.read(8))
    rows, cols = struct.unpack(">II", f.read(8))
    images = []
    for i in range(img_count):
        binary = f.read(rows * cols)
        image = ",".join([str(b) for b in binary])
        images.append(image)

# ファイルへ書き出し.
outpath = "./csv/test-images.csv"
with open(outpath, "w") as f:
    f.write("\n".join(images))
