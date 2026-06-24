# A2A vs MCP - Quick Notes

## Problem
AI agents need a standard way to:
- Talk to other agents
- Access databases, files, APIs, and code repositories

Protocols:
1. A2A (Agent-to-Agent)
2. MCP (Model Context Protocol)

---

# A2A (Agent-to-Agent Protocol)

### Purpose
Allows different AI agents to communicate and collaborate.

### Key Features
- Open protocol
- Exchange requests, responses, negotiation and coordination messages
- Uses Agent Cards (agent resume/capabilities)
- Supports text, images, files, and structured data
- Uses HTTP + JSON-RPC 2.0
- Supports streaming updates via SSE

### Best Use Case
Agent ↔ Agent communication

---

# MCP (Model Context Protocol)

### Purpose
Allows an AI agent to access external tools and data in a standard way.

Examples:
- File systems
- Databases
- Code repositories

### Architecture
- MCP Host = AI application where agent runs
- MCP Server = Connects to tools/resources and provides a uniform interface

### MCP Primitives
1. Tools – actions/functions
2. Resources – files/data/state
3. Prompts – reusable templates

### Communication
- JSON-RPC
- Local: stdin/stdout
- Remote: HTTP with streaming support

### Advantages
- Build integration once, reuse everywhere
- Existing MCP servers for Slack, GitHub, databases, file systems, etc.

### Best Use Case
Agent ↔ Tools/Data communication

---

# A2A vs MCP

| A2A | MCP |
|------|------|
| Agent talks to Agent | Agent talks to Tools/Data |
| Multi-agent collaboration | External resource access |
| Uses Agent Cards | Uses Tools, Resources, Prompts |

---

# Easy Memory Trick

- A2A = Agent → Agent
- MCP = Agent → Tools/Data

A2A handles collaboration.
MCP handles context and integrations.
Both are complementary, not competing.
