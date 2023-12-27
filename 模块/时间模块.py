from datetime import datetime, timedelta

now = datetime.now()  # 获取当前日期和时间
tomorrow = now + timedelta(days=1)  # 计算明天的日期


import time

start_time = time.time()  # 获取当前时间戳
time.sleep(2)  # 等待2秒
end_time = time.time()
elapsed_time = end_time - start_time
