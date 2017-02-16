import json
import matplotlib.pyplot as plt
import numpy as np

###################################################

# Whether to create a cumulative plot or not
cum = 1

# File with source data
filename = "map-utxo-count.json"

###################################################

def parse_and_plot(src_filename, cum=1, output="figure.png"):

    with open(src_filename) as data_file:
        data = json.load(data_file)

    max_height = sorted(data.keys(), key=int)[-1]
    x = range(0, int(max_height)+1)

    # Blocks with 0 utxos are not included in the dataset, so we add them here
    y = [0 for _ in x]
    for k in data.keys():
        y[int(k)] = data[k]

    assert ((data["261684"] == y[261684]) and (x[261684] == 261684)), "There has been some error!"
    print "Total number of utxos in all blocks: " + str(sum(y))

    if cum:
        y = np.cumsum(y)

    print "Block " + str(x[100000]) + ": " + str(y[100000])
    print "Block " + str(x[150000]) + ": " + str(y[150000])
    print "Block " + str(x[200000]) + ": " + str(y[200000])

    plt.title("Num. utxos per block")
    plt.ylabel("Number of utxos")
    plt.xlabel("Block height")
    plt.plot(x, y)
    plt.savefig('fog.png')


parse_and_plot(filename, 1)
