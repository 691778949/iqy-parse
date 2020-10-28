import requests, re, time, os, hashlib, shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_authKey(tm, tvid):
    # 计算 authKey ：md5(md5("")+时间戳+tvid)
    md = hashlib.md5()
    md.update(str("").encode('utf-8'))
    k = str(md.hexdigest()) + str(tm) + tvid
    md = hashlib.md5()
    md.update(str(k).encode('utf-8'))
    authKey = str(md.hexdigest())
    return authKey


def write_iqy_vf_js(vf_url, tm):
    # 改写vf算法js文件中的传入url值
    os.system("copy iqy_vf.js iqy_get_vf-{}.js".format(tm))
    # print("iqy_get_vf.js复制完毕")

    three_line = '''
        var a = "{}";\n
        var _vf = cmd5x_exports.cmd5x(a);\n
        return _vf;\n
    '''.format(vf_url)

    fp = open("./iqy_get_vf-{}.js".format(tm), "a", encoding="utf-8")
    fp.write(three_line)
    fp.close()
    # print("iqy_get_vf.js写入完毕")


def get_vf(tm):
    # 计算vf参数
    f = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chromedriver.exe'
    chrome_options = Options()
    # 关闭自动测试状态显示 // 会导致浏览器报：请停用开发者模式
    # window.navigator.webdriver还是返回True,当返回undefined时应该才可行。
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # 关闭开发者模式
    chrome_options.add_experimental_option("useAutomationExtension", False)
    # 自动开启控制台
    # chrome_options.add_argument("--auto-open-devtools-for-tabs")
    # 无头模式
    chrome_options.add_argument("--headless")
    # 禁止加载图片
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # 接管已打开的调试模式chrome
    # chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{chrome_debug_port}")

    browser = webdriver.Chrome(f, options=chrome_options)
    # 窗口最大化
    # browser.maximize_window()
    # 设置执行js代码转换模式
    # browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            #"source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    #})

    url = "https://so.iqiyi.com/so/q_python"
    browser.get(url)
    print("-----------getting vf-----------")
    with open("./iqy_get_vf-{}.js".format(tm), "r", encoding="utf-8", errors="ignore") as file:
        iqy_vf = file.read()
    vf = browser.execute_script(iqy_vf)
    time.sleep(2)
    browser.quit()
    return vf


def parse_iqy(target_url):
    # 解析视频真实播放地址
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response = requests.get(url=target_url, headers=headers)
    # print(response.text)

    tvid = re.findall(r"param\['tvid'\] = \"(.*?)\";", response.text)[0]
    print("tvid = %s" % tvid)

    vid = re.findall(r"param\['vid'\] = \"(.*?)\";", response.text)[0]
    print("vid = %s" % vid)

    irTitle = re.findall(r'<meta\s\sname="irTitle"\scontent="(.*?)"\s/>', response.text)[0]
    print("irTitle = %s" % irTitle)

    tm = round(time.time() * 1000)
    print("tm = %s" % tm)

    authKey = get_authKey(tm, tvid)
    print("authKey = %s" % authKey)

    dirname = tvid + "--" + irTitle

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
        'cookie': 'QC005=617109f4ce263090879c56015a80e72d; QC006=b82uu46sgoie6enhhqoyimr1; QC173=0; T00404=579a8a5a6246d438c829d98d0b1f3ba3; P00004=.1601097079.c67952bdd3; P1111129=1601097095; P00037=A00000; P00039=fbxy30MJeTd7evLEbMsLUUsXPv9Jsm3gwatS8Nm1Gm2wWazm3ki4P5wGbF4Uw4eIfpEGm3A7c; P00003=938396906162179; P00010=938396906162179; P01010=1601136000; P00PRU=938396906162179; P00002=%7B%22uid%22%3A%22938396906162179%22%2C%22pru%22%3A938396906162179%2C%22user_name%22%3A%2215372027535%22%2C%22nickname%22%3A%22%5Cu7528%5Cu6237355778e400803%22%2C%22pnickname%22%3A%22%5Cu7528%5Cu6237355778e400803%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D; P000email=15372027535; QC160=%7B%22commonType%22%3A%2229%22%7D; QC170=0; QC170.sig=kpbsfShzd6-lfX4KsUFQ8tg5jLU; QP0013=0; QP007=0; QC124=1%7C0; P00001=c3uDm3m3vM0q7zNfkRjAZoqFwqq32VBuwu3RrKZlm18clZAjyxp8WKf4NDWHqs3h6XTXl57; P00007=c3uDm3m3vM0q7zNfkRjAZoqFwqq32VBuwu3RrKZlm18clZAjyxp8WKf4NDWHqs3h6XTXl57; Hm_lvt_292c77bd6e6064e926d1d58f63241745=1603287778; T00700=EgcI9L-tIRABEgcIz7-tIRABEgcI67-tIRACEgcIkMDtIRABEgcI77-tIRABEgcIg8DtIRABEgcI0b-tIRABEgcI4b-tIRABEgcI8L-tIRABEgcIhcDtIRABEgcI7L-tIRAGEgcIi8HtIRABEgcI87-tIRABEgcI9sDtIRABEgcImMDtIRABEgcI57-tIRABEgcI6b-tIRABEgcIlMDtIRAB; QY_PUSHMSG_ID=617109f4ce263090879c56015a80e72d; _ga=GA1.2.679220744.1603546456; QC163=1; QC175={%22upd%22:true%2C%22ct%22:1603637797334}; QC008=1601094540.1603607479.1603638090.11; nu=0; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1603512933,1603546456,1603607526,1603638090; QC179=%7B%22userIcon%22%3A%22https%3A//img7.iqiyipic.com/passport/20200802/ee/6c/passport_938396906162179_159627040773521_130_130.jpg%22%2C%22vipTypes%22%3A-1%7D; QP008=960; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A0%2C%22hideRoleTip%22%3A1%2C%22isOpen%22%3A1%2C%22speed%22%3A10%2C%22density%22%3A30%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%2C%22hadTip%22%3A1%2C%22isFilterHongbao%22%3A0%7D; QC007=https%253A%252F%252Fwww.baidu.com%252Flink%253Furl%253DGp2ak2FZD6_sd4WP4vKAdIhI0tlJAKDi3lIjGbLFqEK%2526wd%253D%2526eqid%253Df16b1549001a10fb000000025f95c477; QC021=%5B%7B%22key%22%3A%22%E4%BA%94%E8%8A%B1%E5%A4%A7%E7%BB%91%E9%AD%94%E6%9C%AF%22%7D%2C%7B%22key%22%3A%22%E9%AD%94%E6%9C%AF%22%7D%2C%7B%22key%22%3A%22eva%22%7D%2C%7B%22key%22%3A%22%E6%9F%AF%E5%8D%97%22%7D%2C%7B%22key%22%3A%22%E7%BA%B8%E7%89%8C%E9%AD%94%E6%9C%AF%22%7D%2C%7B%22key%22%3A%22%E6%89%91%E5%85%8B%E7%89%8C%E9%AD%94%E6%9C%AF%E6%95%99%E5%AD%A6%22%7D%2C%7B%22key%22%3A%22%E5%BC%A0%E8%B5%B7%E7%81%B5%22%7D%2C%7B%22key%22%3A%22%E4%B9%A1%E6%9D%91%E7%88%B1%E6%83%85%22%7D%2C%7B%22key%22%3A%22%E6%AD%A6%E6%9E%97%E5%A4%96%E4%BC%A0%22%7D%5D; websocket=true; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1603652530; QC010=96585115; QP0027=101; CM0001=1; IMS=IggQBBj_5Nv8BSokCiBjNDFhYTA5OGY4NTQ0MzY5ZTg5MWZjM2E0Mjg0ZTMzNBAAciQKIGM0MWFhMDk4Zjg1NDQzNjllODkxZmMzYTQyODRlMzM0EACCAQCKASQKIgogYzQxYWEwOThmODU0NDM2OWU4OTFmYzNhNDI4NGUzMzQ; TQC002=type%3Djspfmc140109%26pla%3D11%26uid%3D617109f4ce263090879c56015a80e72d%26ppuid%3D938396906162179%26brs%3DCHROME%26pgtype%3Dplay%26purl%3Dhttps%3A%252F%252Fwww.iqiyi.com%252Fv_19rsglj8y0.html%26cid%3D1%26tmplt%3D%26tm1%3D2581%2C0; __dfp=a1a48f3ce98e544970afc5d05b46f71f8ef099da41299db3f4275e4c7a1e3ccb19@1604048726964@1602752727964'
    }

    dfp = re.findall(r'_dfp=(.*?)@', headers['cookie'])[0] # cookie: __dfp
    print("dfp = %s" % dfp)

    pck = re.findall(r'P00001=(.*?);', headers['cookie'])[0] # cookie: P00001
    print("pck = %s" % pck)

    uid = re.findall(r'P00002=%7B%22uid%22%3A%22(.*?)%22%2C', headers['cookie'])[0] # cookie: P00002['uid']
    print("uid = %s" % uid)

    k_uid = re.findall(r'QC005=(.*?);', headers['cookie'])[0] # cookie: QC005
    print("k_uid = %s" % k_uid)

    # bid: 500,720P(默认), 600,1080P（暂时不行）
    vf_url = "/dash?tvid={}&bid=500&vid={}&src=01010031010000000000&vt=0&rs=1&uid={}&ori=pcw&ps=0&k_uid={}&pt=0&d=0&s=&lid=&cf=&ct=&authKey={}&k_tag=1&ost=0&ppt=0&dfp={}&locale=zh_cn&prio=%7B%22ff%22%3A%22f4v%22%2C%22code%22%3A2%7D&pck={}&k_err_retries=0&up=&qd_v=2&tm={}&qdy=a&qds=0&k_ft1=706436220846084&k_ft4=1162183859249156&k_ft5=1&bop=%7B%22version%22%3A%2210.0%22%2C%22dfp%22%3A%22{}%22%7D&ut=0".format(tvid, vid, uid, k_uid, authKey, dfp, pck, tm, dfp)
    write_iqy_vf_js(vf_url, tm)
    vf = get_vf(tm)
    print("vf = %s" % vf)

    real_url = "https://cache.video.iqiyi.com" + vf_url + "&vf=" + vf
    print(real_url)
    response = requests.get(url=real_url, headers=headers)
    # print(response.text)

    # 判断f4v/m3u8
    file_end = response.json().get("data")["program"]["video"][0]["ff"]
    if file_end == 'ts':
        print('视频为m3u8流媒体')
    elif file_end == 'f4v':
        print('视频为f4v流媒体')

    # 获取download_url_list
    download_url_list = []
    if file_end == 'ts':
        video_list_json = ""
        for k in response.json().get("data")["program"]["video"]:
            try:
                video_list_json = k["m3u8"]
            except:
                pass
        download_url_list = re.findall(r'(http://.*?)\s#', video_list_json)
        print(download_url_list)
    elif file_end == 'f4v':
        video_fs = []
        for k in response.json().get("data")["program"]["video"]:
            try:
                video_fs = k["fs"]
            except:
                pass
        download_url_list = []
        for h in video_fs:
            middle_url = "http://data.video.iqiyi.com/videos" + h["l"]
            res = requests.get(url=middle_url, headers=headers)
            download_url = res.json().get("l")
            download_url_list.append(download_url)
        print(download_url_list)

    # 下载视频
    if os.path.exists("./{}".format(dirname)):
        shutil.rmtree("./{}".format(dirname))
    os.mkdir(dirname)
    no = 10000
    for i in download_url_list:
        no += 1
        r = requests.get(url=i, headers=headers, stream=True)
        with open('./{}/{}.{}'.format(dirname, no, file_end), "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        print("已下载%d%%" % ((no-10000)*100/len(download_url_list)))

    # 合并视频（windows环境下）
    root_path = os.getcwd()
    tmp = os.listdir("./{}".format(dirname))
    os.chdir("./{}".format(dirname))
    filename = "result.{}".format(file_end)
    shell_str = '+'.join(tmp)
    shell_str = 'copy /b ' + shell_str + ' ' + filename
    os.system(shell_str)
    os.chdir(root_path)


if __name__ == '__main__':

    url_list = ["https://www.iqiyi.com/v_19rrjbfmso.html", "https://www.iqiyi.com/w_19s9jsxbo5.html"]
    for url in url_list:
        parse_iqy(url)