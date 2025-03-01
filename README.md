# MCP Actions Adapter

A simple adapter to convert a MCP server to a GPT actions compatible API

## Installation

```bash
uv tool install mcp-actions-adapter
```

## Usage

1) Create config.json the same way as claude desktop. An example config file is provided in the `config.example.json` file.

2) Start a cloudflare tunnel with the following command:

```bash
cloudflared tunnel --url http://localhost:8000
```

3) Start the adapter with the following command:

```bash
uv run mcp-actions-adapter -c config.json --url ${CF_TUNNEL_URL}
```
4) Open the custom GPT builder and copy the contents of http://localhost:8000/openapi.json into the schema box.

5) test the model

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details