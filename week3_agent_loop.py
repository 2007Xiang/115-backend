"""Week 3: repeated tool calls and chat context."""
from agent.core import AgentError, run_agent

if __name__ == "__main__":
    try:
        answer, path = run_agent("請讀取 sample.txt，整理重點，並用 calculate 計算 24 乘 7。", max_steps=6)
        print(answer, "\n紀錄：", path)
    except AgentError as e:
        print("錯誤：", e)
