# MCP vs API - Quick Revision Notes

## MCP (Model Context Protocol)
- Open standard for connecting AI agents with tools and data sources.
- Uses JSON-RPC 2.0.
- Components:
  - MCP Host
  - MCP Client
  - MCP Server

### MCP Primitives
- **Tools** → executable functions
- **Resources** → read-only data
- **Prompts** → prompt templates

### Key Feature
- Dynamic discovery:
  - tools/list
  - resources/list
  - prompts/list

## API
- General-purpose interface between applications.
- Typically REST over HTTP.

### Common Methods
- GET → Read
- POST → Create
- PUT → Update
- DELETE → Remove

## MCP vs API

| MCP | API |
|------|------|
| AI-focused | General-purpose |
| Dynamic discovery | Fixed endpoints |
| Standard interface | Service-specific interface |
| Built-in tool calling | Custom implementation |
| Runtime capability discovery | Usually not supported |

## Key Advantage of MCP
- Build once, integrate many.
- Agents can discover new capabilities automatically.

## Important Point
MCP does not replace APIs.

```text
AI Agent
  ↓
MCP Client
  ↓
MCP Server
  ↓
REST API
  ↓
Service
```

- MCP servers often act as wrappers around existing APIs.

## One-Line Summary
**API connects applications; MCP connects AI agents to tools and data in a standardized, discoverable way.**
