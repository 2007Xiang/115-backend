"""Week 1: one Chat Completions request, no tools."""
from agent.core import AgentError, call_api

if __name__ == "__main__":
    try:
        message, _ = call_api([{"role": "user", "content": "請用繁體中文說明 API 是什麼，100 字內。"}])
        print("AI：", message.get("content") or "（模型沒有文字回答）")
    except AgentError as e:
        print("錯誤：", e)
