"""Week 6: final interactive command-line AI agent."""
import argparse
from agent.core import AgentError, run_agent


def main():
    parser = argparse.ArgumentParser(description="NVIDIA AI Agent (Week 6)")
    parser.add_argument("task", nargs="?", help="要交給 Agent 的任務；省略則進入互動模式")
    parser.add_argument("--max-steps", type=int, default=8, help="最多執行幾個 AI 回合，預設 8")
    args = parser.parse_args()
    print("NVIDIA AI Agent - 輸入 exit 結束")
    while True:
        try:
            task = args.task or input("\n任務 > ").strip()
            if task.lower() in {"exit", "quit"}: break
            if not task: continue
            answer, trace = run_agent(task, max_steps=args.max_steps)
            print("\nAI 回覆：\n" + answer)
            print("\n執行紀錄：" + str(trace))
        except (KeyboardInterrupt, EOFError):
            print("\n結束")
            break
        except AgentError as exc:
            print("執行失敗：" + str(exc))
        if args.task: break

if __name__ == "__main__":
    main()
