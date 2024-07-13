import pandas as pd
import csv
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_lat_long(station_name):
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'text_'))
    )
    result_element = driver.find_element(By.ID, 'result_')
    input_element.clear()
    input_element.send_keys(station_name)
    button = driver.find_element(By.XPATH, '//input[@value="查询"]')
    button.click()
    try:
        WebDriverWait(driver, 20).until(
            EC.text_to_be_present_in_element_value((By.ID, 'result_'), ',')
        )
        lat_long = result_element.get_attribute('value').split(',')
    except TimeoutException:
        lat_long = "99999,99999".split(',')

    result_element.clear()
    return float(lat_long[0]), float(lat_long[1])

def main():
    with open('xian_bus_info.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data_list = []
        for row in reader:
            route_name = row[0]
            direction_b = row[6].strip('"').split(',')[:-1]

            for station in direction_b:
                lat, long = get_lat_long(station+"公交站")  # ("西安" + station)
                data_entry = {
                    "线路名称": route_name,
                    "站点": station,
                    "纬度": lat,
                    "经度": long
                }
                data_list.append(data_entry)
                print(f"Processed station: {data_entry}")

    # 使用pandas创建DataFrame
    df = pd.DataFrame(data_list)

    # 写入Excel文件
    df.to_excel('bus_stations_lines.xlsx', index=False)


if __name__ == "__main__":
    driver_path = "chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    # 使用os.path.join来构建正确的文件路径
    from os.path import abspath, dirname, join
    file_path = abspath(join(dirname(__file__), 'index.html'))
    url = f'file://{file_path}'
    
    driver.get(url)
    main()
    driver.quit()