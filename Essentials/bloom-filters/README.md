# Bloom Filter Implementation

## Overview
This project demonstrates a simple Bloom Filter implementation using a bit array.

A Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set.  
It is space-efficient but may produce false positives.

## Implementation Details

1. Implemented a Bloom Filter using a bit array.
2. Used two text files:
   - `words.txt` → used to populate the filter
   - `new.txt` → used to test for false positives
3. Words from `words.txt` are inserted into the Bloom Filter.
4. Words from `new.txt` are checked against the filter to measure false positives.

## Observations

Bit Array Size: 1016  
False Positive Rate: ~0%

Bit Array Size: 50  
False Positive Rate: ~35%

Bit Array Size: 16  
False Positive Rate: ~79%

## Key Insight

As the size of the bit array decreases, the collision probability increases, which leads to more false positives.

This demonstrates the trade-off in Bloom Filters between memory usage and false positive probability.