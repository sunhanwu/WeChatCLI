import itchat


def print_context(msg):
    print(msg['TEXT'])


def main():
    itchat.auto_login(hotReload=True)
    itchat.run()

if __name__=='__main__':
    main()
    print_context(itchat.content.TEXT)
