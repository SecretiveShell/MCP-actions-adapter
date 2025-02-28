from fastapi import FastAPI

app = FastAPI(
    title="MCP Actions Adapter",
    description="A simple adapter to convert a MCP server to a GPT actions compatible API",
)

