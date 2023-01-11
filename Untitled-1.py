from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import heliopy.data.wind as wind

starttime = datetime(1995, 1, 30, 2, 0, 0)
endtime = starttime + timedelta(hours=1)

Bdata = wind.mfi_h0(starttime, endtime)

Bdata.peek(columns=['BGSE_0', 'BGSE_1', 'BGSE_2'])
change