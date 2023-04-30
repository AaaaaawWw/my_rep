def wordCount(data):
    re={}
    for i in data:
        re[i] = re.get(i,0)+1
    return re

if __name__ =="__main__":
    data = ['ab','ab','cd','s','saf','cd','cd','sb']
    print("The result is %s"%wordCount(data))