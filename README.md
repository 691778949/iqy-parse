# iqy-parse
download free video without watermark from aiqiyi\n

IQIYI divides the video into 8-10 seconds and needs to merge the video after downloading\n
The VIP video is temporarily unavailable, of course you can try it with the VIP account cookie\n
The video defaults to 720P (if the video is not 720P, the highest definition is downloaded by default)\n
Environment: python3.7, windows, chrome, selenium\n
[After analyzing a URL in about 5 seconds, the current efficiency is poor, and there will be better solutions in the future.]\n

You need to change 3 lines of code in iqy-parse.py\n
Line 36: chromedriver local path\n
Line 97: iQIYI cookie for login account\n
Line 183: URL to be crawled\n

写在前面\n
下载爱奇艺上的免费视频，无水印\n
爱奇艺将视频切分为8-10秒，下载后需要合并视频\n
VIP的视频暂时不行，当然你可以用VIP账号的cookie试一下\n
视频默认720P（如果视频未到720P，默认下载最高清晰度）\n
环境：python3.7，windows, chrome, selenium\n
【如果感兴趣的人多，再详细写参数破解过程吧】\n
【大概5秒分析完一个url，目前效率较差，后续有更好解决方案会更新】\n

你需要更改iqy-parse.py的3行代码\n
36行：chromedriver本地路径\n
97行：登录账号的爱奇艺cookie\n
183行：需要抓取的url\n
