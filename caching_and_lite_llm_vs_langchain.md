# Abstraction Layers (Frameworks)

LLM frameworks — also called **abstraction layers** — sit between your code and the LLM provider APIs, giving you a simpler or more powerful way to work with models. They go by lots of names, but two are worth knowing well: **LangChain** and **LiteLLM**.

## LangChain

LangChain is by far the most famous LLM abstraction layer.

It's powerful, mighty, and quite heavyweight. There's a lot to learn: a fair number of important abstractions that let you work across many different models, but they come with real learning overhead.

**Example — asking GPT-5-mini to tell a joke:**

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5-mini")
response = llm.invoke([{"role": "user", "content": "Tell a joke"}])
print(response)
```

- You create a `ChatOpenAI` object.
- Call `.invoke()`, passing in your messages (a list of dicts).
- Print the result.

This particular example doesn't look too heavy — but that's just the entry point. There's much more depth once you go further (e.g. chains, agents, memory, tools).

To use a different provider with LangChain, you swap in a different import (`langchain_<provider>`) and create a different object connected to that provider.

## LiteLLM

LiteLLM sits at almost the opposite extreme from LangChain. It does exactly what its name says: it's a **very light**, simple abstraction layer that gives you one easy interface to call *any* model.

**Example:**

```python
from litellm import completion

response = completion(model="openai/gpt-4.1", messages=messages)
print(response.choices[0].message.content)
```

- It looks a lot like calling the OpenAI client directly — just with `completion` instead.
- You pass in a model string in the format `provider/model-name`.
- LiteLLM maintains the full list of supported providers.

The big win: if you want to call a model on **Bedrock** (AWS), you just prefix with `bedrock/`. Same idea for **Azure** and **Vertex AI** (Google) — any managed service, same pattern, same interface. That consistency is what makes LiteLLM so convenient for switching between models.

## Tracking Cost and Tokens

One of the most useful things LiteLLM gives you is a built-in utility to report **input tokens, output tokens, and cost** for every call.

Key takeaway on cost:
- For individual, everyday calls — even with a "big" model — the actual cost is tiny.
- LiteLLM lets you check costs per call, but you should still monitor usage on the provider platforms directly.

# Prompt Caching

Run the *same* large-context question a second time within a few minutes, and something interesting happens: the cost drops by about **5x**.

Why? Most of the input tokens are now marked as **cached tokens** — the provider detected a repeated (or similar) input context and reused it instead of reprocessing from scratch. This is **prompt caching**.

### Rules of thumb by provider

- **OpenAI (and generally):** The beginning of the prompt must match *identically* up to the point you want cached. 
 - **Trap:** if you put something that changes every time (like today's date) at the *start* of your prompt, you'll never get caching, because the prompt never starts identically twice.
 - **Fix:** put static content (like the full text of Hamlet) at the start, and put the variable part (your specific question) at the end.

- **Anthropic:** Caching is *not* automatic — you have to explicitly tell it to cache ("prime the cache"). 
 - Priming the cache costs **25% more** upfront.
 - But reusing from the cache afterward is about **10x cheaper** — a much bigger saving than OpenAI's, at the cost of a small upfront premium.

- **Gemini:** Supports both an implicit mode and an explicit mode (check provider docs for details).

### Why it matters

If you're cost-conscious and sending large prompts with lots of input context repeatedly, prompt caching is a great lever for cutting costs — but only if you structure your prompts correctly (static content first, variable content last).

LiteLLM makes this easy to observe in production: because it tracks tokens and spend per call, you can build systems that monitor usage and cost **per user or per client**, and compare that against revenue to keep your unit economics healthy.
