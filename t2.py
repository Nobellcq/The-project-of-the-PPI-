import pandas as pd
import re

# 这里的seq需要携带一下，前面携带名字，后面携带
def detectOneLine(seq):
    # 遍历motifs
    for x in range(len(motif)):
        result = re.search(motif[x:x+1].Regex.values[0], seq.split('|')[1])
        # 匹配到了，检查当前序列的名字是啥,如果包含了，那么就加一
        if result is not None:
            find_item = motif[x:x+1].ELMIdentifier.values[0]
            if not find.__contains__(find_item):
                find.append( find_item )
                protein_name = seq.split('|')[0]
                detectTimes(protein_name)
                # print(find_item)

def detectTimes(protein_name):
    for index in range(1, 17):
        if protein_name.__contains__("nsp"+str(index)):
            list["nsp"+str(index)] = list["nsp"+str(index)] + 1
    if protein_name.__contains__("capsid"):
        list["capsid"] = list["capsid"] + 1

def listInit():
    for index in range(1, 17):
        list["nsp" + str(index)] = 0
    list["capsid"] = 0

if __name__ == '__main__':
    motif = pd.read_csv('elm_classes.tsv', sep='\t')
    find = []  # 匹配到的所有的
    list = {}
    listInit()
    lines = open("MERS.txt").read()  # 这里是Mers匹配到的
    data = lines.split('\n')
    data.pop()  # remove the last space
    total_number = len(data)
    new = []  # 新的过滤后的  和名字一起处理的
    for x in data:
        protein_name = x.split("|Protein Name:")
        protein_sequ = x.split("|sequence ")
        if len(protein_name) > 1:
            protein_name = protein_name[1].split("|")[0]
            protein_sequ = protein_sequ[1]
            if not protein_name.__contains__("nsp11"):  # 名字重复没有关, 序列不能重复就是了
                if protein_name.__contains__("capsid") or protein_name.__contains__("nsp"):
                    protein_name = protein_name + "|" + protein_sequ
                    if not new.__contains__(protein_name):
                        new.append(protein_name)

    for x in range(len(new)):
        print(x)
        detectOneLine(new[x])
    print(len(find))
    print(list)
    out = ""
    for i in range(1,len(list)+1):
        if i == 17:
            out +=str(list["capsid"] / total_number) + " "
        elif not i == 11:
            out +=str(list["nsp"+str(i)]/total_number)+" "

    print(out)
    with open("out.txt", 'w') as f:
        f.write(out)
