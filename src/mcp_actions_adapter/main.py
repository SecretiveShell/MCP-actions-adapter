from fastapi import FastAPI
from mcp_actions_adapter.config import config
from mcp_actions_adapter.lifespan import lifespan

app = FastAPI(
    title="MCP Actions Adapter",
    description="A simple adapter to convert a MCP server to a GPT actions compatible API",
    servers=[{"url": config.url}],
    lifespan=lifespan,
)

