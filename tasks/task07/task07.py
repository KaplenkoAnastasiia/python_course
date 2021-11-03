import uuid
from datetime import date


class Good():
    def __init__(self, name: str, price: float):
        self.name = name
        self.id = uuid.uuid4()
        self.price = price


class Order():
    def __init__(self, order_id: uuid.UUID, order_date, client_id: uuid.UUID, goods: list, price=0):
        self.order_id = order_id
        self.order_date = order_date
        self.client_id = client_id
        self.Goods = goods
        self.price = price

    @property
    def price(self):
        return sum(g.price for g in self.goods)

    @price.setter
    def price(self, value):
        self._price = value

    def AddGood(self, good: Good):
        if not type(good) is Good:
            return
        self.Goods.append(good)


class OrderRepository():
    def __init__(self):
        self.items = []

    def add(self, order: Order):
        self.items.append(order)

    def get(self, order_id: uuid.UUID):
        for order in self.items:
            if order.order_id == order_id:
                return order
            return None

    def delete(self, order_id: uuid.UUID):
        order = self.get(order_id)
        self.items.remove(order)

    def list(self, n_latest: int = None):
        if n_latest == None or n_latest >= len(self.items):
            return self.items
        return self.items[:n_latest]


apple = Good("Apple", 10.9)
cheese = Good("Cheese", 113)
water = Good("Water", 15)

order1 = Order(uuid.uuid4(), date.today(), uuid.uuid4(), [])
order1.AddGood(apple)
order1.AddGood(cheese)

order2 = Order(uuid.uuid4(), date.today(), uuid.uuid4(), [])
order2.AddGood(apple)
order2.AddGood(apple)

order3 = Order(uuid.uuid4(), date.today(), uuid.uuid4(), [])
order3.AddGood(apple)
order3.AddGood(cheese)
order3.AddGood(water)

repository = OrderRepository()
repository.add(order1)
repository.add(order2)
repository.add(order3)

assert len(repository.list(10)) == 3

orders = repository.list(2)

assert len(orders) == 2
