# 把当前文件夹下所有的fasta 转为 单行的txt
import os
for file in os.listdir():
    if str(file).endswith("fasta"):
        lines = open(file).read()
        data = lines.split('>')
        res = []
        for x in data:
            if x != "":
                x = x.split('\n')
                builder = ""
                index = 0
                while index < len(x) - 1:
                    builder += x[index + 1]
                    index += 1
                res.append(">" + x[0] + " |sequence " + builder + '\n')

        with open(file.split(".fasta")[0]+".txt", 'w') as f:
            for x in res:
                f.write(x)
