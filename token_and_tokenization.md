# Tokens and Tokenizers

## Chapter 1: What Are Tokens?

### The Problem: How Do You Feed Text Into a Neural Network?

A neural network doesn't understand words or letters — it only understands numbers. So before any text can be processed, it has to be broken into pieces and each piece needs to be turned into a number.

The big question researchers had to answer was: **what should those pieces be?** A single character? A whole word? Something in between?

The answer — and the reason you hear the word "token" so often — came after trying a few different approaches, each with its own tradeoffs.

---

### Attempt 1: Character by Character

Early neural networks were trained to read text **one character at a time**, predicting the next most likely character.

**Why this seemed like a good idea:**
- There are only about 100 possible characters (uppercase, lowercase, punctuation)
- A tiny, simple vocabulary
- Low memory usage, very efficient

**Why it didn't work well:**
- The network had to do *too much work* — it had to learn how characters combine to form words **and** figure out what those words mean, all at once
- Too much was left for the model to figure out from scratch

---

### Attempt 2: Whole Words

The next obvious idea: treat **each word** as one input unit.

**Why this seemed like a good idea:**
- Words already carry meaning, so the model doesn't have to "build" meaning from scratch

**Why it didn't work well:**
- Human language has an enormous number of words
- Add in proper nouns — names of people, places, brands — and the list of possible words explodes
- Rare words had to be left out of the vocabulary entirely, meaning the model simply couldn't understand them

---

### The Breakthrough: Tokens (A Middle Ground)

The solution was to stop thinking in extremes (character vs. word) and instead use **chunks of text** — pieces that could be:
- A whole word
- A fragment of a word
- Occasionally, two common words joined together

This chunk-based vocabulary is what we call **tokens**.

| Approach | Vocabulary Size | Problem |
|---|---|---|
| Character-level | Very small (~100) | Model has to learn too much from scratch |
| Word-level | Huge, ever-growing | Can't cover every possible word/name |
| **Token-level** | **Constrained, manageable** | **Best of both worlds** |

**Why tokens work so well:**
- The vocabulary can be limited to a fixed, manageable size
- It can always fall back to character-level chunks if needed for rare/unknown text, so nothing is truly "left out"
- It's efficient and fast to train
- It naturally picks up on **word stems** — since a chunk of characters is often followed by a smaller chunk that just modifies it (e.g., a root word plus a suffix), which fits naturally with how we already spell and write things

> Note: Tokens aren't some deep theoretical requirement — the model *could* have been trained on characters or entire word dictionaries instead. Tokens simply turned out to be a highly efficient compromise, similar to how the transformer architecture works well in practice without being the *only* possible design.

---

### Where Tokens Fit In: Tokens vs. Vectors

This is a common point of confusion, so it's worth being explicit:

- **Tokens** are the very first input into a language model. Specifically, it's not the token itself but the **token ID** — a number representing which token from the vocabulary it is.
- **Vectors** are a *different*, later concept in the pipeline. They come further downstream in the neural network.

Whether the model is generating the next token or building a vector representation, the very first thing it receives is always the **token ID** — nothing more. Vectors come later 

---

### Try It Yourself

You can experiment with how real text gets broken into tokens using OpenAI's tokenizer tool:
👉 `platform.openai.com/tokenizer`

Paste in any sentence and see exactly how it gets split into token chunks — it's the fastest way to build intuition for this concept.

---

## Chapter 2: How tokenization works

Tokenization is the process of converting raw text into a sequence of tokens that a language model can understand. It's like translating human language into the model's native tongue.

### Key Points to Remember

- **It's learned, not predefined**: The tokenizer doesn't have a fixed set of rules about what makes a good token — it learns them entirely from the text it's trained on.
- **Not all tokenizers work the same**: While Byte-Pair Encoding (BPE) is very common (used by GPT-3, GPT-4, Llama, etc.), there are other methods like WordPiece (used by BERT) and SentencePiece (used by many models), though they all follow the same core idea of learning common text chunks.
- **Goal: Balance efficiency and flexibility**: The tokenizer tries to find the sweet spot where it can represent text using the fewest possible tokens (for efficiency) while still being able to represent any possible text (using smaller chunks when needed).
- **The tokenization process is consistent**: For a given tokenizer and a given input text, the output will always be the same — the same tokenization will always produce the same token sequence.

- **Roughly, a token is like three quarters of a word, so a thousand tokens would be about 750 words.**

---
