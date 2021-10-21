import matplotlib.pyplot as plt
import numpy as np
with open('/home/gr101/Desktop/Scripts/Boris Mukhachev/settings.txt', 'r') as settings:
    tmp = [float(i) for i in settings.read().split('\n')]

data_array = np.loadtxt('/home/gr101/Desktop/Scripts/Boris Mukhachev/data.txt', dtype = int)
data_array = data_array * 3.3 / 256
    
fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)
ax.plot(data_array, color = 'blue', linewidth = 1, linestyle = '-')
plt.ylim(data_array.min(), data_array.max())
#ax.text(1, 2, 'time of charging = ')
#ax.text(1, 1, 'time of discharging = ')
ax.minorticks_on()
ax.set_title('voltage versus time graph')
ax.set_xlabel('time, s')
ax.set_ylabel('Voltage, V')
ax.grid(which = 'major', linewidth = 1, color = 'black')
ax.grid(which = 'minor', linewidth = 0.5, linestyle = '--', color = 'grey')
ax.tick_params(which = 'major', length = 15, width = 1)
ax.tick_params(which = 'minor', length = 7, width = 0.5)
ax.plot(label = 'Voltage versus time')
plt.legend('V(t)')
fig.set_figwidth(12)
fig.savefig('/home/gr101/Desktop/Scripts/Boris Mukhachev/test.svg')

plt.show()
    