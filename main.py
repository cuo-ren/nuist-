import requests
import time

cookie=input("请输入cookies：")
data="""------WebKitFormBoundarysXGwBj7L9uYnP3AM
Content-Disposition: form-data; name="cmd"

xuexi_online
------WebKitFormBoundarysXGwBj7L9uYnP3AM--"""
url="https://examsafety.nuist.edu.cn//exam_xuexi_online.php"
headers={"accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6","connection":"keep-alive","content-length":"146","content-type":"multipart/form-data; boundary=----WebKitFormBoundarysXGwBj7L9uYnP3AM","cookie":cookie,"host":"examsafety.nuist.edu.cn","origin":"https://examsafety.nuist.edu.cn","sec-ch-ua":'"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',"sec-ch-ua-mobile":"?0","sec-ch-ua-platform":'"Windows"',"sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0","x-requested-with":"XMLHttpRequest"}


while True:
    
    r=requests.post(url,data=data,headers=headers)
    print(r.text)
    time.sleep(60)
