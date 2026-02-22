# Single Thread Benchmark (Toy Test)

All 3 DBs are running on Docker on same machine.
Dataset size: 10k records.
Test type: Random primary key reads, single thread, warm cache.

========== RESULTS ==========

MySQL:
Total Time     : 10.1823 sec
Avg Latency    : 1.0182 ms
Requests/sec   : 982.09

MongoDB:
Total Time     : 12.0093 sec
Avg Latency    : 1.2009 ms
Requests/sec   : 832.69

Redis:
Total Time     : 7.3682 sec
Avg Latency    : 0.7368 ms
Requests/sec   : 1357.18


Learnings:

- Redis is fastest, but not dramatically faster.
- MySQL and MongoDB are already very fast for indexed reads.
- With 10k records, everything fits in memory.
- No disk I/O was involved (warm cache).
- This is single-thread, so no concurrency pressure.
- Python loop overhead affects total timing.
- Localhost network latency is minimal.
- Benchmark results depend on workload, not just technology.

Conclusion:

For simple indexed lookups on small datasets, all modern databases perform very well.
Real performance differences appear under high concurrency, large datasets, or resource limits.
