# LLM Basics: 

1. Context Windows
2. API Costs

---

## 1. What is a Context Window?

The **context window** is the maximum number of tokens a model can look back on when deciding what to generate next. Think of it as the model's short-term memory — a limited-size whiteboard it can glance at while writing its next word.

If you try to feed in more than the model's context window allows, it simply fails with an error like "input too large."

### How generation actually works — and why input + output share one budget

LLMs generate text **one token at a time**, and each time they do, the *whole* conversation gets fed back in:

1. You send the full conversation so far.
2. The model predicts the single most likely next token (e.g., `"Your"`).
3. That new token gets appended, and the **entire updated sequence** is fed back into the model.
4. The model predicts the next token (e.g., `"name"`).
5. This repeats — `"is"`, then `"kush"` — until the reply is complete.

Because every generated token has to be re-fed in along with everything before it, the context window isn't just holding your conversation history — it's also holding the model's reply as it's being written, right up to (but not including) the very last token. So input and output tokens draw from the **same pool**:

> `input tokens + output tokens ≤ context window`

**Example:** if a model has a 400,000-token context window and your conversation history + prompt already uses 390,000 tokens, the model only has **10,000 tokens left** to write its entire response — even if its "max output" limit is technically much higher (e.g. 128,000 tokens). Run out of room mid-answer, and the response gets cut off.

This is why some providers list two separate numbers: a total **context window** (input + output combined) and a smaller **max output tokens** cap (a ceiling on any single response, regardless of how much room is left in the window).

---

## 2. API Costs

### Subscription vs. API — two different worlds

| | Chat product (e.g. ChatGPT app) | API |
|---|---|---|
| **Pricing** | Flat monthly subscription ($20–$200/month) | Pay-per-use |
| **Limits** | Rate-limited, but no per-message charge | No subscription needed — just pay for what you use |
| **Use case** | Personal/casual use | Building your own product on top of the model |

API costs pay for the actual compute happening behind the scenes — and indirectly help offset the enormous cost of training these models in the first place (often $100M+).

### What you're actually paying for

Cost is based on two things:

1. **Input tokens** — and this includes the *entire* conversation history you're feeding in each time (all your "fake memory," any RAG content, etc.), not just your latest message.
2. **Output tokens** — including any hidden "reasoning" tokens some models generate behind the scenes before giving you the final answer. You pay for these even if you never see them.

> **Why pay for the full history each time?** Because the model genuinely needs to reprocess the whole conversation to predict the next token accurately. You *could* only send your latest message and skip the history to save money — but your results will suffer. It's a real trade-off between cost and quality.

### Real-world pricing examples

Generating the entire works of Shakespeare (~1M tokens) would cost about **$10** with GPT-5, or **less than $1** with GPT-5 nano. For everyday small prompts like "Hi, my name is Ed," the actual cost is a tiny fraction of a cent — divide the per-million rate by roughly 100,000.

### A money-saving trick: caching

If you send the *same* input repeatedly within a short window of time, some providers charge you less because that input gets cached:

- **OpenAI (GPT):** Automatic.
- **Claude (Anthropic):** More nuanced — caching is possible but requires more deliberate setup.

---

## Key Takeaways

- 🧠 **Context window** = the total token budget for one exchange — conversation history **and** the model's reply share the same pool.
- 🔁 Text generation happens **one token at a time**, with the whole conversation re-fed into the model at every step.
- 💵 **API cost** = input tokens (full history) + output tokens (including hidden reasoning), billed per million tokens.
- 📊 Context windows vary a lot: GPT-5 (400K) < Claude (200K)... up to Gemini 2.5 Flash (1M).
- 🐢 For casual, one-off use, API costs are negligible. They add up fast only when you're running large-scale or agentic systems that loop through many calls.