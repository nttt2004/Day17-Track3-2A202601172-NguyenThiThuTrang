# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **2**
- Passed: **2/2**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **345.9 ms**
- Average token reduction vs full source context: **89.6%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E06 | semantic | PASS | 457.9 | 53 | 88.4% |  |
| E11 | semantic | PASS | 234.0 | 52 | 90.8% |  |

## Evidence excerpts

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.`
