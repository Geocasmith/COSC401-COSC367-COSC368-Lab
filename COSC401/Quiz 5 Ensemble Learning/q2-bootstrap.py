import hashlib
import numpy as np

def pseudo_random(seed=0xDEADBEEF):
    """Generate an infinite stream of pseudo-random numbers"""
    state = (0xffffffff & seed)/0xffffffff
    while True:
        h = hashlib.sha256()
        h.update(bytes(str(state), encoding='utf8'))
        bits = int.from_bytes(h.digest()[-8:], 'big')
        state = bits >> 32
        r = (0xffffffff & bits)/0xffffffff
        yield r

def take(n, iterator):
    while n > 0:
        yield next(iterator)
        n -= 1
def bootstrap(dataset, sample_size):
    """Returns a generator of samples (arrays with sample_size rows of randomly chosen rows from dataset) from the dataset which goes until sample size is reached"""
    num_rows, num_columns = dataset.shape

    while(True):
        #Empty numpy array to hold the sample
        sample = np.zeros(shape=(num_rows-1, num_columns))

        # for num rows, gets the random number from the pseudo random generator and uses it to get a random row from the dataset. Appends that row to the sample array
        index=0
        for r in take(sample_size, pseudo_random()):
            random_row_index = int(r * len(dataset))
            sample[index] = dataset[random_row_index]
            index += 1
        yield sample


dataset = np.array([[1, 0, 2, 3],
                    [2, 3, 0, 0],
                    [4, 1, 2, 0],
                    [3, 2, 1, 0]])
ds_gen = bootstrap(dataset, 3)
print(next(ds_gen))
print(next(ds_gen))