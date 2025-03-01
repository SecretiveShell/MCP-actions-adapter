import argparse
import json
import os
from typing import Annotated
from loguru import logger
from pydantic import BaseModel, Field
from mcp.client.stdio import StdioServerParameters


class Config(BaseModel):
    mcpServers: Annotated[
        dict[str, StdioServerParameters], Field(description="MCP server configuration")
    ]
    url: str = Field(description="Gateway URL included in openAPI spec")


def get_config():
    parser = argparse.ArgumentParser(
        description="A script that accepts a config file path via -c argument."
    )
    parser.add_argument(
        "-c", "--config", type=str, required=True, help="Path to the configuration file"
    )
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        required=False,
        help="Gateway URL included in openAPI spec",
    )

    args = parser.parse_args()
    args.config

    if not os.path.exists(args.config):
        logger.error(f"Config file {args.config} does not exist")
        exit(1)

    if not os.path.isfile(args.config):
        logger.error(f"Config file {args.config} is not a file")
        exit(1)

    try:
        with open(args.config, "r") as f:
            config = f.read()
            config = json.loads(config)
            config["url"] = args.url if args.url else config["url"]
            parsed_config = Config.model_validate(config)
    except Exception as e:
        logger.error(f"Error parsing config file: {e}")
        exit(1)

    return parsed_config


config: Config = get_config()
