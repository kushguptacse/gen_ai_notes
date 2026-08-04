How Gradio Works

Gradio is a simple framework that turns Python code into web UIs.

The Three Things Gradio Does
1. Generates Frontend from Python

You describe your UI in Python using Gradio components like gr.Textbox(), gr.Button(), or gr.ChatInterface().

Gradio takes your Python description and generates a Svelte frontend (which compiles down to vanilla JavaScript). Your high-level Python code becomes a complete, interactive web interface.

2. Starts a Web Server

When you call .launch(), Gradio spins up a Starlette web server in the background.

The server listens on a port (default is 7860, then increments if occupied)
It serves your generated frontend to anyone who visits

That's it. You now have a live web app.

3. Connects Callbacks to Routes

You pass Gradio your Python callback functions (like def chat(message):).

Gradio automatically:

Creates backend routes for each callback
Wires your frontend buttons/inputs to hit those routes
Takes the function's return value and populates it back into the UI

The frontend code handles all the plumbing—no extra work needed.

Why This Matters

Fast prototyping: Write Python, get a deployed web UI in seconds.

Scalable: Starlette can handle real load. This works for internal tools and MVPs, not just toys.

Natural migration path: Start with Gradio's UI, later swap in a custom frontend (React, Next.js, etc.) while keeping your Gradio backend as an API.