# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1127.4 ms**
- Average token reduction vs full source context: **20.9%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| E06 | semantic | PASS | 3091.7 | 148 | 67.8% |  |
| E09 | long_term | PASS | 1159.0 | 611 | 0.0% |  |
| E10 | short_term | PASS | 0.3 | 195 | 0.0% |  |
| E02 | long_term | PASS | 2334.0 | 916 | 0.0% |  |
| E03 | long_term | PASS | 1093.5 | 920 | 0.0% |  |
| E04 | episodic | PASS | 256.7 | 153 | 30.8% |  |
| E05 | episodic | PASS | 269.8 | 127 | 42.5% |  |
| E07 | mixed | PASS | 2167.0 | 485 | 14.2% |  |
| E11 | semantic | PASS | 261.2 | 146 | 74.2% |  |
| E08 | long_term | PASS | 1768.5 | 918 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata=`

### E09 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88, and they prioritize Java and Spring Boot for backend development.  Lan prioritizes Java and Spring Boot for backend development and avoids using Python for this purpose. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tie`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> The user is learning about async/await and coroutines versus Tasks, and is debugging async HTTP. Their personal project is named ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python. The user prefers Python for their personal demo project ORCHID-27. They are working to complete a benchmark report, labeled LAB-REPORT-1600, before Saturday at 4 PM. The user has tried increasing the timeout to 60 seconds and is checking the connection pool, client lifecycle, and concurrency. Recent efforts focused on resolving connection churn related to the ASYNC-FIX-20 incident by reusing the aiohttp ClientSession and setting concurrency to `

### E03 - long_term

`<USER_SUMMARY> The user is learning about async/await and coroutines versus Tasks, and is debugging async HTTP. Their personal project is named ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python. The user prefers Python for their personal demo project ORCHID-27. They are working to complete a benchmark report, labeled LAB-REPORT-1600, before Saturday at 4 PM. The user has tried increasing the timeout to 60 seconds and is checking the connection pool, client lifecycle, and concurrency. Recent efforts focused on resolving connection churn related to the ASYNC-FIX-20 incident by reusing the aiohttp ClientSession and setting concurrency to `

### E04 - episodic

`EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn.`

### E05 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Backend cua BLUEBIRD-42 bat buoc dung stack gi? EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi?`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is learning about async/await and coroutines versus Tasks, and is debugging async HTTP. Their personal project is named ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python. The user prefers Python for their personal demo project ORCHID-27. They are working to complete a benchmark report, labeled LAB-REPORT-1600, before Saturday at 4 PM. The user has tried increasing the timeout to 60 seconds and is checking the connection pool, client lifecycle, and concurrency. Recent efforts focused on resolving connection churn related to the ASYNC-FIX-20 incident by reusing the aiohttp ClientSession and setting con`

### E11 - semantic

`EPISODE: {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playbook-2026","updated_at":"2026-08-11T00:00:00Z"} metadata= EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. metadata=`

### E08 - long_term

`<USER_SUMMARY> The user is learning about async/await and coroutines versus Tasks, and is debugging async HTTP. Their personal project is named ORCHID-27. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS and not Python. The user prefers Python for their personal demo project ORCHID-27. They are working to complete a benchmark report, labeled LAB-REPORT-1600, before Saturday at 4 PM. The user has tried increasing the timeout to 60 seconds and is checking the connection pool, client lifecycle, and concurrency. Recent efforts focused on resolving connection churn related to the ASYNC-FIX-20 incident by reusing the aiohttp ClientSession and setting concurrency to `
