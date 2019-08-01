# _*_ coding=utf-8 _*_


from abc import ABCMeta, abstractmethod

"""
不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品的实例
优点：1隐藏对象创建的实现细节
      2客户端不需要修改代码
缺点：1违反了单一职责原则，将创建逻辑集中到一个工厂类
      2违反开闭原则，当添加新产品时，需要修改工厂类代码

"""


class Payment(metaclass=ABCMeta):
    """抽象产品角色"""

    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    """具体产品角色"""

    def __init__(self, hb=False):
        self.hb = hb

    def pay(self, money):
        print("支付宝支付%s元" % money)


class WechatPay(Payment):
    """具体产品角色"""

    def pay(self, money):
        print("微信支付%s元" % money)


class SimpleFactory:
    """工厂角色"""

    def create_payment(self, method):
        if method == "alipay":
            return Alipay()
        elif method == "wechat":
            return WechatPay()
        elif method == "hb":
            return Alipay(hb=True)
        else:
            raise TypeError("No such payment named %s" % method)


# client 调用代码层
pf = SimpleFactory()
p = pf.create_payment('alipay')
p.pay(100)
