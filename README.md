这是OCR方案实现自动答题的代码文件，模型用的ppocrv3，识别英文和数字的轻量化模型（因为模型复杂会跑的慢，就随便选了个小的）。

方案逻辑：

iPhone投影到Mac上 --> grabScreen.py抓题目 --> greaterThan.py识别数字 --> writeAnswer.py写答案， app.py是主程序入口。

windows和安卓同理，由于ios的互相投屏可以解决模拟器投屏问题，就偷懒了，如果是其他系统，则需要完成手机显示器到电脑显示器投影这一步，后续代码都可以不变。

所有需要修改的参数都在config.py文件内，主要一些捕捉图像区域参数，是针对不同屏幕大小和不同型号手机设计的，如果是iPhone和Mac，则投屏到最右侧即可，如有问题可修改config参数微调。

第一版比较粗糙，可能会有BUG，速度也只能做到1秒+一道题（因为题目有刷新时间，刷新再截取屏幕的新题目再识别作答），抓包yyds。

有OCR大神帮我提速或者任何交流可以发邮件联系：daledeng1998@163.com

后续更新加减乘除分数计算等模式~
