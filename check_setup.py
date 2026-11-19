"""本機檢查 NVIDIA API 設定；不會印出金鑰，也不會發送網路請求。"""
import os
from pathlib import Path

key = os.getenv("NVIDIA_API_KEY", "").strip()
model = os.getenv("NVIDIA_MODEL", "minimaxai/minimax-m3.1-flash").strip()
print("Python 專案目錄：", Path(__file__).resolve().parent)
print("NVIDIA_MODEL：", model)
if not key:
    print("NVIDIA_API_KEY：未設定。請取得全新 NVIDIA Build API Key。"); raise SystemExit(1)
if key.lower().startswith("bearer "):
    print("NVIDIA_API_KEY：格式不對，環境變數只放金鑰，不要放 Bearer。"); raise SystemExit(1)
if key in {"你的金鑰", "你的NVIDIA_API金鑰", "your_key", "$NVIDIA_API_KEY"}:
    print("NVIDIA_API_KEY：目前是示範文字，請換成真正的新金鑰。"); raise SystemExit(1)
print("NVIDIA_API_KEY：已設定（已隱藏內容；不代表金鑰一定有效）")
print("本機設定檢查通過。請執行 python week1_single_call.py 實際確認 API。")
