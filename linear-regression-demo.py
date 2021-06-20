import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlim([10, 35])
ax.set_ylim([0, 200])
ax.set_title("Lineární regrese")

x = np.array([])
y = np.array([])

axes = fig.gca()
x_vals = np.array([])
y_vals = np.array([])
regre_plot, = ax.plot(x_vals, y_vals, '--')

def onclick(event):
    ix, iy = event.xdata, event.ydata
    if ix is not None and iy is not None:
        global x
        global y
        x = np.append(x, ix)
        y = np.append(y, iy)

        ax.scatter(ix, iy)

        # Linear regression
        n = np.size(x)

        if n > 1:
            # mean of x and y vector
            m_x = np.mean(x)
            m_y = np.mean(y)

            # calculating cross-deviation and deviation about x
            SS_xy = np.sum(y*x) - n*m_y*m_x
            SS_xx = np.sum(x*x) - n*m_x*m_x

            # calculating regression coefficients
            b_1 = SS_xy / SS_xx
            b_0 = m_y - b_1*m_x


            axes = fig.gca()

            x_vals = np.array(axes.get_xlim())
            y_vals = b_0 + b_1 * x_vals
            regre_plot.set_ydata(y_vals)
            regre_plot.set_xdata(x_vals)

        fig.canvas.draw()
        fig.canvas.flush_events()


cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
