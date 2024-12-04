import matplotlib.pyplot as plt
import numpy as np

# 提取时间和调用次数数据
times = ['15:29:12', '15:29:13', '15:29:14', '15:29:15', '15:29:21', '15:29:22', '15:29:23', '15:29:25', '15:29:26', '15:29:27', '15:29:28', '15:29:47', '15:29:48', '15:29:52', '15:29:53', '15:30:07', '15:30:08', '15:30:19', '15:30:25', '15:30:26', '15:30:27', '15:30:29', '15:30:30', '15:30:32', '15:30:33', '15:30:34', '15:30:35', '15:30:40', '15:30:41', '15:30:44', '15:30:45', '15:30:50', '15:30:51', '15:31:00', '15:31:01', '15:31:11', '15:31:12', '15:31:13', '15:31:14', '15:31:15', '15:31:19', '15:31:20', '15:31:21', '15:31:22', '15:31:25', '15:31:30', '15:31:31', '15:31:32', '15:31:33', '15:31:34', '15:31:35', '15:31:40', '15:31:45', '15:31:46', '15:31:49', '15:31:50', '15:31:55', '15:32:00', '15:32:05', '15:32:06', '15:32:10', '15:32:15', '15:32:20', '15:32:25', '15:32:26', '15:32:30', '15:32:31', '15:32:35', '15:32:36', '15:32:40', '15:32:45', '15:32:46', '15:32:52', '15:32:53', '15:32:55', '15:33:00', '15:33:01']
counts = [1, 1, 5, 6, 1, 10, 5, 4, 1, 5, 111, 1, 1, 23, 41, 27, 282, 1, 14, 32, 179, 11, 69, 38, 65, 116, 158, 47, 160, 25, 278, 10, 52, 22, 57, 14, 115, 265, 57, 398, 1, 20, 18, 65, 154, 32, 37, 92, 25, 51, 134, 177, 78, 653, 14, 167, 56, 52, 41, 94, 110, 78, 45, 57, 209, 16, 151, 40, 94, 140, 77, 39, 18, 119, 24, 52, 90]

# 创建趋势图
plt.figure(figsize=(12, 6))
plt.plot(times, counts)
plt.xlabel('时间')
plt.ylabel('调用次数')
plt.title('时间-调用次数趋势图')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()