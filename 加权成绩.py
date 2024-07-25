studic={22001:(70,80),22005:(90,65),22003:(81, 86),22010:(75,84),22008:(75,74)}
def getfinal(d):
    final = {}
    for k, v in d.items():
        final[k] = v[0] * 0.3 + v[1] * 0.7
    return final
fd = getfinal(studic)
print(fd)
id = int(input("请输入一个学号: "))
if id in fd:
  print(fd[id])
else:
  print("not found")
 
fd_sorted = sorted(fd.items(), key=lambda x: x[1], reverse=True)
print(fd_sorted)
