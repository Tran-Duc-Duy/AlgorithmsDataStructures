# Khai báo thư viện Queue
from queue import Queue

# Nhập kích thước queue và số lượng gói tin
size, packagesCount = map(int, input().split())

# Khởi tạo thời gian CPU
cpuTime = 0

# Khởi tạo queue
queue = Queue(size)

# Duyệt qua từng gói tin
for i in range(packagesCount):
    # Nhập thời gian đến và thời gian xử lý của gói tin
    arrival, duration = map(int, input().split())

    # Xóa các gói tin đã được xử lý xong khỏi queue
    while not queue.empty() and queue.queue[0] <= arrival:
        queue.get()

    # Nếu thời gian CPU chưa đến thì in ra thời gian đến của gói tin
    if cpuTime < arrival:
        print(arrival)
        cpuTime = arrival + duration
        queue.put(cpuTime)
    # Nếu queue chưa đầy thì in ra thời gian CPU hiện tại và thêm gói tin vào queue
    elif queue.qsize() < size:
        print(cpuTime)
        cpuTime += duration
        queue.put(cpuTime)
    # Nếu queue đã đầy thì in ra -1
    else:
        print(-1)