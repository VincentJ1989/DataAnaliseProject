import pandas as pd

# 4.3.1 转换字符串时间为标准时间
order = pd.read_csv('../data/meal_order_info.csv', sep=',', encoding='gbk')
print('转换前订单表中lock_time的类型:', order['lock_time'].dtype)
order['lock_time'] = pd.to_datetime(order['lock_time'])
print('转换后订单表中lock_time的类型:', order['lock_time'].dtype)

print('最小时间:', pd.Timestamp.min)
print('最大时间:', pd.Timestamp.max)

dateIndex = pd.DatetimeIndex(order['lock_time'])
print('使用DatetimeIndex之后的类型:', type(dateIndex))
# freq：时间间隔。S表示秒
periodIndex = pd.PeriodIndex(order['lock_time'], freq='S')
print('使用PeriodIndex之后的类型:', type(periodIndex))

# 4.3.2 提取时间序列数据信息
years = [i.year for i in order['lock_time']]
print('年份前5个数据为:\n', years[:5])
months = [i.month for i in order['lock_time']]
print('月份前5个数据为:\n', months[:5])
days = [i.day for i in order['lock_time']]
print('日期前5个数据为:\n', days[:5])
weekdays = [i.day_name for i in order['lock_time']]
print('星期名前5个数据为:\n', weekdays[:5])
# 使用DateIndex和PeriodIndex更加便捷
print('dateIndex中星期名称前5个数据为:\n', dateIndex.weekday_name[:5])
print('periodIndex中星期名称前4个数据为:\n', periodIndex.weekday[:4])

# 4.3.3加减时间数据--Timedelta(目前周期中没有年月)
# 后移一天(也可以是负值)
time1 = order['lock_time'] + pd.Timedelta(days=1)
time2 = order['lock_time'] + pd.Timedelta(days=-1)
print('前移一天后的数据:\n', time2[:5])
print('原先的数据:\n', order['lock_time'][:5])
print('后移一天后的数据:\n', time1[:5])
# 时间相减得到一个Timedelta
timeDelta = order['lock_time'] - pd.to_datetime('2017-1-1')
print('相减的前5个数据为:\n', timeDelta[:5])
print('相减得到的数据类型:', type(timeDelta))
