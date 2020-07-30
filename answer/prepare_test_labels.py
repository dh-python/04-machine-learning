"""
    MNISTファイル(gzip)を、CSVファイルに変換します.
    対象 : テストデータ : ラベル
"""
import struct
import gzip

fpath = "./mnist/t10k-labels-idx1-ubyte.gz"
with gzip.open(fpath, "rb") as f:
    magic_number, img_count = struct.unpack(">II", f.read(8))
    labels = []
    for i in range(img_count):
        label = str(struct.unpack("B", f.read(1))[0])
        labels.append(label)

# ファイルへ書き出し.
outpath = "./csv/test-labels.csv"
with open(outpath, "w") as f:
    f.write("\n".join(labels))
