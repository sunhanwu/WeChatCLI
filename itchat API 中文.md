# itchat API 中文

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



