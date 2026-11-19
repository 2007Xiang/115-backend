"""Week 4: multiple tools with structured error returns."""
import json
from agent.core import execute_tool

if __name__ == "__main__":
    cases = [("read_file", {"path": "sample.txt"}),
             ("read_file", {"path": "missing.txt"}),
             ("calculate", {"a": 20, "b": 4, "operation": "divide"}),
             ("calculate", {"a": 20, "b": 0, "operation": "divide"}),
             ("invalid_tool", {})]
    for name, args in cases:
        print(name, json.dumps(execute_tool(name, args), ensure_ascii=False))
