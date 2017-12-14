
## workflow

之前也一直使用被称为mac神器到alfred。直到今天才发现我用的是低版本，功能非常基础。而高版本所支持的workflow才是真的称为神器。。workflow就是让alfred直接执行脚本，包括shell、python、php等。


#### workflow登录校园网

在之前用旧版本的alfred登录校园网所用的方法是在feature添加web url，输入p打开p.nju.edu.cn。然后点击输入浏览器记住的密码登陆。相比打开浏览器页面已经快捷很多。但是如果使用workflow可以直接，输入指定内容，回车就可以登陆。具体定义该workflow的步骤如下：

1. preference中点击workflow,按照如图选择keyword to script

	![](images/alfred1.png)
	
2. 输入关键字和描述，保存

	![](images/alfred2.png)

3. 右键创建script

	![](images/alfred3.png)

4. 输入执行的脚本并保存

```python
# -*- coding:utf-8 -*-

import json
import urllib
import urllib2


def login():
    url = 'http://p.nju.edu.cn/portal_io/login'
    username = 'xxxx'  # 可将密码等保存至文件
    password = 'xxxxx'
    data = {'username': username, 'password': password}
    postdata = urllib.urlencode(data).encode('utf-8')
    try:
        request = urllib2.Request(url, postdata)
        response = urllib2.urlopen(request)
        res = json.loads(response.read().decode('utf-8'))
        # print res["reply_code"]
    except Exception as e:
        print(e)
        
        
if __name__ == '__main__':
    login()
```
快捷键打开alfred输入框，输入你的关键字，回车。就连上了校园网，很方便。


#### 更简单的方式：下载.alfredworkflow文件

1. 下载NJUnet.alfredworkflow文件
2. 双击下载的文件
3. 双击这两个脚本 按提示输入自己的账号密码

![屏幕快照 2017-12-14 下午5.12.12.png](http://upload-images.jianshu.io/upload_images/7054861-6194aff17a77a040.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**_*此时快捷键‘opt+p’可以登录校园网，登录成功后有提示音和notification；‘opt+o’可以退出登录校园网，退出成功后有提示音和notification；*_**



---

#### 最后安利，alfred是真神器。
	

