import numpy as np
import matplotlib.pyplot as plt

category_names = ['High temp', 'Humidity', 'Wind Speed', 'Precipitation', 'Low Temp']
results = {
    'July 21': [84, 74, 7, 0, 67],
    'July 22': [83, 68, 6, 0, 75],
    'July 23': [83, 64, 7, 0, 75],
    'July 24': [82, 62, 7, 0, 73],
    'July 25': [84, 61, 6, 0, 74],
}

def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'black' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    return fig, ax


survey(results, category_names)
plt.show()

fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
weather = ['Overcast', 'Partly Sunny', 'Passing Clouds', 'Scattered Clouds', 'Light Rain', 'Thunder Shower', 'Sunny']
amount = [5, 25, 5, 15, 2, 1, 2]
ax.pie(amount, labels=weather, autopct='%1.2f%%')

plt.show()
