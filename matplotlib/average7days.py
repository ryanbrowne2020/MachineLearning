
#populate the values from external source
calorietracker = [1230, 1460, 700, 1302, 1202, 1402, 1403]
sleephours = [7.4, 6.9, 5.5, 8.2, 7.1, 7.4, 7.6]
stepswalked = []
coaching_domains = [2,4,4,3,5]

def average7days(list):
    total = sum(list)
    average = round(total/7)
    return average

#use in utter, etc
print(average7days(calorietracker))
print(average7days(sleephours))

import matplotlib.pyplot as plt
import numpy as np

def averageMe(data):
    window_size = 3
    i = 0
    moving_averages = []
    for x in range(window_size - 1):
        moving_averages.append(np.nan)
    while i < len(data) - window_size + 1:
        this_window = data[i : i + window_size] #get current window
        window_average = sum(this_window) / window_size
        moving_averages.append(window_average)
        i += 1
    return moving_averages

def dataplot(data, title):
    xs = [x for x in range(len(data))]
    smoothed = averageMe(data)
    plt.plot(xs, data, smoothed)
    plt.show()
    # Make sure to close the plt object once done
    plt.close()


dataplot(sleephours, "Sleep Hours")


labels=['Sleep', 'Cognitive', 'Nutrition', 'Exercise', 'Social']
markers = [0, 1, 2, 3, 4, 5]
str_markers = ["0", "1", "2", "3", "4", "5"]

def make_radar_chart(name, stats, attribute_labels=labels,
                     plot_markers=markers, plot_str_markers=str_markers):

    labels = np.array(attribute_labels)

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats,[stats[0]]))
    angles = np.concatenate((angles,[angles[0]]))

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8),
                       subplot_kw=dict(polar=True))

    plt.xticks(angles[:-1], labels, color='grey', size=12)
    plt.yticks(np.arange(1, 6), ['1', '2', '3', '4', '5'],
            color='grey', size=12)
    plt.ylim(0, 5)
    ax.set_rlabel_position(30)
    
    ax.plot(angles, stats, linewidth=1, linestyle='solid')
    ax.fill(angles, stats, 'skyblue', alpha=0.4)

    # plt.show()

    # fig = plt.figure()
    # ax = fig.add_subplot(111, polar=True)
    # ax.plot(angles, stats, 'o-', linewidth=2)
    # ax.fill(angles, stats, alpha=0.25)
    # ax.set_thetagrids(angles * 180/np.pi, labels)
    # plt.yticks(markers)
    # ax.set_title(name)
    # ax.grid(True)

    #fig.savefig("static/images/%s.png" % name)

    return plt.show()

make_radar_chart("Username", coaching_domains) # example

