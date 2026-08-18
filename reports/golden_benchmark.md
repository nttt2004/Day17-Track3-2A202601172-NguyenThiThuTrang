# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **2110.6 ms**
- Average token reduction vs full source context: **14.5%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.6 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G06 | long_term | PASS | 3025.6 | 663 | 0.0% |  |
| G09 | semantic | PASS | 782.4 | 148 | 67.8% |  |
| G10 | semantic | PASS | 494.6 | 95 | 79.3% |  |
| G14 | mixed | PASS | 2791.4 | 431 | 0.0% |  |
| G03 | long_term | PASS | 2572.2 | 1253 | 0.0% |  |
| G04 | long_term | PASS | 2198.2 | 1255 | 0.0% |  |
| G07 | episodic | PASS | 312.9 | 274 | 0.0% |  |
| G08 | episodic | PASS | 1207.2 | 292 | 0.0% |  |
| G11 | mixed | PASS | 5200.9 | 439 | 22.3% |  |
| G13 | mixed | PASS | 1033.9 | 406 | 28.1% |  |
| G15 | mixed | PASS | 3119.9 | 736 | 0.0% |  |
| G16 | mixed | PASS | 5376.4 | 484 | 14.3% |  |
| G17 | mixed | PASS | 2574.8 | 484 | 14.3% |  |
| G18 | mixed | PASS | 954.8 | 403 | 28.7% |  |
| G19 | mixed | PASS | 3240.9 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1968.8 | 1250 | 0.0% |  |
| G12 | mixed | PASS | 3266.9 | 431 | 31.8% |  |
| G20 | mixed | PASS | 2090.4 | 609 | 3.6% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> Lan's main project is LOTUS-88, with a focus on Java and Spring Boot. Lan does not use Python for backend development. </USER_SUMMARY> EPISODE: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. EPISODE: Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. [EPISODES] Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. [ENTITIES] Name: Java Label: Topic Attributes: name: Java Summary: Lan Tran prioritizes Java for the LOTUS-88 project backend. [ENTITIES] Name: Spring Boot Label: Topic Attributes: name: Spring Boot Summary: Lan Tran prioritizes Spri`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G10 - semantic

`EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's main project is LOTUS-88, with a focus on Java and Spring Boot. Lan does not use Python for backend development. </USER_SUMMARY> EPISODE: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. EPISODE: Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. [EPISODES] Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend. [FACTS] Lan Tran does not use Python in the backend for the LOTUS-88 project example. (2026-08-01 11:00:00) FACT: Lan Tran does not use Python in the backend for the LOTUS-88 project example. [valid_at=2026-08-01T11:00:00`

### G03 - long_term

`<USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java`

### G04 - long_term

`<USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java`

### G07 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Hom nay to`

### G08 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: To`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khon`

### G13 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: TODO: hoan `

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khon`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day l`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khon`

### G18 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE:`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khon`

### G05 - long_term

`<USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh is working on a personal project named ORCHID-27, which uses Python. For a company project named BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project.  Minh prefers Python and dislikes Java. When explaining code, use short examples. When explaining async/await and the confusion between coroutines and Tasks, use a timeline for the explanation.  For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python should not be used for this project. The personal project ORCHID-27 continues to use Python. </USER_SUMMARY> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khon`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
