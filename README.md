# iqy-parse
download free video without watermark from aiqiyi

IQIYI divides the video into 8-10 seconds and needs to merge the video after downloading
The VIP video is temporarily unavailable, of course you can try it with the VIP account cookie
The video defaults to 720P (if the video is not 720P, the highest definition is downloaded by default)
Environment: python3.7, windows, chrome, selenium
[After analyzing a URL in about 5 seconds, the current efficiency is poor, and there will be better solutions in the future.]

You need to change 3 lines of code in iqy-parse.py
Line 36: chromedriver local path
Line 97: iQIYI cookie for login account
Line 183: URL to be crawled

写在前面
下载爱奇艺上的免费视频，无水印
爱奇艺将视频切分为8-10秒，下载后需要合并视频
VIP的视频暂时不行，当然你可以用VIP账号的cookie试一下
视频默认720P（如果视频未到720P，默认下载最高清晰度）
环境：python3.7，windows, chrome, selenium
【如果感兴趣的人多，再详细写参数破解过程吧】
【大概5秒分析完一个url，目前效率较差，后续有更好解决方案会更新】

你需要更改iqy-parse.py的3行代码
36行：chromedriver本地路径
97行：登录账号的爱奇艺cookie
183行：需要抓取的url
