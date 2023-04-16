# /src/chainkey/utils.py

import random

# data_segmentation
def data_segmentation(data, num_chunks):
    data_len = len(data)
    chunk_size = data_len // num_chunks
    chunk_indices = list(range(0, data_len, chunk_size))

    if data_len % num_chunks != 0:
        chunk_indices.append(data_len)
    
    chunks = [data[i:j] for i, j in zip(chunk_indices[:-1], chunk_indices[1:])]
    random.shuffle(chunks)

    chunk_order = [chunk_indices[chunks.index(chunk)] for chunk in chunks]
    return ''.join(chunks), chunk_order

# data_restor
def data_restored(segments, chunk_order):
    ordered_segments = [None] * len(chunk_order)

    for i, chunk_start in enumerate(chunk_order):
        ordered_segments[chunk_order.index(chunk_start)] = segments[i]

    return ''.join(ordered_segments)