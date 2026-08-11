# Tokenizers

## What a tokenizer is

A tokenizer is a bit of code that maps between natural language and the numbers that represent that natural language. That's its job.

```
natural language  →  tokens  →  token IDs
   "words and         little      the numbers
    letters"          chunks
```

1. **You begin with natural language** — words and letters that make up a sentence. That's your starting point.
2. **The tokenizer turns this into tokens** — little chunks of words.
3. **The tokenizer turns each token into a number.** Every possible token has a different number associated with it — which is called the **token ID**. It's like its index in the list of all possible tokens.

### Token vs. token ID

| Term | What it actually is |
|---|---|
| **Token** | The fragment of a word — the chunk |
| **Token ID** | The number that represents that chunk |

A token is a block of letters together that makes up part of a word. Or it can be a whole word. But that is a token. In-general token is 0.75 of word.

People often say "token" when they mean "token ID," and it doesn't really matter. But strictly speaking: **the token is the chunk, the ID is the number.**

---

## The dictionary

The tokenizer has a **dictionary** — and I mean that both in the Python sense and just in the normal sense. It's a lookup thing that holds:

- A list of all the possible tokens it knows about — the **vocab**
- An ID associated with each one

It uses this to look up a chunk and replace it with its ID. That vocab is all the possible things it can break text down into.

It **also** contains a few **special tokens** that don't map to any natural language word — special tokens that are going to be used to inform the model about something.

---

## Special tokens

An example special token: one that represents *"this is the beginning of a prompt. This is the start of what I want to tell you."*

That has its own number. Let's say it's the number **10**. Then the number 10 gets used in the numbers we pass into the LLM any time we want to represent the start of a prompt. And that's how it will know.

### The important bit — how special tokens actually work

When I say the LLM is going to "know" that 10 is the start of a prompt:

In all the training data — the masses and masses of training data — we repeatedly used the number 10 at the start of every single prompt. And because we always did that, the neural network learned over time, from all the examples, that this is an indication of what's coming next. And it got better and better at predicting next tokens when it saw similar kinds of constructs.

Given enough examples with the number 10 always starting a new prompt, it has seen those patterns and it replicates those patterns. So starting a prompt with token ID 10 **orients the statistics correctly** so that it predicts patterns better. That's the point.

---

## Every model has its own tokenizer

Different LLMs don't need to use the same approach for tokenizing — for turning text into token IDs. In fact, they typically don't.

Typically, when someone's building a model, they build the tokenizer that they think makes the most sense: that treats words and turns them into IDs in the way they like, and uses special tokens in the way they want to for training.

So you potentially have a different tokenizer for every model you work with.


---

## Two typical questions

### 1. "Does it matter? Is one model more efficient because it uses fewer tokens for the same sentence — so it's cheaper?"

Honestly, it's not worth worrying about anything like that.

These decisions are very small, trivial decisions that people made to try and get a bit more juice out of their model. If one tokenizer makes fewer tokens, then maybe you're saving a fraction of a cent in terms of your input token use — but maybe the model gives slightly worse results, or slightly better.

The much more important factor is **the quality of the results given the input you give it**, rather than exactly how many tokens it maps to.

That's something of a red herring. Don't get too bogged down in why different tokenizers produce different numbers of tokens. It's more important to understand that **a tokenizer belongs to a model**, without getting hung up on the kinds of tokens it creates.

### 2. "Are tokens the same as vectors?"

No.
**tokens are not the same as vectors.** Vectors come from deeper within the neural network, *after* the tokens have been what's called **embedded** into the model.

All models — including models that create vectors — **take in tokens as their inputs.**

Because statistical models can only talk in numbers. They don't know what it means to have a word. So you have to input something in the form of numbers, and the numbers we choose are the token IDs. That's how we first feed information into a model.

```
IN:   token IDs                        ← always, for all models
OUT:  a vector embedding
      / the next token
      / lots of different things
```

So **tokenization is a step before you get to things like vectors**, which we'll cover later. Just in case that was confusing you — that clears it up.


## Creating our first tokenizer

We do that using a Hugging Face class called **`AutoTokenizer`**, which has this one static class method, **`from_pretrained`**, which takes in the name of a model from Hugging Face.

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B")
```

The Hugging Face model name is made of two parts:

- the **Hugging Face ID** — `meta-llama`, that's Meta's name for the Meta Llama account
- the **name of the model** itself — `Meta-Llama-3.1-8B`

So you pass that in.

- `from_pretrained` means: *this is a pre-trained model, I want you, Hugging Face, to look this up.*
- `AutoTokenizer` means: *please create the right kind of tokenizer for this model* and return it into this variable `tokenizer`.

---

## Encode and decode

`encode` and `decode` are the two main methods you can call on a tokenizer.

### `encode` — text → token IDs

```python
text = "I am excited to show Tokenizers in action to my LLM engineers"
tokens = tokenizer.encode(text)
print(tokens)
```

it's turning text into **token IDs**.

**Let's count:**

| | |
|---|---|
| Characters | 61 |
| Words | 12 |
| Tokens | 15 |

Seems roughly in line with the rule of thumb. it's about **0.75 of a word to a token**, on average.


**These numbers make sense to an LLM.** It's expecting them; it's been trained off lots of numbers like that. You couldn't put that *text* into a statistical model — a weighted thing with lots of parameters that combines numbers. It needs numbers. You need numbers to combine numbers. And here are the numbers it would expect to receive.

### `decode` — token IDs → text

```python
tokenizer.decode(tokens)
```

```
<|begin_of_text|>I am excited to show Tokenizers in action to my LLM engineers
```

That's a **special token** getting decoded at the beginning.

That 128000 maps to the special token **`<|begin_of_text|>`**. And that special token tells the LLM *hey, this is the start of some text to you.*

### `batch_decode` — token IDs → the individual pieces

```python
tokenizer.batch_decode(tokens)
```

`batch_decode` is a bit different to `decode`.

Instead of giving you the whole sentence back, it turns it into the **individual tokens**:

```
['<|begin_of_text|>', 'I', ' am', ' excited', ' to', ' show', ' Token',
 'izers', ' in', ' action', ' to', ' my', ' LL', 'M', ' engineers']
```

That's showing you the individual token breakdown.

---
