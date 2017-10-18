#1. Linux课程实验

## 1.1 Linux系统的安装
本文主要介绍Windows环境下安装Ubuntu14.04双系统，虚拟机安装Ubuntu14.04可参考[虚拟机安装Ubuntu14.04](http://blog.csdn.net/u013142781/article/details/50529030)
###1.1.1 前期准备
1、大于2G的U盘一个(我的系统盘制作完成后大约占1个多G的容量)

2、已下载好的Ubuntu安装文件(选择在官网下载,有32和64位选择)

3、已安装好UltraISO软件的电脑(UltraISO安装包自行百度)

4、打算安装Ubuntu的电脑(我的电脑已安装好64位Win7系统)
###1.1.2 UltraISO制作Ubuntu14.04的系统启动盘
1、打开UltraISO,将Ubuntu14.04的系统文件制作成U盘启动,过程大概2分钟,十分简单,不懂得直接度娘教给你,不在过多介绍
###1.1.3 Ubuntu14.04系统安装及设置
1、右键点击我的电脑》管理》磁盘管理,选择一个空间较大的盘,右键选择压缩卷,为Ubuntu14.04划分了80G的空间(空间大小根据自己的需要自行选择,建议如果只是安装作为练习使用有30G就可以,要是自己有运行的程序或者要处理数据还是建议多分一点空间),设置好容量大小后点压缩即可,不用给他设置盘符,我们在安装Ubuntu的时候在重新分区。
![installubuntu1](img/installubuntu1.jpg)



2、将Ubuntu的启动插在电脑上,重启电脑,开机时按F12,选择U盘启动
![installubuntu2](img/installubuntu2.jpg)


3、选择U盘启动后,进入Ubuntu的安装界面,选择语言》中文(简体),点击安装Ubuntu
![installubuntu3](img/installubuntu3.jpg)


4、准备安装Ubuntu,可以联网,也可以不联网,如果联网选择安装第三方软件及更新,也可以选择不安装,安装完成后再系统里选择更新,完成后点击继续
![installubuntu4](img/installubuntu4.jpg)


5、安装类型选择,这里一定选择》其他选项》继续,这样我们可以自己分区
![installubuntu5](img/installubuntu5.jpg)


6、分区设置,如图选中空闲分区,也就是我们之前在Win7下划分出的80G的空间

![installubuntu6](img/installubuntu6.jpg)

7、新建分区,点击“+”,设置交换空间swap,如果电脑内存是8G可以划分给8G,一般不大于物理内存就行

![installubuntu7](img/installubuntu7.jpg)

8、新建分区,点击“+”,设置Ubuntu启动引导区,一般划分200Mb足够了
![installubuntu8](img/installubuntu8.jpg)


9、新建分区,点击“+”,设置“/”主分区,相当于Win7的系统C盘,同样的方法,将剩余空间设置“/home”分区,用于存在文件。重要的一点是在安装启动引导设备选择前面划分的/boot盘

![installubuntu9](img/installubuntu9.jpg)
![installubuntu10](img/installubuntu10.jpg)
![installubuntu11](img/installubuntu11.jpg)

10、进入用户设置,自行设置用户名、密码

![installubuntu12](img/installubuntu12.jpg)

11、进入安装界面,等待安装更新
![installubuntu13](img/installubuntu13.jpg)

12、安装完成后用你设置的用户名密码进入,重新启动计算机。


## 1.2 Linux常用命令
```
ls　　            显示文件或目录
     -l           列出文件详细信息l(list)
     -a           列出当前目录下所有文件及目录，包括隐藏的a(all)
mkdir             创建目录
     -p           创建目录，若无父目录，则创建p(parent)
cd                切换目录
touch             创建空文件
echo              创建带有内容的文件。
cat               查看文件内容
cp                拷贝
mv                移动或重命名
rm                删除文件
     -r           递归删除，可删除子目录及文件
     -f           强制删除
find              在文件系统中搜索某文件
wc                统计文本中行数、字数、字符数
grep              在文本文件中查找某个字符串
rmdir             删除空目录
tree              树形结构显示目录，需要安装tree包
pwd               显示当前目录
ln                创建链接文件
more、less        分页显示文本文件内容
head、tail        显示文件头、尾内容
ctrl+alt+F1       命令行全屏模式
 
系统管理命令
stat              显示指定文件的详细信息，比ls更详细
who               显示在线登陆用户
whoami            显示当前操作用户
hostname          显示主机名
uname             显示系统信息
top               动态显示当前耗费资源最多进程信息
ps                显示瞬间进程状态 ps -aux
du                查看目录大小 du -h /home带有单位显示目录信息
df                查看磁盘大小 df -h 带有单位显示磁盘信息
ifconfig          查看网络情况
ping              测试网络连通
netstat           显示网络状态信息
man               命令不会用了，找男人  如：man ls
clear             清屏
alias             对命令重命名 如：alias showmeit="ps -aux" ，另外解除使用unaliax showmeit
kill              杀死进程，可以先用ps 或 top命令查看进程的id，然后再用kill命令杀死进程。
打包压缩相关命令
gzip：
bzip2：
tar:                 打包压缩
     -c              归档文件
     -x              压缩文件
     -z              gzip压缩文件
     -j              bzip2压缩文件
     -v              显示压缩或解压缩过程 v(view)
     -f              使用档名
例：
tar -cvf /home/abc.tar /home/abc            只打包，不压缩
tar -zcvf /home/abc.tar.gz /home/abc        打包，并用gzip压缩
tar -jcvf /home/abc.tar.bz2 /home/abc       打包，并用bzip2压缩
当然，如果想解压缩，就直接替换上面的命令  tar -cvf  / tar -zcvf  / tar -jcvf 中的“c” 换成“x” 就可以了。
 
关机/重启机器
shutdown
     -r             关机重启
     -h             关机不重启
     now            立刻关机
halt                关机
reboot              重启
```
##1.3 Linux常见问题的解决方案

**1. Ubuntu使用apt-get时提示>”E: You must put some ‘source’ URIs in your sources.list”。**

解决方法
```
sudo sed -i -- 's/#deb-src/deb-src/g' /etc/apt/sources.list && sudo sed -i -- 
's/# deb-src/deb-src/g' /etc/apt/sources.list
sudo apt-get update
```
**2 vim配置**

不错的方案：https://github.com/ma6174/vim

在用户目录下新建.vimrc,保存即可生效。若想对所有用户生效，可直接修改/etc/vimrc.
```
set nocompatible    " 关闭 vi 兼容模式
syntax on           " 自动语法高亮
colorscheme molokai " 设定配色方案
set number          " 显示行号
set cursorline      " 突出显示当前行
set ruler           " 打开状态栏标尺
set shiftwidth=4    " 设定 << 和 >> 命令移动时的宽度为 4
set softtabstop=4   " 使得按退格键时可以一次删掉 4 个空格
set tabstop=4       " 设定 tab 长度为 4
set nobackup        " 覆盖文件时不备份
set autochdir       " 自动切换当前目录为当前文件所在的目录
filetype plugin indent on " 开启插件
set backupcopy=yes  " 设置备份时的行为为覆盖
set ignorecase smartcase " 搜索时忽略大小写，但在有一个或以上大写字母时仍保持对大小写敏感
set nowrapscan      " 禁止在搜索到文件两端时重新搜索
set incsearch       " 输入搜索内容时就显示搜索结果
set hlsearch        " 搜索时高亮显示被找到的文本
set noerrorbells    " 关闭错误信息响铃
set novisualbell    " 关闭使用可视响铃代替呼叫
set t_vb=           " 置空错误铃声的终端代码
" set showmatch     " 插入括号时，短暂地跳转到匹配的对应括号
" set matchtime=2   " 短暂跳转到匹配括号的时间
set magic           " 设置魔术
set hidden          " 允许在有未保存的修改时切换缓冲区，此时的修改由 vim 负责保存
set guioptions-=T    " 隐藏工具栏
set guioptions-=m   " 隐藏菜单栏
set smartindent     " 开启新行时使用智能自动缩进
set backspace=indent,eol,start
                    " 不设定在插入状态无法用退格键和 Delete 键删除回车符
set cmdheight=1     " 设定命令行的行数为 1
set laststatus=2    " 显示状态栏 (默认值为 1, 无法显示状态栏)
set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ %c:%l/%L%)\ 
" 设置在状态行显示的信息
set foldenable " 开始折叠
set foldmethod=syntax " 设置语法折叠
set foldcolumn=0 " 设置折叠区域的宽度
setlocal foldlevel=1 " 设置折叠层数为
" set foldclose=all " 设置为自动关闭折叠 
" nnoremap <space> @=((foldclosed(line('.')) < 0) ? 'zc' : 'zo')<CR>
" 用空格键来开关折叠
```
**3. 用apt-get安装时，提示：E could not get lock /vaa/lib/dpkg/lock -open等**
```
reasons :可能是由于上次使用apt-get install 时，未能成功安装便强制结束了。
solutions: 
sudo rm /var/cache/apt/archives/lock 
sudo rm /var/lib/dpkg/lock
```
**4. 常用软件安装**

安装chrome

```
添加签名密钥： 
wget -q -O - http://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
添加软件源： 
sudo sh -c ‘echo “deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main” >> /etc/apt/sources.list.d/google.list’
安装chrome 
sudo apt-get update 
sudo apt-get install google-chrome-stable
```

有道词典
```
百度有道词典，进入有道首页，点“下载词典客户端”，下载对应版本。
打开终端，进入下载目录，输入sudo dpkg -i youdao-dict_1.0.2~ubuntu_amd64.deb
```
notepadqq

在Ubuntu / Ubuntu Kylin下安装和卸载 Nodepadqq 
对于Ubuntu发行版本可以通过PPA安装，命令如下：
```
sudo add-apt-repository ppa:notepadqq-team/notepadqq
sudo apt-get update
sudo apt-get install notepadqq
           类似的，卸载命令如下：
sudo apt-get remove notepadqq
sudo add-apt-repository --remove ppa:notepadqq-team/notepadqq
```

cmake 编译

[ ] 添加调试信息,在CMakeList.txt中添加以下内容：
```
SET(CMAKE_BUILD_TYPE "Debug")  
SET(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -O0 -Wall -g2 -ggdb")  
SET(CMAKE_CXX_FLAGS_RELEASE "$ENV{CXXFLAGS} -O3 -Wall")  
```

##1.4 Shell编程实验
**1.  shell脚本接受两个整数，让脚本分别计算并显示这两个整数的和，差，积，商**
```
#!/bin/bash
echo "first number $1"  （表示输出第一个数）
echo "second number $2" （表示输出第二个数）
echo " $(($1+$2))"      （输出两数之和）
echo "$[$1-$2]"         （输出两数之差）
echo "$[$1*$2]"         （输出两数之积）
echo "$[$1/$2]"         （输出两数之商）
```
**2.  shell编程得到某个目录下所有文件的名字**
```
#!/bin/bash
cd /home/hadoop
for file in $(ls *)
do
  echo $file
done   
```
**3. shell case语句练习**
```
#!/bin/sh
echo "please input number 1 to 3"
read number
case $number in
1)
        echo "you input 1"
       ;;
2)
        echo "you input 2"
        ;;
3)
        echo "you input 3"
        ;;
*)
        echo "error! the number you input isn't 1 to 3"
        ;;
esac
```

**4.shell编程进行杀死进程**
```
#!/bin/sh  
NAME=$1  
echo $NAME  
ID=`ps -ef | grep "$NAME" | grep -v "grep" | awk '{print $2}'`  
echo $ID  
echo "---------------"  
for id in $ID  
do  
kill -9 $id  
echo "killed $id"  
done  
echo "---------------"  
```
**5.shell编程检查网络服务是否正常**
```
#!/usr/bin/bash
#超时时间  
timeout=5
#目标网站  
target=www.baidu.com
#获取响应状态码  
ret_code=`curl -I -s --connect-timeout $timeout $target -w %{http_code} | tail -n1`

if [ "x$ret_code" = "x200" ]; then
    echo "网络畅通"
else
    echo "网络不畅通"
fi

```
**6.shell编程实现文件的移动**
```
#/bin/sh 
filelist=`ls /email/file/error`for file in $filelist
do 
 echo $file
 mv /email/file/error/$file /email/file/collection
done
```


