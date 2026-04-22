import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(values):

    for j in range(len(values)):
        min_index = j
        min_value = values[min_index]
        for i in range(j+1, len(values)):
            if values[i] < min_value:
                min_index = i
                min_value = values[i]
        values[j], values[min_index] = values[min_index], values[j]
        print(values)
    return values


def bubble_sort(values):

    plt.ion()
    plt.show()
    for j in range(len(values)):
        for i in range(len(values)-1):
            if values[i] > values[i+1]:
                values[i], values[i+1] = values[i+1], values[i]
                index_highlight1 = j
                index_highlight2 = j + 1
                colors = ["steelblue"] * len(values)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(values)), values, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)
        print(values)
    plt.ioff()
    plt.show()
    return (values)




if __name__ == "__main__":
    values = random_numbers(10)
    #selection_sort(values)
    bubble_sort(values)
