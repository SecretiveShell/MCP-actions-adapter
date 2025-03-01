from fastapi import FastAPI
from mcp_actions_adapter.config import config
from mcp_actions_adapter.lifespan import lifespan
from loguru import logger

app = FastAPI(
    title="MCP Actions Adapter",
    description="A simple adapter to convert a MCP server to a GPT actions compatible API",
    servers=[{"url": config.url}],
    lifespan=lifespan,
)

logger.info("Get openapi.json from http://localhost:8000/openapi.json")
