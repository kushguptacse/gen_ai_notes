# Understanding Tools in LLMs

## What Are Tools?

Tools are a fundamental building block in modern AI. They allow a language model to connect to external functions and execute code:

- **Call external functions** - Connect to code you've written
- **Retrieve data** - Query databases or external sources
- **Take actions** - Book tickets, run calculations, execute Python code
- **Enhance capabilities** - Do things a text-generating model couldn't do alone


## How Tool Calling Actually Works

1. **Your code** sends a message to the LLM with instructions that it *can* use tools, plus a user question
2. **The LLM** generates tokens that say: "Please call this tool"
3. **Your code** detects this request and actually runs the tool/function
4. **Your code** sends the result back to the LLM as part of the conversation history
5. **The LLM** generates a final response based on the tool's answer

The LLM is **still just generating tokens**. Those tokens happen to be a request for a tool call — nothing more magical than that.

## How Does the LLM Know to Call Tools?

Simple: **You tell it in the prompt.**

In your first message to the LLM, you describe:
- What task you want it to perform
- What tools are available (in JSON)
- How to ask for a tool (usually in JSON format)

The LLM was trained on countless examples of JSON tool descriptions, so it already knows how to respond in that format. When you give it a question, if a tool would help, it simply responds with the tool call request.
