# playwrightDemo

# Playwright Demo Project

## 📑 專案簡介
本專案是使用 [Playwright](https://playwright.dev/) 自動化測試框架所建置的一個範例，旨在進行瀏覽器自動化測試。  
透過本專案可以實現 UI 自動化測試、端對端測試以及多瀏覽器支援
---
## 🚀 專案特性
- 自動化測試：支援 Chrome、Firefox、WebKit 等瀏覽器。
- 撰寫測試：使用 TypeScript/Python 撰寫測試腳本。
- 自動化執行：支援 CI/CD 流程整合（如 GitHub Actions、Jenkins）。
- 報表生成：執行結果自動生成報表。

---

## 🛠️ 環境準備
### **1. 安裝 Node.js**
請確保已安裝 Node.js (版本 >= 16)  
[下載 Node.js](https://nodejs.org/)

### **2. 安裝 Playwright**
透過 安裝 Playwright：  
```bash
pip insall playwright
playwright install

```

### **3. 克隆專案**
```bash
git clone https://github.com/qa235/playwrightDemo.git
cd playwrightDemo
```
### **4. 安裝相依套件**
```bash
npm install
pip install pytest-playwright
playwright install
pip install pytest

```

---

## 📝 執行測試
### **1. 執行單一測試：**
```bash
1. **基本執行：**pytest tests/

Example:pytest tests/test_login.py-v
```

### **2. 執行所有測試：**
```bash
pytest tests/ --html=reports/report.html --self-contained-html -v

```

### **3. 生成測試報告：**
```bash
pytest tests/test_login.py --html=reports/report.html --self-contained-html -v && start reports/report.html

```
---

## 📂 專案結構
```
playwrightDemo/
├── tests/                   # 測試腳本
│   └── test_login.py        # 範例測試檔案
├── reports/  
│   ├── report.html          # 測試報告  
│   └── screenshots/         # 截圖存放資料夾  
└── package.json             # 套件資訊
└── README.md                 # 專案說明文件
```

---

## 🌟 貢獻指南
1. Fork 此專案至個人帳戶  
2. Clone 專案  
3. 建立新分支進行修改：  
   ```bash
   git checkout -b feature/new-feature
   ```
4. 提交變更：  
   ```bash
   git commit -m "新增功能"
   ```
5. 推送分支：  
   ```bash
   git push origin feature/new-feature
   ```
6. 建立 Pull Request，等待審核合併  

---

## 📧 聯繫方式
如有任何問題，歡迎聯繫我：qakaty672@gmail.com

