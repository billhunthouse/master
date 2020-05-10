#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Bill
# @Software: PyCharm

from pathlib import *

#1.使用windows风格的路径

pp = PurePath('setup.py')
print(type(pp))
pp = PurePath('crazy','some/path','info')
print(pp)
#输出windows风格的路径符号，正斜杠：crazy\some\path\info

#2.使用unix风格的路径：posix
pp = PurePosixPath('crazy','some/path','info')
print(pp)
#输出路径符号为反斜杠：crazy/some/path/info


#3.如果包含多个根路径，则默认使用最后一个。
pp = PurePosixPath('/etc','/usr','info')
print(pp)  #输出信息：  扔掉/etc     /usr/info
pp = PureWindowsPath('C:/windows','D:info')
print(pp)   #输出信息：  D:info

pp = PureWindowsPath('C:\windows',':\programmer file')
print(pp) #C:\windows\:\programmer file

#4.路径中的多余的斜杠和点会被忽略，但是两个点不会，代表了上一级目录
pp = PurePath('foo//bar')
print(pp)
pp = PurePath('foo/./bar')
print(pp)
pp = PurePath('foo/../bar')
print(pp) # foo\..\bar

#5.比较同一系统下大小写是否一致，也可以比较大小写
print(PurePosixPath('info')  == PurePosixPath('INFO'))
print(PurePosixPath('info')  == PureWindowsPath('INFO'))
print(PureWindowsPath('info')  == PureWindowsPath('INFO')) #window
print(PurePosixPath('info')  == PureWindowsPath('info'))
