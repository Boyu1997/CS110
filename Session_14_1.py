import heapq
import urllib
import os
from collections import defaultdict
from bitarray import bitarray
import cPickle as pickle


# Download the file if need be:
def download_file(url, filename):
    if not os.path.exists(filename):
        urllib.urlretrieve(url + filename, filename)


# build a frequency table:
def build_freq(filename):
    freq = defaultdict(int)
    with open(filename, 'r') as f:
        for line in f:
            for char in line.decode('utf-8-sig'):
                freq[char] += 1
    total = float(sum(freq.values()))
    return {char: count / total for (char, count) in freq.items()}


# Now build the Huffman encoding:
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights.

    Accept a dictionary which maps a symbol to a probability.
    Return a new dictionary which maps a symbol to a bitarray."""

    raise NotImplementedError()


# Now compress the file:
def compress(filename, encoding, compressed_name=None):
    if compressed_name is None:
        compressed_name = filename + ".huff"
    output = bitarray()
    with open(filename, 'r') as f:
        for line in f:
            for char in line.decode('utf-8-sig'):
                output.extend(encoding[char])
    N = len(output)
    with open(compressed_name, 'wb') as f:
        pickle.dump(N, f)
        pickle.dump(encoding, f)
        output.tofile(f)


# Now decompress the file:
def decompress(filename, decompressed_name=None):
    if decompressed_name is None:
        decompressed_name = filename + ".dehuff"
    with open(filename, 'rb') as f:
        N = pickle.load(f)
        encoding = pickle.load(f)
        bits = bitarray()
        bits.fromfile(f)
        bits = bits[:N]

    # Totally cheating here and using a builtin method:
    output = bits.decode(encoding)

    output = "".join(output).encode('utf-8-sig')
    with open(decompressed_name, 'wb') as f:
        f.write(output)


url = "https://www.gutenberg.org/ebooks/"
filename = "100.txt.utf-8"

download_file(url, filename)
freq = build_freq(filename)
encoding = encode(freq)
compress(filename, encoding)
decompress(filename + ".huff")
# Do you get identical files?