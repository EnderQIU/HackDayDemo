import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import json
import xlwt

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders

    return style

def main(uid="18602706460", pwd="QtI@Uaqy547"):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
    driver = webdriver.Chrome()
    driver.get("http://www.iqiyi.com/iframe/loginreg")
    time.sleep(2)
    use_pwd = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[6]/div[2]/p/span/a[1]")
    use_pwd.click()
    username= driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div[2]/input")
    password = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/input[1]")
    time.sleep(1)
    username.send_keys(uid)
    password.send_keys(pwd)
    time.sleep(20)
    driver.get("http://www.iqiyi.com/u/record")
    time.sleep(1)
    soup = bs(driver.page_source, "html.parser")
    histories = soup.select(".portrait_title")
    rest_times = soup.select(".mod-listTitle_right")
    videos = []
    for h, r in zip(histories, rest_times):
        title = h.next
        rtime = r.text
        href = h.attrs["href"]
        driver.get(href)
        spoon = bs(driver.page_source, "html.parser")
        tags = spoon.select("#datainfo-taglist")
        _tags = tags[0].text.strip("\n").split("\n")
        s = rtime[2:]
        l = s.split(":")
        if len(l) == 3:
            rtime = int(l[0]) * 60 + int(l[1])
        else:
            rtime = int(l[0])
        videos.append({"title": title, "tags": _tags, "time": rtime})

    wb = xlwt.Workbook()
    sheet1 = wb.add_sheet("sheet1", cell_overwrite_ok=True)
    default = set_style('Times New Roman', 220, True)

    for video, row in zip(videos, range(len(videos))):
        sheet1.write(row, 0, len(video), default)
        sheet1.write(row, 1, str(video["tags"]), default)
        sheet1.write(row, 2, video["time"], default)
    wb.save("wb.xls")
    return json.dumps(videos)


if __name__ == "__main__":
    print(main())
