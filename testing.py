from data_queue import MessageQueue


m = MessageQueue()

m.put("hi")

print(m.queue)

mes = m.get()
ms = m

print(mes)
print(ms.queue)