# Test Time Compute (Thinking Models) - Quick Notes

## Traditional LLMs (Train-Time Compute)

LLMs improve by:
- More parameters
- More training data
- More compute (FLOPs)

After training:
- Weights are frozen
- Same inference process for every query

Issue:
- One forward pass, means once next token is generated it cannot go back, it always moves on to predict next new token.
- Can hallucinate if initial reasoning is wrong

---

# What is Test Time Compute? (Thinking Models)

Extra compute used during inference.

Flow:

Query

↓

Thinking

↓

Answer

The "Thinking..." message represents this reasoning stage.

---

# Mechanism 1: Chain of Thought

Model generates thinking tokens before the final answer.

Thinking tokens:
- Break problem into steps
- Explore different approaches
- Change direction before committing

Reasoning models use Reinforcement Learning (RL) to do this automatically.

---

# Mechanism 2: Search

Instead of one reasoning path:

- Create multiple branches
- Score each branch using a verifier
- Continue with the best branch

---

# Mechanism 3: Self-Consistency

Solve the same problem multiple times.

Example:
- 10 reasoning paths
- 7 reach same answer

Use majority vote as final answer.

---

# Trade-offs

Benefits:
- Better reasoning
- Higher accuracy
- Small models can outperform much larger models on difficult tasks

Costs:
- Higher latency
- More output tokens
- Higher inference cost
- Overthinking may reduce performance on simple questions

---

# CAPEX vs OPEX

Train-Time Compute
- CAPEX
- Paid once during training

Test-Time Compute
- OPEX
- Paid per query

---

# Best Practice

Adaptive Routing

Easy Query

↓

Fast Model

Hard Query

↓

Reasoning Model

Many chatbots automatically choose the appropriate path.

---

# Easy Memory Trick

Train-Time Compute = Learn More

Test-Time Compute = Think More

Training makes the model smarter.

Test-time compute spends extra compute only on difficult problems.
