from abc import ABC, abstractmethod
import time


class QueueInterface(ABC):

  @abstractmethod
  def size(self):
    pass

  @abstractmethod
  def isEmpty(self):
    pass

  @abstractmethod
  def front(self):
    pass

  @abstractmethod
  def enqueue(self, info):
    pass

  @abstractmethod
  def dequeue(self):
    pass


class Order:

  def __init__(self, qtty, customer):
    self.customer = customer
    self.qtty = qtty

  def print(self):
    print("     Customer: " + str(self.getCustomer()))
    print("     Quantity: " + str(self.getQtty()))
    print("     ------------")

  def getQtty(self):
    return self.qtty

  def getCustomer(self):
    return self.customer


class Node:

  def __init__(self, info):
    self.info = info
    self.next = None

  def getInfo(self):
    return self.info

  def setInfo(self, info):
    self.info = info

  def getNext(self):
    return self.next

  def setNext(self, next):
    self.next = next


class Queue(QueueInterface):

  def __init__(self):
    self.top = None
    self.tail = None

  def size(self):
    count = 0
    current = self.top
    while current is not None:
      count += 1
      current = current.getNext()
    return count

  def isEmpty(self):
    return self.top is None

  def front(self):
    if self.isEmpty():
      return None
    return self.top.getInfo()

  def enqueue(self, info):
    newNode = Node(info)
    if self.isEmpty():
      self.top = newNode
      self.tail = newNode
    else:
      self.tail.setNext(newNode)
      self.tail = newNode

  def dequeue(self):
    if self.isEmpty():
      return None
    item = self.top.getInfo()
    self.top = self.top.getNext()
    if self.top is None:
      self.tail = None
    return item

  def printInfo(self):
    print("********* QUEUE DUMP *********")
    print("   Size: " + str(self.size()))
    node = self.top
    elementIndex = 1
    while node is not None:
      print("   ** Element " + str(elementIndex))
      info = node.getInfo()
      if isinstance(info, Order):
        info.print()
      else:
        print("     Info: " + str(info))
      node = node.getNext()
      elementIndex += 1
    print("******************************")

  def getNth(self, pos):
    if pos < 1:
      return None
    current = self.top
    currentPos = 1
    while current is not None:
      if currentPos == pos:
        return current.getInfo()
      current = current.getNext()
      currentPos += 1
    return None


class TestQueue:

  @staticmethod
  def main():
    start_time = time.time()

    cola = Queue()

    p1 = Order(20, "cust1")
    p2 = Order(30, "cust2")
    p3 = Order(40, "cust3")
    p4 = Order(50, "cust3")

    cola.enqueue(p1)
    cola.enqueue(p2)
    cola.enqueue(p3)
    cola.enqueue(p4)

    cola.printInfo()

    f = cola.front()
    if isinstance(f, Order):
      f.print()

    n3 = cola.getNth(3)
    if isinstance(n3, Order):
      n3.print()

    d = cola.dequeue()
    if isinstance(d, Order):
      d.print()

    cola.printInfo()

    end_time = time.time()
    duration_ms = (end_time - start_time) * 1000
    print(f"\nTiempo de ejecucion: {duration_ms:.4f} ms")


if __name__ == "__main__":
  TestQueue.main()
