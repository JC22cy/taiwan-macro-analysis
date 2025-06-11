# taiwan-macro-analysis

台灣 CPI/GDP 數據分析專案

此範例專案提供 `analysis.py`，示範如何載入近十年 CPI、GDP 與實質薪資資料，計算年增率並繪製圖表，最終匯出 Markdown（及可選的 PDF）報告。

## 使用方法

1. 安裝相依套件：
   ```bash
   pip install pandas matplotlib
   ```

2. 準備資料：
   - `data/cpi.csv`：CPI 指數資料，欄位需包含 `Year,Value`。
   - `data/gdp.csv`：GDP 數值資料，欄位需包含 `Year,Value`。
   - `data/wage.csv`：實質薪資指數資料，欄位需包含 `Year,Value`。

   專案附有範例資料，可直接執行取得示範結果。

3. 執行分析：
   ```bash
   python analysis.py
   ```

   圖表與 `report.md` 將輸出至 `output/` 目錄。若系統安裝了 `pandoc`，將同時產生 `report.pdf`。
