#!/usr/bin/python
# -*- coding: UTF-8 -*-
#KagurazakaYashi
import sys
import os
import os.path
class Hashrename:
    codemode = True #T:编码，F:解码
    codemethod = "base64" #"base64"/"md5"
    path = [] #文件或文件夹路径
    allyes = False #T:无需确认，F:需要确认
    argumentdict = {}
    alert = ""
    #显示关于信息
    def about(self):
        print "\nYashi Hashrename v1.0" #,sys.argv[0]
        #for i in range(1, len(sys.argv)):
            #print "parameter", i, sys.argv[i]
    #显示英文帮助信息
    def help(self):
        hlp = [
        "usage: "+sys.argv[0]+" [--encoding [base64|md5] | --decoding [base64]] [--file <filename> | --folder <foldername>] [--readonly]",
        "--help [en|cn] | -h [en|cn] :",
        "  Display the help. Default value is en.",
        "--encoding [base64|md5] | -e [base64|md5] :",
        "  Set encoding mode (default). Default value is base64.",
        "--decoding [base64] | -d [base64] :",
        "  Set decoding mode. Default value is base64.",
        "--file <filename> | -i <filename> :",
        "  Rename a file.",
        "--folder <foldername> | -f <foldername> :",
        "  Rename all files in a folder.",
        "--yes | -y :",
        "  no confirmation will follow. Default value is void.",
        " "]
        for i in range(0, len(hlp)):
            print " ",hlp[i]
    #显示中文帮助信息
    def helpcn(self):
        hlp = [
        "使用方法: "+sys.argv[0]+" [--encoding [base64|md5] | --decoding [base64]] [--file <文件名> | --folder <文件夹名>] [--readonly]",
        "--help [en|cn] 或者 -h [en|cn] :",
        "  显示这些帮助信息，添加 cn 可以显示此中文帮助。默认值为英语。",
        "--encoding [base64|md5] 或者 -e [base64|md5] :",
        "  使用指定方式编码（默认）。默认值是 base64 。",
        "--decoding [base64] 或者 -d [base64] :",
        "  使用指定方式解码。默认值是 base64 。",
        "--file <文件名> 或者 -i <文件名> :",
        "  重命名单一文件。",
        "--folder <文件夹名> 或者 -f <文件夹名> :",
        "  重命名一个文件夹中的所有文件。",
        "--yes 或者 -y :",
        "  不进行确认询问，直接进行重命名操作。默认值是需要询问。"
        " "]
        for i in range(0, len(hlp)):
            print " ",hlp[i]
    #程序起点
    def init(self):
        self.about()
        if self.argumentparsing() == False:
            self.argumenterr()
    #处理参数
    def argumentparsing(self):
        argvlen = len(sys.argv)
        if (argvlen == 1):
            return False
        nk = "" #当前得到的参数Key
        nv = "" #当前得到的参数value
        if argvlen > 1:
            for i in range(1, len(sys.argv)):
                nowp = sys.argv[i] #当前参数
                if nk == "": #应输入nk
                    if self.argumentiskey(nowp) == False:
                        return False
                    nk = nowp
                else: #应输入nv
                    if self.argumentiskey(nowp) == True: #这是下一个nk
                        nk = nowp
                        nv = ""
                    else:
                        nv = nowp
                    #print "nk =",nk,"nv =",nv
                    self.argumentdict[nk] = nv
                    nk = ""
                    nv = ""
        return self.argumentkv()
    #判断是否为key
    def argumentiskey(self,key):
        onechar = key[0]
        if onechar == "-":
            return True
        return False
    #处理nknv
    def argumentkv(self):
        keys = self.argumentdict.keys()
        for ni in range(0, len(keys)):
            nk = keys[ni]
            nv = self.argumentdict[nk]
            canstart = True
            if nk == "--help" or nk == "-h":
                canstart = False
                if nv == "" or nv == "en":
                    self.help()
                elif nv == "cn":
                    self.helpcn()
                else:
                    return False
            elif nk == "--encoding" or nk == "-e":
                if self.codemethod != "":
                    return False
                if nv == "base64" or nv == "md5":
                    self.codemethod = nv
                else:
                    return False
            elif nk == "--decoding" or nk == "-d":
                if self.codemethod != "":
                    return False
                if nv == "base64":
                    self.codemethod = nv
                else:
                    return False
            elif nk == "--file" or nk == "-i":
                if len(self.path) > 0:
                    return False
                if os.path.exists(nv) == False:
                    self.alert = "File does not exist."
                    return True
                self.path = [nv]
            elif nk == "--folder" or nk == "-f":
                if len(self.path) > 0:
                    return False
                if os.path.exists(nv) == False:
                    self.alert = "Folder does not exist."
                    return True
                for parent,dirnames,filenames in os.walk(rootdir): #遍历文件夹
                    for filename in filenames:
                        fullpath = os.path.join(parent,filename)
                        self.path.append(fullpath)
                if len(self.path) == 0:
                    self.alert = "Folder is empty."
                    return True
            elif nk == "--yes" or nk == "-y":
                self.allyes = True
            else:
                return False
            if canstart == True and len(self.path) == 0:
                return False
        return True
    #参数错误
    def argumenterr(self):
        print "  No parameter or parameter error."
        self.help()

hobj = Hashrename()
hobj.init()