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
