# Hugging Face Ecosystem: Platform + Libraries

## Overview
Hugging Face is two things: **a platform** (the Hub website with repos of models, datasets, and spaces) and **a set of open-source Python libraries** for working with transformer models. This note focuses on the libraries.

## Hugging Face Libraries vs. Running a Model Like Llama

| | Ollama-style (e.g. Llama) | Hugging Face Libraries |
|---|---|---|
| What it is | Pre-built software/application | Raw Python code you run yourself |
| How you use it | Runs locally, exposes an OpenAI-compatible API endpoint | Import code, download weights, run in Jupyter/Cursor/Colab |
| Customization | None — it's a black box | Full access: swap layers, tweak tokens, fine-tune |
| Format | Packaged model files (e.g. GGUF) run via efficient C++ | Live PyTorch/TensorFlow/JAX code |

**In short:** Llama-style tools = fast, pre-baked software. Hugging Face = the actual source code, fully hackable.

## The Six Core Libraries

### Foundational
1. **Hub** — the Python library that connects your code to the Hugging Face Hub (the website), letting you log in and pull down models/datasets programmatically.
2. **Datasets** — once you pull a dataset via the Hub, it becomes an object in this library. Built for efficiently manipulating very large volumes of data.
3. **Transformers** — the flagship library. Lets you load a model, get its code, run it, and train it. This is the heart of the Hugging Face ecosystem.

### Advanced (used later in the course)
4. **PEFT** (Parameter-Efficient Fine-Tuning) — lets you fine-tune a model without updating all of its billions of parameters. Underlies techniques like **LoRA**.
5. **TRL** (Transformers Reinforcement Learning) — for training transformers via reinforcement learning.
6. **Accelerate** — distributes model training/inference across multiple GPUs.

## Key Takeaway
Originally these libraries were built around models like Meta's Llama, but today they support nearly any open-source model. Note the naming overlap: "Hub" is both the website *and* the library used to talk to it.