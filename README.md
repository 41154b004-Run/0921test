# BMI 計算器 (Python BMI Calculator)

[![Python CI](https://github.com/41154b004-Run/0921test/actions/workflows/ci.yml/badge.svg)](https://github.com/41154b004-Run/0921test/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一個使用 Python 撰寫的輕量級命令列身體質量指數（BMI）計算工具。

---

## 專案結構

```text
.
├── .github/workflows/ci.yml   # GitHub Actions 自動測試流程
├── .editorconfig              # 程式碼編輯器排版設定
├── .gitignore                 # Git 忽略檔案清單
├── LICENSE                    # MIT 開源授權條款
├── README.md                  # 專案說明文件
├── pyproject.toml             # Python 專案現代化配置
├── requirements.txt           # 專案依賴套件清單
├── hello.py                   # BMI 計算主程式
└── tests/
    └── test_hello.py          # 單元測試程式
```

---

## 功能特點

- **精確計算**：支援身高（公分）與體重（公斤）輸入並精準換算 BMI。
- **健康分級**：參照衛福部/WHO 標準提供體重等級評估（過輕、正常、過重、肥胖）。
- **防呆驗證**：自動攔截負數、零及非數字等無效輸入。
- **持續整合**：內建 GitHub Actions CI，每次 Push 自動跑單元測試。

---

## 快速開始

### 1. 執行主程式
```bash
python hello.py
```

### 2. 執行單元測試
```bash
python -m unittest discover -s tests
```

---

## 授權條款
本專案採用 [MIT License](LICENSE) 授權。
