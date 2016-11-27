## Filenameencoder

非英文字符文件名.jpg -> Filenameencoder rename -> 6Z2e6Iux5paH5a2X56ym5paH5Lu25ZCN.jpg -> Filenameencoder rename -> 非英文字符文件名.jpg

###Usage:

filenameencoder.py \[\[--encoding [disable|base64|md5|sha1] | --decoding [disable|base64]] \[--file "filename" | --folder "foldername"] \[--readonly] \[--hiddenfiles] \[--yes] \[--readencode [auto|utf-8|mbcs|gbk|...]] [--writeencode [auto|utf-8|mbcs|gbk|...]]

Enter "filenameencoder.py --help" to get help.

-  --help [en|cn] | -h [...] | /? [...]:
-    Display the help. Default value is en.
-  --encode [disable|base64|md5|sha1] | -e [...] | /e [...] :
-    Set encoding mode (default). Default value is disable.
-  --decode [disable|base64] | -d [...] | /d [...] :
-    Set decoding mode. Default value is disable.
-  --file "filename" | -i "filename" | /i "filename" :
-    Rename a file.
-  --folder "foldername" | -f "foldername" | /f "foldername" :
-    Rename all files in a folder.
-  --hiddenfiles | -s | /s :
-    Include hidden files. Default value is void (not included).
-  --yes | -y | /y :
-    No confirmation will follow. Default value is void (no).
-  --readencode [auto|utf-8|mbcs|gbk|...] | -r [...] | /r [...] :
-    (Advanced) Read file name using encoding. Default value is auto.
-  --writeencode [auto|utf-8|mbcs|gbk|...] | -w [...] | /w [...] :
-    (Advanced) Write file name using encoding. Default value is auto.

###使用方法:

filenameencoder.py \[\[--encoding [disable或base64或md5或sha1]或者--decoding [disable或base64]] \[--file "文件名"或者--folder "文件夹名"] \[--readonly] \[--hiddenfiles] \[--yes] \[--readencode [auto或utf-8或mbcs或gbk或...]] [--writeencode [auto或utf-8或mbcs或gbk或...]]

-  --help [en或cn] 或者 -h [...] 或者 /? [...] :
-    显示这些帮助信息，添加 cn 可以显示此中文帮助。默认值为英语。
-  --encode [disable或base64或md5或sha1] 或者 -e [...] 或者 /e [...] :
-    使用指定方式编码（默认）。默认值是 disable 。
-  --decode [disable或base64] 或者 -d [...] 或者 /d [...] :
-    使用指定方式解码。默认值是 disable 。
-  --file "文件名" 或者 -i "文件名" /i "文件名" :
-    重命名单一文件。
-  --folder "文件夹名" 或者 -f "文件夹名" 或者 /f "文件夹名" :
-    重命名一个文件夹中的所有文件。
-  --hiddenfiles 或者 -s 或者 /s :
-    包含隐藏文件。默认值是不包含隐藏文件。
-  --yes 或者 -y 或者 /y :
-    不进行确认询问，直接进行重命名操作。默认值是需要询问。
-  --readencode [auto或utf-8或mbcs或gbk或...] 或者 -r [...] 或者 /r [...] :
-    (高级选项)指定读取文件名时使用的字符编码。默认值为自动。
-  --writeencode [auto或utf-8或mbcs或gbk或...] 或者 -w [...] 或者 /w [...] :
-    (高级选项)指定写入文件名时使用的字符编码。默认值为自动。

###e.g. / 使用示范 :

- command$ python filenameencoder.py -e base64 -f test/
- *. /Users/KagurazakaYashi/filenameencoder/test/.DS_Store
- -> Skip hidden file.
- 1. /Users/KagurazakaYashi/filenameencoder/test/重命名测试文件1.test
- -> /Users/KagurazakaYashi/filenameencoder/test/5rWL6K+V5pWw5o2uMQ==.test
- 2. /Users/KagurazakaYashi/filenameencoder/test/重命名测试文件2.test
- -> /Users/KagurazakaYashi/filenameencoder/test/5rWL6K+V5pWw5o2uMg==.test
- 2 Ready, 1 Skip, 3 Total
- Start rename (y/N)? :y
- Start rename ...
- 1. /Users/KagurazakaYashi/filenameencoder/test/重命名测试文件1.test
- -> /Users/KagurazakaYashi/filenameencoder/test/5rWL6K+V5pWw5o2uMQ==.test
- -> OK.
- 2. /Users/KagurazakaYashi/filenameencoder/test/重命名测试文件2.test
- -> /Users/KagurazakaYashi/filenameencoder/test/5rWL6K+V5pWw5o2uMg==.test
- -> OK.
- 2 OK, 0 Fail, 1 Skip, 3 Total.


- command$ python filenameencoder.py -d base64 -f test/
- *. /Users/KagurazakaYashi/filenameencoder/test/.DS_Store
- -> Skip hidden file.
- 1. /Users/KagurazakaYashi/filenameencoder/test/5rWL6K+V5pWw5o2uMg==.test
- -> /Users/KagurazakaYashi/filenameencoder/test/重命名测试文件2.test
- 2. /Users/KagurazakaYashi/filenameencoder/test/5rWL6K+V5pWw5o2uMQ==.test
- -> /Users/KagurazakaYashi/filenameencoder/test/重命名测试文件1.test
- 2 Ready, 1 Skip, 3 Total
- Start rename (y/N)? :y
- Start rename ...
- 1. /Users/KagurazakaYashi/filenameencoder/test/5rWL6K+V5pWw5o2uMg==.test
- -> /Users/KagurazakaYashi/filenameencoder/test/重命名测试文件2.test
- -> OK.
- 2. /Users/KagurazakaYashi/filenameencoder/test/5rWL6K+V5pWw5o2uMQ==.test
- -> /Users/KagurazakaYashi/filenameencoder/test/重命名测试文件1.test
- -> OK.
- 2 OK, 0 Fail, 1 Skip, 3 Total.