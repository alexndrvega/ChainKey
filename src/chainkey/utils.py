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

    return chunks, chunk_order

# data_restored
def data_restored(segments, chunk_order):
    ordered_segments = [None] * len(segments)
    chunk_size = len(segments[0])

    for i, chunk_start in enumerate(chunk_order):
        ordered_segments[chunk_start // chunk_size] = segments[i]

    restored_data = ''.join(segment for segment in ordered_segments if segment is not None)
    return restored_data