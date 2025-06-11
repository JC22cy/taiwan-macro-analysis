import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path('data')
OUTPUT_DIR = Path('output')
OUTPUT_DIR.mkdir(exist_ok=True)

# Load sample data
cpi = pd.read_csv(DATA_DIR / 'cpi.csv')
gdp = pd.read_csv(DATA_DIR / 'gdp.csv')
wage = pd.read_csv(DATA_DIR / 'wage.csv')

# Ensure data is sorted by Year
cpi = cpi.sort_values('Year').reset_index(drop=True)
gdp = gdp.sort_values('Year').reset_index(drop=True)
wage = wage.sort_values('Year').reset_index(drop=True)

# Calculate YoY growth rates
cpi['YoY'] = cpi['Value'].pct_change() * 100
gdp['YoY'] = gdp['Value'].pct_change() * 100
wage['YoY'] = wage['Value'].pct_change() * 100

# Merge data for correlation
merged = cpi[['Year', 'YoY']].merge(wage[['Year', 'YoY']], on='Year', suffixes=('_CPI', '_WAGE'))
correlation = merged['YoY_CPI'].corr(merged['YoY_WAGE'])

# Plot CPI and GDP trends
plt.figure(figsize=(8,4))
plt.plot(cpi['Year'], cpi['Value'], label='CPI Index')
plt.plot(gdp['Year'], gdp['Value']/1000, label='GDP (thousand units)')
plt.title('CPI and GDP Trend (Sample Data)')
plt.xlabel('Year')
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'cpi_gdp_trend.png')
plt.close()

# Plot YoY growth rates
plt.figure(figsize=(8,4))
plt.plot(cpi['Year'], cpi['YoY'], label='CPI YoY %')
plt.plot(gdp['Year'], gdp['YoY'], label='GDP YoY %')
plt.plot(wage['Year'], wage['YoY'], label='Real Wage YoY %')
plt.title('YoY Growth Rates (Sample Data)')
plt.xlabel('Year')
plt.ylabel('Percent')
plt.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / 'yoy_growth.png')
plt.close()

# Generate Markdown report
report_lines = [
    '# 台灣 CPI、GDP、實質薪資分析 (範例資料)',
    '',
    '此報告示範如何載入資料並計算年增率與相關性。',
    '',
    f'- CPI 與實質薪資年增率相關係數: {correlation:.2f}',
    '',
    '![CPI & GDP Trend](cpi_gdp_trend.png)',
    '',
    '![YoY Growth Rates](yoy_growth.png)',
]

report_path = OUTPUT_DIR / 'report.md'
with open(report_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(report_lines))

print(f'Report generated: {report_path}')

# Optional: convert to PDF if pandoc is available
if os.system('which pandoc > /dev/null') == 0:
    os.system(f'pandoc {report_path} -o {OUTPUT_DIR / "report.pdf"}')
    print('PDF report generated.')
else:
    print('Pandoc not found. PDF was not generated.')
