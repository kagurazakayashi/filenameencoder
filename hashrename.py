#!/usr/bin/python
# -*- coding: UTF-8 -*-
#KagurazakaYashi
import sys
class Hashrename:
    codemode = True #T:编码，F:解码
    codemethod = "none" #"base64"/"md5"
    filedir = True #T:文件，F:文件夹
    path = "" #文件或文件夹路径
    allyes = True #T:无需确认，F:需要确认
    pathing = False #路径是否完成。T:引号已开始，F:引号已结束
    keys = ["--help","-h","--encoding","-e","--decoding","-d","--file","-i","--folder","-f","--yes","-y"] #可接受参数类型
    #显示关于信息
    def about(self):
        print "\nYashi Hashrename v1.0" #,sys.argv[0]
        for i in range(1, len(sys.argv)):
            print "parameter", i, sys.argv[i]
    #显示英文帮助信息
    def help(self):
        hlp = [
        "usage: "+sys.argv[0]+" [--encoding [base64|md5] | --decoding [base64]] [--file <filename> | --folder <foldername>] [--readonly]",
        "--help [en|cn] | -h [en|cn] :",
        "  Display the help topic.",
        "--encoding [base64|md5] | -e [base64|md5] :",
        "  Set encoding mode.",
        "--decoding [base64] | -d [base64] :",
        "  Set decoding mode.",
        "--file <filename> | -i <filename> :",
        "  Rename a file.",
        "--folder <foldername> | -f <foldername> :",
        "  Rename all files in a folder.",
        "--yes | -y :",
        "  no confirmation will follow.",
        " "]
        for i in range(0, len(hlp)):
            print " ",hlp[i]
    #显示中文帮助信息
    def helpcn(self):
        hlp = [
        "使用方法: "+sys.argv[0]+" [--encoding [base64|md5] | --decoding [base64]] [--file <文件名> | --folder <文件夹名>] [--readonly]",
        "--help [en|cn] 或者 -h [en|cn] :",
        "  显示这些帮助信息，添加cn可以显示此中文帮助。",
        "--encoding [base64|md5] 或者 -e [base64|md5] :",
        "  使用指定方式编码。",
        "--decoding [base64] 或者 -d [base64] :",
        "  使用指定方式解码。",
        "--file <文件名> 或者 -i <文件名> :",
        "  重命名单一文件。",
        "--folder <文件夹名> 或者 -f <文件夹名> :",
        "  重命名一个文件夹中的所有文件。",
        "--yes 或者 -y :",
        "  不进行确认询问，直接进行重命名操作。"
        " "]
        for i in range(0, len(hlp)):
            print " ",hlp[i]
    #程序起点
    def init(self):
        self.about()
        if (self.argumentparsing() == False):
            self.argumenterr()
    #处理参数
    def argumentparsing(self):
        argvlen = len(sys.argv)
        if (argvlen == 1):
            return False
        nk = ""
        nv = ""
        if (argvlen > 1):
            for i in range(1, len(sys.argv)):
                nowp = sys.argv[i] #当前参数
                if (nk == ""): #应输入nk
                    for i in range(0, len(self.keys)):
                        nowip = self.keys[i] #当前待比对内置参数
                        if (nowp == nowip):
                            nk = nowp
                            break
                    if (nk == ""): #没有nk
                        return False
                else: #应输入nv
                    nv = nowp

        return True
    #参数错误
    def argumenterr(self):
        print "  No parameter or parameter error."
        self.help()

hobj = Hashrename()
hobj.init()