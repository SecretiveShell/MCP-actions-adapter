import asyncio
import os
import shutil
from fastapi import FastAPI
from contextlib import asynccontextmanager
from mcp_actions_adapter.config import config
import mcp.client
import mcp.client.stdio
import mcp.client.session

server_session = None

def get_server():
    global server_session
    return server_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    global server_session
    server = config.mcpServers.popitem()[1]
    server.command = shutil.which(server.command) or server.command

    server.env = os.environ.copy() | (server.env or {})

    print(server)

    async with mcp.client.stdio.stdio_client(server) as client:
        async with mcp.client.session.ClientSession(*client) as session:
            await asyncio.sleep(0.1)
            await session.initialize()
            server_session = session
            yield
    
