"""Week 2: one tools-enabled model request and local tool dispatch."""
import json
from agent.core import AgentError, TOOL_SPECS, call_api, execute_tool

if __name__ == "__main__":
    try:
        msg, _ = call_api([{"role": "user", "content": "請使用 calculate 工具計算 24 * 7"}], TOOL_SPECS)
        for call in msg.get("tool_calls") or []:
            fn = call.get("function", {})
            try:
                args = json.loads(fn.get("arguments") or "{}")
                result = execute_tool(fn.get("name", ""), args)
            except json.JSONDecodeError as exc:
                result = {"ok": False, "error": f"參數 JSON 錯誤：{exc.msg}"}
            print(fn.get("name", ""), json.dumps(result, ensure_ascii=False))
        if not msg.get("tool_calls"):
            print("模型未要求工具呼叫：", msg.get("content"))
    except AgentError as e:
        print("錯誤：", e)
