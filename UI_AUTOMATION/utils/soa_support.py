import socket
from utils.config import Config
TEST_HOST1 = '10.40.2.62'
TEST_HOST2 = '10.40.2.109'
c = Config()


def get_remote_ip(url):
    return socket.gethostbyname(url)


def get_account(url):
    ip = get_remote_ip(url)
    account = ''
    if ip == TEST_HOST1:
        account = c.get("account")['test1']
    elif ip == TEST_HOST2:
        account = c.get('account')['test2']
    else:
        print("invalid url")
    return account


def get_pay_method():
    yield from c.get('payMapping')


if __name__ == '__main__':
    rip = get_remote_ip('user.hqygou.com')
    # t1 = c.get('account')['test1']
    p1 = c.get('payMapping')[0]
    print(rip)
    # print(t1, p1)
    pay = get_pay_method()
    print(next(pay))
    print(next(pay))