# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **2832.1 ms**
- Average token reduction vs full source context: **19.1%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.2 | 133 | 0.0% |  |
| E06 | semantic | PASS | 8202.5 | 53 | 88.4% |  |
| E09 | long_term | PASS | 3021.8 | 617 | 0.0% |  |
| E10 | short_term | PASS | 0.6 | 195 | 0.0% |  |
| E02 | long_term | PASS | 7601.1 | 1266 | 0.0% |  |
| E03 | long_term | PASS | 2820.2 | 1295 | 0.0% |  |
| E04 | episodic | PASS | 224.2 | 234 | 0.0% |  |
| E05 | episodic | PASS | 238.0 | 253 | 0.0% |  |
| E07 | mixed | PASS | 6465.3 | 390 | 31.0% |  |
| E11 | semantic | PASS | 684.7 | 52 | 90.8% |  |
| E08 | long_term | PASS | 1894.8 | 1297 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.`

### E09 - long_term

`<USER_SUMMARY> Lan's main project is LOTUS-88, with a focus on Java and Spring Boot. Lan does not use Python for backend development. </USER_SUMMARY> EPISODE: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. EPISODE: Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. [EPISODES] Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. [EPISODES] Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. [ENTITIES] Name: Python Label: Topic Attributes: name: Python Summary: Lan Tran does not use Python in the backend for the LOTUS-88 pro`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPI`

### E03 - long_term

`<USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop `

### E04 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Toi d`

### E05 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Da gh`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khon`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.`

### E08 - long_term

`<USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScrip`
