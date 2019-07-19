import  queue
q=queue.Queue(maxsize=10)
for i in range (1,11):
    q.put(i)
while not q.empty():
    print(q.get())
