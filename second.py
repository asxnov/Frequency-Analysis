import matplotlib.pyplot as plt
import main as m

keys = m.chrs.keys()
values = m.chrs.values()

plt.bar(keys, values, 0.75, data=m.chrs)
plt.show()


