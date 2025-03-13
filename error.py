from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")

# 启动浏览器
driver = webdriver.Chrome(options=chrome_options)

# 打开 Coinglass 页面
driver.get("https://www.coinglass.com/zh/pro/i/FearGreedIndex")

# 等待页面加载
time.sleep(5)

data = driver.execute_script("""
    let chart = echarts.getInstanceByDom(document.querySelector('echarts-for-react'));  // 需要你提供图表的div或class
    return chart.getOption().series[0].data;
""")
print(data[:5])  # 预览

# 关闭浏览器
driver.quit()

df = pd.DataFrame(data, columns=['date', 'fear_greed_index'])
print(df.head())
df.to_csv('coinglass_fear_greed.csv', index=False)
print("数据已保存")