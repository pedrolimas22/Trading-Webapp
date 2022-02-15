import numpy
import talib as TL
from numpy import genfromtxt

my_data = genfromtxt('1_day_csv', delimiter = ',')
close = my_data[:, 4]

# close = numpy.random.random(100)
# moving_avg = TL.SMA(, timeperiod = 10)

rsi = TL.RSI(close)

print(rsi)

