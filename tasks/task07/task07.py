import uuid
from datetime import date

class Good():
  def __init__(self, name: str, price: float):
      self.name = name
      self.id = uuid.uuid4()
      self.price = price


class Order():
    def __init__(self):
        self.order_id = uuid.uuid4()
        self.order_date = date.today()
        self.client_id = uuid.uuid4()
        self.Goods = {}
    
    @property
    def price(self):
      price = 0
      if self.Goods is None or len(self.Goods.items()) < 1:
        return price
      for k,v  in self.Goods.items():
        if not type(k) is Good:
          return price
        price += v
      return price
    
    def AddGood(self,good : Good):
      if not type(good) is Good:
        return
      self.Goods[good] = good.price

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
       for order in self.items:
          if order.order_id == order_id:
            self.items.remove(order)

    def list(self, n_latest : int = None):
      if n_latest == None:
        return self.items
      if n_latest >= len(self.items):
        return self.items
      return self.items[:n_latest]
        

apple = Good("Apple", 10.9)
cheese = Good("Cheese", 113)
water = Good("Water", 15)

order1 = Order()
order1.AddGood(apple)
order1.AddGood(cheese)

order2 = Order()
order2.AddGood(apple)
order2.AddGood(apple)

order3 = Order()
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