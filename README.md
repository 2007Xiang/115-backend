# NVIDIA AI Agent Week 1–6：Windows CMD 完整教學（MiniMax M3.1 Flash）

此專案是依照短影片中可辨識的 Week 1–6 主題製作的教學實作，不是課程官方原始碼。需自行確認老師的具體繳交規範。

## 重要：舊 API Key 已經公開，必須輪替

若曾經將完整 `nvapi-...` 金鑰貼在聊天、截圖或任何公開位置，**應先到 NVIDIA Build 撤銷這組舊金鑰，重新生成全新金鑰**。不可繼續用舊金鑰，也不可把新金鑰放進 `.py`、README、截圖、版本控制或繳交的壓縮檔。

## 1. 安裝與確認

- Windows 10/11、Python 3.10 以上、網路連線
- 在檔案總管進入這個專案資料夾，點網址列輸入 `cmd` 後 Enter，或使用 `cd /d C:\...\NVIDIA_AI_Agent_HW`
- 在 CMD 逐行執行：

```cmd
python --version
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

如果 `python` 無法使用，改用 `py`；必須在正確的專案目錄執行。

## 2. NVIDIA Build 建立新的金鑰

官方模型頁：https://build.nvidia.com/minimaxai/minimax-m3.1-flash/build

1. 登入 NVIDIA Build，尋找 Generate API Key，取得**新的** NVIDIA API Key（不是 MiniMax 官方平台的金鑰）。
2. 在剛才同一個 **CMD 視窗**執行以下指令，把「新金鑰」替換成真的金鑰，只放金鑰本體，不要加入 `Bearer `：

```cmd
set "NVIDIA_API_KEY=在這裡貼上新產生的NVIDIA金鑰"
set "NVIDIA_MODEL=minimaxai/minimax-m3.1-flash"
python check_setup.py
```

> `set` 在目前 CMD 視窗有效，關閉後須重新設定。不要執行 `echo %NVIDIA_API_KEY%`；也不要截圖金鑰。設定方式不會把金鑰寫入任何專案程式檔案。

> 2026-11-19 已核對官方 API 文件：模型 ID `minimaxai/minimax-m3.1-flash`、Chat Completions URL `https://integrate.api.nvidia.com/v1/chat/completions`，認證標頭 `Authorization: Bearer <NVIDIA_API_KEY>`，本程式使用非串流回應 (`stream: false`)，Accept 為 `application/json`。可否呼叫仍依 API Key 有效性與帳號權限而定。

## 3. 執行 Week 1～6

先跑 Week 1，成功後繼續：

```cmd
python week1_single_call.py
python week2_tool_call.py
python week3_agent_loop.py
python week4_multi_tools.py
python week5_trace_limits.py
python harness.py
```

- Week 1：單次 API 請求，應得到繁體中文解釋 API 的文字。
- Week 2：嘗試要求 AI 呼叫 `calculate(24,7,multiply)`，結果應為 `168`。若模型沒有呼叫工具，畫面會明確提示。
- Week 3：Agent 讀取 `workspace/sample.txt`，計算 24×7，並以對話迴圈完成。
- Week 4：本機測試 `read_file`/`calculate`/不合法工具；**會故意出現錯誤回傳**，不需 Key。
- Week 5：Agent 產生 `outputs/trace_*.jsonl` 紀錄，附加執行限制。
- Week 6：完整互動 CLI：輸入任務，輸入 `exit` 結束。

另可執行：

```cmd
python harness.py "請讀取 sample.txt 並整理三個重點"
python harness.py "請使用 calculate 工具計算 18 除以 3"
python harness.py --max-steps 5
```

`run_windows.bat` 也可以啟動 Week 6，但啟動前必須在相同工作階段設定 Key，或從已設定變數的 CMD 執行批次檔。

## 4. API 401 故障排除

`401 Unauthorized` = **伺服器拒絕此次認證**，不代表 Python 語法錯。依序確認：

1. 是否已將之前暴露的 NVIDIA Key **撤銷並產生新 Key**。
2. 金鑰是否來自 **NVIDIA Build** 而不是 MiniMax 平台。
3. `python check_setup.py` 是否顯示已設定（此步驟只檢查存在，不會測試有效性）。
4. 是否在**相同 CMD 視窗**中設定，再執行 Python。
5. Key 內容只貼 `nvapi-...`，**不要貼** `Bearer nvapi-...`，不要加多餘空格、引號。
6. 若仍為 401，請到 NVIDIA Build 重新產生金鑰並查看帳號權限；不要再公開金鑰。

`410` = 模型已停用；`403` = 帳號/資源權限可能不足；`404` = 路由或模型 ID 可能不符；`429` = 速率/額度限制。`200` 才表示該 API 請求成功。

## 5. 程式檔案

| 檔案 | 用途 |
|---|---|
| `check_setup.py` | 檢查金鑰環境變數是否存在，不顯示內容、不連線 |
| `week1_single_call.py` | Week 1：單次 API 呼叫 |
| `week2_tool_call.py` | Week 2：Tool Calling |
| `week3_agent_loop.py` | Week 3：對話迴圈 |
| `week4_multi_tools.py` | Week 4：工具錯誤回傳 |
| `week5_trace_limits.py` | Week 5：紀錄與限制 |
| `harness.py` | Week 6：互動式整合 Agent |
| `agent/core.py` | 共用 API、工具與 Agent 核心 |
| `tests/test_agent.py` | 不用 API Key 的單元測試 |
| `run_windows.bat` | Windows 批次啟動 |

## 6. 安全與限制

- `workspace/` 才能由 `read_file` 讀取，檔案類型與大小受限制。
- `http_get` 僅用於教學，仍有 DNS rebinding 風險，不建議部署到內網伺服器。
- `outputs/trace_*.jsonl` 可能包含輸入任務、工具資料；不要直接公開上傳。
- 本機單元測試**不等於** NVIDIA 線上 API 測試，本環境未持有你的有效新金鑰，所以無法代替你驗證 200。

## 官方資料

- NVIDIA 模型官方 API Reference：https://build.nvidia.com/minimaxai/minimax-m3.1-flash/apireference
- NVIDIA 模型 Build：https://build.nvidia.com/minimaxai/minimax-m3.1-flash/build
- NVIDIA API 文件：https://docs.api.nvidia.com/nim/reference/minimaxai-minimax-m3-1-flash-infer
- Python Requests：https://requests.readthedocs.io/en/latest/
