import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
stdev = statistics.stdev(data)
print(population_mean, stdev)

def random_set_of_mean(counter) :
    dataset = []
    for i in range(0, counter) :
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0, 100) :
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)

meanOfSamples = statistics.mean(mean_list)
sampleStdev = statistics.stdev(mean_list)
print(meanOfSamples, sampleStdev)

fig = ff.create_distplot([mean_list], ["Sample mean of number of claps"], show_hist=False)
fig.show()