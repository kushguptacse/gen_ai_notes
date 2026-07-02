# AI Agent Memory (CoALA) -- Quick Notes

## Overview

CoALA (Cognitive Architectures for Language Agents) defines **4 memory
types** used by AI agents.

  -----------------------------------------------------------------------
  Memory           Purpose            Typical Storage
  ---------------- ------------------ -----------------------------------
  **Working**      Current session    LLM context window
                   context            

  **Semantic**     Facts & knowledge  Markdown, Vector DB, Knowledge
                                      Graph

  **Procedural**   Task execution     `skill.md`
                   skills             

  **Episodic**     Past experiences   Distilled memory store
  -----------------------------------------------------------------------

## 1. Working Memory

-   Temporary (RAM-like)
-   Fast but limited by context window
-   Cleared after the session

## 2. Semantic Memory

Stores persistent knowledge: - Documentation - Coding standards -
Architecture - Business rules

Example: - `Claude.md` - Company knowledge base - RAG documents

## 3. Procedural Memory

Stores **how** to perform tasks.

Uses **Agent Skills** (`skill.md`) containing: - Task description -
Step-by-step workflow - Required scripts/templates

### Progressive Disclosure

-   Load only skill metadata like name and description initially.
-   Load full instructions only when the skill is selected.
-   Reduces context/token usage.

## 4. Episodic Memory

Stores distilled experiences instead of full conversations.

Example: - ✅ "Auth issue was caused by middleware." - ❌ Entire
45-minute debugging transcript.

Challenges: - What to remember? - What to forget? - When does memory
become obsolete?

## Key Differences

  Question                 Memory
  ------------------------ ------------
  What is happening now?   Working
  What do I know?          Semantic
  How do I do this?        Procedural
  What happened before?    Episodic

## Key Takeaways

-   **Working** = Current context.
-   **Semantic** = Persistent knowledge.
-   **Procedural** = Reusable skills.
-   **Episodic** = Learned experience.
