# itchat API 中文

[TOC]

## login 函数

```python
def login(self, enableCmdQR=False, picDir=None, qrCallback=None,
        loginCallback=None, exitCallback=None):
    ''' log in like web wechat does
        for log in
            - a QR code will be downloaded and opened
            - then scanning status is logged, it paused for you confirm
            - finally it logged in and show your nickName
        for options
            - enableCmdQR: show qrcode in command line
                - integers can be used to fit strange char length
            - picDir: place for storing qrcode
            - qrCallback: method that should accept uuid, status, qrcode
            - loginCallback: callback after successfully logged in
                - if not set, screen is cleared and qrcode is deleted
            - exitCallback: callback after logged out
                - it contains calling of logout
        for usage
            ..code::python

                import itchat
                itchat.login()

        it is defined in components/login.py
        and of course every single move in login can be called outside
            - you may scan source code to see how
            - and modified according to your own demond
    '''
    raise NotImplementedError()
```

## search_mps 函数

```python
def search_mps(self, name=None, userName=None):
    return self.storageClass.search_mps(name, userName)
```

1. 函数功能：搜索公众号

2. 参数列表“

   + name: 获取公众号名名称中含有”name“的公众号
   + userName:获取公众号名名称为”name“的公众号

3. 返回值：

   self.storageClass.search_mps（name.userName）

##