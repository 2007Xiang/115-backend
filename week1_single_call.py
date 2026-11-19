"""Week 1: One HTTP POST and inspect message, status, usage."""
from agent.cli import load_env
from agent.core import NvidiaClient, get_message, ApiError, settings

if __name__ == "__main__":
    load_env()
    cfg = settings()
    client = NvidiaClient(model=cfg["model"], url=cfg["api_url"], timeout=cfg["timeout"], max_tokens=cfg["max_tokens"])
    try:
        result = client.complete([{"role": "user", "content": "用一句話解釋 HTTP。"}])
        print("status_code: 200 (HTTP request succeeded)")
        print("content:", get_message(result).get("content"))
        print("usage:", result.get("usage"))
    except ApiError as exc:
        print(exc)
        raise SystemExit(1)
