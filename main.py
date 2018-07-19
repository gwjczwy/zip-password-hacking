import os
import tarfile
import zipfile
import rarfile
import zipfile

def aopen(filename):#万金油版读取文本文件  返回一个list
    for k in ["utf-8",'gb18030', 'ISO-8859-2','gb2312',"gbk"]:#编码集循环
        try:
            f=open(filename,"r",encoding=k)
            txt=f.read()
            f.close()
            return txt.encode(encoding="utf-8",errors="replace").decode('utf-8').split('\n')
        except:
            pass
    raise Exception(filename,'had no way to decode')
pw=aopen(r'E:\PanDownload\绅士密码.txt')

def tryUnzip(filePath,passWord=''):
    print('zip ',passWord)
    zf=zipfile.ZipFile(filePath)
    try:
        zf.extractall(pwd=passWord)
#         print('密码正确',passWord)
        zf.close()
        return True
    except:
#         print('密码错误',passWord)
        return False



def tryUnrar(rarPath,passWord=''):
    print('rar ',passWord)
    r=rarfile.RarFile(rarPath)
    try:
        r.extractall(pwd=passWord)
#         print('正确密码',passWord)
        r.close()
        return True
    except:
        #print('错误密码',passWord)
        return False

def main(filePath,passfile=r'E:\PanDownload\绅士密码.txt'):
    pw=aopen(passfile)
    fileType=filePath[-3:]
#     print('文件类型',fileType)
    if fileType=='zip':  #文件类型判断
        crack=tryUnzip
    elif fileType=='rar':
        crack=tryUnrar
    else:
        print('不支持的文件类型')
        return False
    for p in pw:
        if crack(filePath,passWord=p.encode('utf-8')):
            print('密码是',p)
            break

main(r'E:\PanDownload\123.zip')
# main(filePath=r'E:\PanDownload\123.zip',passfile=)