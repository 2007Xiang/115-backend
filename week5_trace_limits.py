"""Week 5: trace JSONL, step limits and policy checks."""
from agent.core import AgentError, Trace, run_agent

if __name__ == "__main__":
    log = Trace()
    try:
        answer, path = run_agent("讀取 sample.txt 並告訴我主要內容", max_steps=5, trace=log)
        print(answer)
        print("可用記事本開啟紀錄：", path)
    except AgentError as exc:
        print("錯誤：", exc)
        print("相關紀錄：", log.path)
