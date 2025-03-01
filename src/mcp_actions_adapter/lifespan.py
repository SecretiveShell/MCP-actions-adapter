import asyncio
import os
import shutil
from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager

from pydantic import BaseModel

from mcp_actions_adapter.config import config
import mcp.client
import mcp.client.stdio
import mcp.client.session

from mcp_actions_adapter.modeler import get_tool_model

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

    # print(server)

    async with mcp.client.stdio.stdio_client(server) as client:
        async with mcp.client.session.ClientSession(*client) as session:
            await asyncio.sleep(0.1)
            await session.initialize()
            server_session = session

            for tool in (await session.list_tools()).tools:
                print(tool)

                tool_name = tool.name
                input_schema = tool.inputSchema.get("properties", {})
                tool_description = tool.description

                ToolModel: type[BaseModel] = get_tool_model(tool_name, input_schema)

                async def tool_func(model: ToolModel = Depends()) -> str:
                    return "fake tool result"
                
                tool_func.__name__ = tool_name
                tool_func.__doc__ = tool_description

                app.post(f"/{tool_name}", response_model=str)(tool_func)

            yield
    
