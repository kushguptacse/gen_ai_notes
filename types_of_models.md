# LLM Model Types

A quick reference to the three main types of Large Language Models (LLMs).

---

## 1. Base Model

Predicts the next token/word in a sequence — similar to smartphone predictive text.

- ❌ No chat capability or reasoning
- Raw, unaligned language model

**Best for:**
- Model fine-tuning
- Training new behaviors

---

## 2. Chat (Instruction) Model

Fine-tuned on top of a base model to follow user instructions using **RLHF** *(Reinforcement Learning from Human Feedback)*.

Uses a structured conversation format:

| Role      | Description                        |
|-----------|------------------------------------|
| System    | Sets the assistant's behavior/tone |
| User      | The human's message                |

**Best for:**
- General conversations
- Fast responses
- Lower cost

---

## 3. Reasoning (Thinking) Model

Trained to think step-by-step before answering. Produces an internal **reasoning trace** before the final response.

- ⚠️ Slower and more expensive due to reasoning tokens

**Better at:**
- Logic
- Mathematics
- Coding
- Complex problem solving

---

## Quick Comparison

| Feature            | Base Model | Chat Model | Reasoning Model |
|--------------------|:----------:|:----------:|:---------------:|
| Follows instructions | ❌        | ✅         | ✅              |
| Step-by-step thinking | ❌      | ❌         | ✅              |
| Speed              | Fast       | Fast       | Slow            |
| Cost               | Low        | Low        | High            |
| Best use case      | Fine-tuning | Conversations | Complex tasks |