def main() -> None:
    from uvicorn import run

    run("mcp_actions_adapter.main:app", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
