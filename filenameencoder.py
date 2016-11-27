#!/usr/bin/python
# -*- coding: UTF-8 -*-
# KagurazakaYashi
# 非英文字符文件名.jpg -> Filenameencoder rename -> 6Z2e6Iux5paH5a2X56ym5paH5Lu25ZCN.jpg -> Filenameencoder rename -> 非英文字符文件名.jpg
import sys
import os
import os.path
import base64
import platform
import hashlib
class Filenameencoder:
    argv =  [] #可以在init前配置此属性以接入使用
    codemode = True #T:编码，F:解码
    codemethod = "" #"disable"/"base64"/"md5"
    path = [] #文件或文件夹路径
    allyes = False #T:无需确认，F:需要确认
    argumentdict = {}
    alert = ""
    hiddenfile = False #T:不隐藏文件，F:包含隐藏文件。同时适用于Unix和NT
    readencoding = None
    writeencoding = None
    systemencoding = ""
    #显示关于信息
    def about(self):
        print "\nYashi Filenameencoder v1.2 for py2" #,self.argv[0]
    def __init__(self):
        self.argv = sys.argv
        self.codemode = True
        self.codemethod = "disable"
        self.path = []
        self.allyes = False
        self.argumentdict = {}
        self.alert = ""
        self.hiddenfile = False
        self.readencoding = None
        self.writeencoding = None
        self.systemencoding = sys.getfilesystemencoding()
    def minihelp(self):
        print "\n  usage: "+self.argv[0]+" [[--encoding [disable|base64|md5|sha1] | --decoding [disable|base64]] [--file <filename> | --folder <foldername>] [--readonly] [--hiddenfiles] [--yes] [--readencode [auto|utf-8|mbcs|gbk|...]] [--writeencode [auto|utf-8|mbcs|gbk|...]]\n"
        print "  Enter \""+self.argv[0]+" --help\" to get help."
        print "  --help [en|cn] | -h [en|cn] | /? [en|cn]:\n"
    #显示英文帮助信息
    def help(self):
        hlp = [
        "\nusage: "+self.argv[0]+" [[--encoding [disable|base64|md5|sha1] | --decoding [disable|base64]] [--file <filename> | --folder <foldername>] [--readonly] [--hiddenfiles] [--yes] [--readencode [auto|utf-8|mbcs|gbk|...]] [--writeencode [auto|utf-8|mbcs|gbk|...]]\n",
        "--help [en|cn] | -h [...] | /? [...]:",
        "  Display the help. Default value is en.",
        "--encode [disable|base64|md5] | -e [...] | /e [...] :",
        "  Set encoding mode (default). Default value is disable.",
        "--decode [disable|base64] | -d [...] | /d [...] :",
        "  Set decoding mode. Default value is disable.",
        "--file <filename> | -i <filename> | /i <filename> :",
        "  Rename a file.",
        "--folder <foldername> | -f <foldername> | /f <foldername> :",
        "  Rename all files in a folder.",
        "--hiddenfiles | -s | /s :",
        "  Include hidden files. Default value is void (not included).",
        "--yes | -y | /y :",
        "  No confirmation will follow. Default value is void (no).",
        "--readencode [auto|utf-8|mbcs|gbk|...] | -r [...] | /r [...] :",
        "  (Advanced) Read file name using encoding. Default value is auto.",
        "--writeencode [auto|utf-8|mbcs|gbk|...] | -w [...] | /w [...] :",
        "  (Advanced) Write file name using encoding. Default value is auto.",
        "\ne.g. :"]
        self.helpview(hlp+self.helpdemo(),"Press Enter to continue")
    #显示中文帮助信息
    def helpcn(self):
        hlp = [
        "\n使用方法: "+self.argv[0]+" [[--encoding [disable或base64或md5或sha1]或者--decoding [disable或base64]] [--file <文件名>或者--folder <文件夹名>] [--readonly] [--hiddenfiles] [--yes] [--readencode [auto或utf-8或mbcs或gbk或...]] [--writeencode [auto或utf-8或mbcs或gbk或...]]\n",
        "--help [en或cn] 或者 -h [...] 或者 /? [...] :",
        "  显示这些帮助信息，添加 cn 可以显示此中文帮助。默认值为英语。",
        "--encode [disable或base64或md5或sha1] 或者 -e [...] 或者 /e [...] :",
        "  使用指定方式编码（默认）。默认值是 disable 。",
        "--decode [disable或base64] 或者 -d [...] 或者 /d [...] :",
        "  使用指定方式解码。默认值是 disable 。",
        "--file <文件名> 或者 -i <文件名> /i <文件名> :",
        "  重命名单一文件。",
        "--folder <文件夹名> 或者 -f <文件夹名> 或者 /f <文件夹名> :",
        "  重命名一个文件夹中的所有文件。",
        "--hiddenfiles 或者 -s 或者 /s :",
        "  包含隐藏文件。默认值是不包含隐藏文件。",
        "--yes 或者 -y 或者 /y :",
        "  不进行确认询问，直接进行重命名操作。默认值是需要询问。",
        "--readencode [auto或utf-8或mbcs或gbk或...] 或者 -r [...] 或者 /r [...] :",
        "  (高级选项)指定读取文件名时使用的字符编码。默认值为自动。",
        "--writeencode [auto或utf-8或mbcs或gbk或...] 或者 -w [...] 或者 /w [...] :",
        "  (高级选项)指定写入文件名时使用的字符编码。默认值为自动。",
        "\n使用示范："]
        self.helpview(hlp+self.helpdemo(),"按回车键继续")
    def helpdemo(self):
        t1 = "/Users/KagurazakaYashi/filenameencoder/test/"
        t2 = "-> "
        t3 = "重命名测试文件"
        t4 = ".test"
        t5 = "5rWL6K+V5pWw5o2uMQ=="
        t6 = "5rWL6K+V5pWw5o2uMg=="
        t7 = "$"
        if 'Windows' in platform.system():
            t7 = ">"
        t7 = "command"+t7+" python "+self.argv[0]+" "
        dmo = [
            t7+"-e base64 -f test/",
            "*. "+t1+".DS_Store",
            t2+"Skip hidden file.",
            "1. "+t1+t3+"1"+t4,
            t2+t1+t5+t4,
            "2. "+t1+t3+"2"+t4,
            t2+t1+t6+t4,
            "2 Ready, 1 Skip, 3 Total",
            "Start rename (y/N)? :y",
            "Start rename ...",
            "1. "+t1+t3+"1"+t4,
            t2+t1+t5+t4,
            t2+"OK.",
            "2. "+t1+t3+"2"+t4,
            t2+t1+t6+t4,
            t2+"OK.",
            "2 OK, 0 Fail, 1 Skip, 3 Total.\n",
            t7+"-d base64 -f test/",
            "*. "+t1+".DS_Store",
            t2+"Skip hidden file.",
            "1. "+t1+t6+t4,
            t2+t1+t3+"2"+t4,
            "2. "+t1+t5+t4,
            t2+t1+t3+"1"+t4,
            "2 Ready, 1 Skip, 3 Total",
            "Start rename (y/N)? :y",
            "Start rename ...",
            "1. "+t1+t6+t4,
            t2+t1+t3+"2"+t4,
            t2+"OK.",
            "2. "+t1+t5+t4,
            t2+t1+t3+"1"+t4,
            t2+"OK.",
            "2 OK, 0 Fail, 1 Skip, 3 Total."]
        for i in range(0, len(dmo)):
            dmo[i] = "| "+dmo[i]
        return dmo
    def helpview(self,hlp,pause):
        for i in range(0, len(hlp)):
            if i%15 == 0 and i != 0:
                content = raw_input("["+pause+"]")
            codestr = self.strencode("  "+hlp[i],"utf-8",self.systemencoding)
            if codestr != None:
                print codestr
    #文件编码
    def strencode(self,istr,rcode,wcode):
        if istr == "" or istr == None:
            return istr
        if rcode == None and wcode == None:
            return istr
        estr = istr
        dstr = istr
        try:
            if rcode != None:
                dstr = istr.decode(rcode)
            if wcode != None:
                estr = dstr.encode(wcode)
        except Exception,e:
            print "[ERROR]",e
        return estr
    #程序起点
    def init(self):
        self.about()
        if self.argumentparsing() == False:
            self.argumenterr()
        elif self.alert != "":
            print self.alert
        else:
            self.filenamepreview()
    #处理参数
    def argumentparsing(self):
        argvlen = len(self.argv)
        if (argvlen == 1):
            return False
        nk = "" #当前得到的参数Key
        nv = "" #当前得到的参数value
        if argvlen > 1:
            #print "self.argv =",self.argv
            for i in range(1, len(self.argv)):
                nowp = self.argv[i] #当前参数
                if nk == "": #应输入nk
                    if self.argumentiskey(nowp) == False:
                        return False
                    nk = nowp
                else: #应输入nv
                    if self.argumentiskey(nowp) == True: #这是下一个nk
                        self.argumentdict[nk] = nv
                        nk = nowp
                        nv = ""
                    else:
                        nv = nowp
                    #print "nk =",nk,"nv =",nv
                    self.argumentdict[nk] = nv
                    nk = ""
                    nv = ""
        if nk != "":
            self.argumentdict[nk] = nv
        return self.argumentkv()
    #判断是否为key
    def argumentiskey(self,key):
        onechar = key[0]
        if onechar == "-" or onechar == "/":
            return True
        return False
    #处理nknv
    def argumentkv(self):
        keys = self.argumentdict.keys()
        for ni in range(0, len(keys)):
            nk = keys[ni]
            nv = self.argumentdict[nk]
            #print "nk =",nk,"nv =",nv
            canstart = True
            if nk == "--help" or nk == "-h" or nk == "/?":
                canstart = False
                if nv == "" or nv == "en":
                    self.help()
                elif nv == "cn":
                    self.helpcn()
                self.alert = " "
                return True
            elif nk == "--hiddenfiles" or nk == "-s" or nk == "/s":
                self.hiddenfile = True
            elif nk == "--encoding" or nk == "-e":
                if nv == "base64" or nv == "md5" or nv == "sha1" or nv == "disable":
                    self.codemethod = nv
                else:
                    return False
            elif nk == "--decoding" or nk == "-d" or nk == "/d":
                self.codemode = False
                if nv == "base64" or nv == "disable":
                    self.codemethod = nv
                else:
                    return False
            elif nk == "--file" or nk == "-i" or nk == "/i":
                if len(self.path) > 0:
                    return False
                if os.path.exists(nv) == False:
                    self.alert = "[ERROR] File does not exist."
                    return True
                #相对路径转绝对路径
                fullpath = os.path.abspath(nv)
                self.path = [self.splitpath(fullpath)]
            elif nk == "--folder" or nk == "-f" or nk == "/f":
                if len(self.path) > 0:
                    return False
                if os.path.exists(nv) == False:
                    self.alert = "[ERROR] Folder does not exist."
                    return True
                for parent,dirnames,filenames in os.walk(nv): #遍历文件夹
                    for filename in filenames:
                        fullpath = os.path.abspath(os.path.join(parent,filename))
                        self.path.append(self.splitpath(fullpath))
                if len(self.path) == 0:
                    self.alert = "[ERROR] Folder is empty."
                    return True
            elif nk == "--readencode" or nk == "-r" or nk == "/r":
                if nv != "auto" or nv != "":
                    self.readencoding = nv
            elif nk == "--writeencode" or nk == "-w" or nk == "/w":
                if nv != "auto" or nv != "":
                    self.writeencoding = nv
            elif nk == "--yes" or nk == "-y" or nk == "/y":
                self.allyes = True
            elif nk == "-test":
                print "Test Mode"
            else:
                return False
        if canstart == True and len(self.path) == 0:
            return False
    #路径拆分
    def splitpath(self,fullpath):
        dir,file=os.path.split(fullpath)
        filename,extname=os.path.splitext(file)
        return [dir,filename,extname]
    #参数错误
    def argumenterr(self):
        print "  No parameter or parameter error."
        self.minihelp()
    #转换开始
    def filenamepreview(self):
        renamep = []
        skipfile = 1
        total = len(self.path)
        skip = 0
        ready = 0
        for i in range(0, total):
            path = self.path[i]
            dir = self.strencode(path[0],self.readencoding,self.writeencoding)
            if dir == None:
                return False
            filename = self.strencode(path[1],self.readencoding,self.writeencoding)
            if filename == None:
                return False
            extname = self.strencode(path[2],self.readencoding,self.writeencoding)
            if extname == None:
                return False
            cfilename = self.strencode(self.filenamecode(filename),self.readencoding,self.writeencoding)
            if cfilename == None:
                return False
            elif cfilename == "":
                print "[ERROR] File name code failed."
                return False
            elif cfilename == "MD":
                print "[ERROR] Irreversible algorithm."
                return False
            oldp = os.path.join(path[0],path[1]+path[2])
            newp = os.path.join(dir,cfilename+extname)
            if self.hiddenfile == False and self.isHidenFile(oldp,filename) == True:
                print "*.",oldp
                skipfile = skipfile - 1
                skip = skip + 1
                print "-> Skip hidden file."
            else:
                print str(i+skipfile)+".",oldp
                print "->",newp
                ready = ready + 1
                renamep.append([oldp,newp])
        content = "y"
        print str(ready),"Ready,",str(skip),"Skip,",str(total),"Total"
        if self.allyes == False:
            content = raw_input("Start rename (y/N)? :")
        if content != "y" and content != "Y":
            print "NO."
            return False
        self.startrename(renamep,skip)
    #开始重命名
    def startrename(self,renamep,skip):
        print "Start rename ..."
        oki = 0
        faili = 0
        total = len(renamep)
        for i in range(0, total):
            nowrenamep = renamep[i]
            oldp = nowrenamep[0]
            newp = nowrenamep[1]
            print str(i+1)+".",oldp
            print "->",newp
            result = "OK."
            try:
                os.rename(oldp,newp)
                oki = oki + 1
            except Exception,e:
                faili = faili + 1
                result = e
            print "->",result
        print str(oki),"OK,",str(faili),"Fail,",str(skip),"Skip,",str(total+skip),"Total."
    #文件名编码
    def filenamecode(self,filename):
        if self.codemethod == "base64":
            if self.codemode == True:
                newstr = ""
                try:
                    newstr = base64.b64encode(filename)
                except Exception,e:
                    print "[ERROR]",e
                return newstr
            else:
                newstr = ""
                try:
                    missing_padding = 4 - len(filename) % 4 #需要补齐等号
                    if missing_padding:
                        filename += b'='* missing_padding
                    newstr = base64.decodestring(filename)
                except Exception,e:
                    print "[ERROR]",e
                return newstr
        elif self.codemethod == "md5":
            if self.codemode == True:
                newstr = ""
                try:
                    md5o = hashlib.md5()
                    md5o.update(filename)
                    newstr = md5o.hexdigest()
                except Exception,e:
                    print "[ERROR]",e
                return newstr
            else:
                return ""
        elif self.codemethod == "sha1":
            if self.codemode == True:
                newstr = ""
                try:
                    md5o = hashlib.sha1()
                    md5o.update(filename)
                    newstr = md5o.hexdigest()
                except Exception,e:
                    print "[ERROR]",e
                return newstr
            else:
                return ""
        elif self.codemethod == "disable":
            return filename
        else:
            print "[ERROR] Mode error."
    #判断是否为隐藏文件
    def isHidenFile(self,filePath,filename):
        if 'Windows' in platform.system(): #Windows
        	p = os.popen('attrib ' + filePath)
        	pr = p.readlines()[0][4]
        	p.close()
        	if pr == "H":
        		return True
        	return False
            #import win32file,win32con
            #fileAttr = win32file.GetFileAttributes(filePath)
            #if fileAttr & win32con.FILE_ATTRIBUTE_HIDDEN :
                #return True
            #return False
        else:
            return filename.startswith('.') #linux

#自检
class FilenameencoderTester:
    tmpfile = "FilenameencoderTestFile.tmp"
    b64file = "RmlsZW5hbWVlbmNvZGVyVGVzdEZpbGU=.tmp"
    md5file = "305862a11a46f7bcc2173cbf67f9f8f5.tmp"
    shafile = "afbe0ed6eab11f2dd4f8a0146af67490d7145707.tmp"
    test = "[TEST]"
    oki = 0
    ali = 0
    def init(self):
        print self.test,"= = = TEST MODE = = ="
        print self.test,"System encode:",sys.getfilesystemencoding()
        targv = sys.argv
        for i in range(0, len(targv)):
            print self.test,"input-parameter", i, targv[i]
        self.createfile()
        print self.test,"Test base64 encode..."
        nargv = [targv[0],"-e","base64","-i",self.tmpfile,"-y"]
        self.starttest(nargv)
        self.checkfile(self.b64file)
        print self.test,"Test base64 decode..."
        nargv = [targv[0],"-d","base64","-i",self.b64file,"-y"]
        self.starttest(nargv)
        self.checkfile(self.tmpfile)
        nargv = [targv[0],"-e","md5","-i",self.tmpfile,"-y"]
        self.starttest(nargv)
        self.checkfile(self.md5file)
        nargv = [targv[0],"-e","sha1","-i",self.md5file,"-y"]
        self.starttest(nargv)
        self.checkfile(self.shafile)
        self.deletefile(self.shafile)
        print self.test,"OK =",str(self.oki),"/",str(self.ali)
        if self.oki == self.ali:
            print self.test,"*ALLOK."
        else:
            print self.test,"*FAIL."
    def starttest(self,nargv):
        for i in range(0, len(nargv)):
            print self.test,"new-parameter", i, nargv[i]
        print self.test,"Init..."
        pobj = Filenameencoder()
        pobj.argv = nargv
        pobj.init()
        pobj = None
        print self.test,"Release."
    def createfile(self):
        print self.test,"createfile",self.tmpfile,"..."
        try:
            f = open(self.tmpfile,'w')
            f.write("0")
            f.close()
            print self.test,"OK."
        except Exception,e:
            print self.test,e
            exit()
    def deletefile(self,filename):
        print self.test,"deletefile",filename,"..."
        try:
            os.remove(filename)
            print self.test,"OK."
        except Exception,e:
            print self.test,e
            exit()
    def checkfile(self,filename):
        self.ali = self.ali + 1
        print self.test,"checkfile",filename,"..."
        t = ""
        try:
            f = open(filename,'r')
            t = f.readline()
            f.close()
        except Exception,e:
            print self.test,e
            exit()
        if t != "0":
            print self.test,"Check failed."
            exit()
        else:
            self.oki = self.oki + 1
            print self.test,"OK."

#程序执行
if len(sys.argv) >= 2 and sys.argv[1] == "-test":
    tobj = FilenameencoderTester()
    tobj.init()
else:
    pobj = Filenameencoder()
    pobj.init()
exit()