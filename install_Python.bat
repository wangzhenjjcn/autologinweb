@echo off
:install
ECHO Start to install python2.76 win32......
start /wait ./tmp/python-3.7.2.exe 
ECHO install python2.76 successfully......
echo start to set python sys path....... 
echo %path%|findstr /i "python37"&&(goto run)  
goto install


:run




echo start to install pip....... 
start /wait  python ./tmp/get-pip.py  
start /wait pip install pyinstaller -i https://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
echo install pip successfully....... 
pause;



start /wait pip install -r requirements
pause;