import ssl
import time

from selenium import webdriver
import chromedriver_autoinstaller
import dbconfig

ssl._create_default_https_context = ssl._create_unverified_context

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

# 드라이버 설치
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  # 해당경로에 드라이버가 있으면 불러오고
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  # 없으면 설치
    driver.close()

url = 'https://app.modeal.net'
driver.get(url)  # url 호출
time.sleep(3)

elm = driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/ul/li[4]')
elm.click()

# 전체 브랜드 목록.
elm = driver.find_element_by_xpath('//*[@id="create_list"]')
maker = elm.text.split("\n")
# print(maker)
# print(len(maker))

for e in maker:
    if e == '현대':
        # print("현대")
        elm = driver.find_element_by_xpath('//*[@id="create_list"]/li[1]/a/figure/img')
        elm.click()
        time.sleep(3)
        car_list = driver.find_element_by_css_selector('#wrap > section > div > ul')
        # print(car_list[0].text) 0번으로 다 출력이됨.
        car_list = car_list.text.split("\n")
        # print(car_list)
        # print(len(car_list))

        for n in car_list:
            if n == "아반떼":
                # print("아반떼")
                car_name = driver.find_element_by_xpath('//*[@id="wrap"]/section/div/ul/li[1]/div/div')
                car_name.click()
                time.sleep(3)  # 3초대기 걸어줘야됨 안걸어줄경우 너무 빨리 지나감.
                car_line = driver.find_element_by_css_selector('#wrap > section > div > ul > li.m_item.active > ul')
                # print(car_line[0].text)
                car_line = car_line.text.split("\n")

                for l in car_line:
                    if l == '아반떼':
                        a = driver.find_element_by_xpath('//*[@id="wrap"]/section/div/ul/li[1]/ul/li[1]/a')
                        a.click()
                        time.sleep(3)
                        fuel = driver.find_element_by_css_selector('#wrap > section > div > ul')
                        fuel = fuel.text.split('\n')
                        # print(fuel)
                        for f in fuel:
                            if f == '가솔린 1.6  [2020년형]':
                                a = driver.find_element_by_xpath('//*[@id="wrap"]/section/div/ul/li[1]/a')
                                a.click()
                                time.sleep(3)
                                model = driver.find_element_by_xpath('//*[@id="wrap"]/section/div/ul')
                                # print(model.text)
                                model = model.text.split('\n')
                                # print(model[0::2]) # 파이썬 슬라이싱 기법 2의 간격의 인덱스들 추출
                                for m in model[0::2]:
                                    # print(m)
                                    if m == '스마트 (수동)':
                                        a = driver.find_element_by_xpath('//*[@id="wrap"]/section/div/ul/li[1]/p')
                                        a.click()
                                        time.sleep(3)
                                        a = driver.find_element_by_xpath(
                                            '//*[@id="wrap"]/section/div/ul/li[1]/div/ul[2]/li[3]/a')
                                        a.click()
                                        time.sleep(3)
                                        month = driver.find_element_by_xpath(
                                            '/html/body/div[2]/section/article[4]/form/div/div[1]/div/div/select')
                                        # print(month.text)

                                        month = month.text.split('\n')
                                        # print(month)

                                        if month[2]:
                                            print(month[2])
                                            month_36 = driver.find_element_by_xpath('//*[@id="PERD_CD"]/option[3]')
                                            month_36.click()
                                            time.sleep(3)
                                            adpay = driver.find_element_by_xpath('//*[@id="PAYPRO_text"]/option[1]')
                                            # print(adpay.text)
                                            adpay.click()
                                            time.sleep(3)
                                            # print(adpay.text)

                                            # adpay = adpay.text.split('\n')
                                            # print(adpay)  # 선수금
                                            if adpay.text.__contains__("0%"):
                                                print("36개월")
                                                adpay = adpay.text.split("|")
                                                print(adpay)
                                                deposit = driver.find_element_by_xpath('//*[@id="DEPPRO_text"]')
                                                # print(deposit.text) # 보증금
                                                deposit_text = deposit.text
                                                deposit = deposit.text.split('\n')
                                                # print(deposit[0])
                                                deposit = deposit[0].split("|")
                                                print(deposit)
                                                residual = driver.find_element_by_xpath(
                                                    '//*[@id="REPRT_AMT"]/option[2]')  # 최대잔가 고정 리스트 출력이 안됨.
                                                # print(residual.text)  # 잔존가치
                                                dits = driver.find_element_by_xpath(
                                                    '//*[@id="STIP_DST_CD"]/option[3]')  # 2만키로 고정 디폴트 2만 돼있어서 클릭이벤트를 주진 않았음.
                                                # print(dits.text)
                                                # city = driver.find_element_by_xpath('//*[@id="PBDBT_CITY_CD"]') # 리스트로 출력됨
                                                # print(city.text, "리스트?")
                                                city = driver.find_element_by_xpath('//*[@id="PBDBT_CITY_CD"]/option[11]')
                                                # print(city.text)

                                                merits = driver.find_element_by_xpath(
                                                    '//*[@id="e2_list"]/tr[1]/td[1]/label')
                                                # print(merits.text)
                                                monthly_pay = driver.find_element_by_xpath(
                                                    '//*[@id="e2_list"]/tr[1]/td[2]')
                                                # print(monthly_pay.text)
                                                # print(e, n, l, f, m, month[2], adpay[1],  deposit[1], residual.text, dits.text, city.text, merits.text, monthly_pay.text)
                                                data_list = [e, n, l, f, m, month[2], adpay[1],  deposit[1], residual.text, dits.text, city.text, merits.text, monthly_pay.text, " ", " ", " ", " ", " ", " ", " ", " "]
                                                dbconfig.insert_sql(data_list) # 깃허브 테스트1

                                        if month[3]:
                                            print(month[3])
                                            month_48 = driver.find_element_by_xpath('//*[@id="PERD_CD"]/option[4]')
                                            month_48.click()
                                            time.sleep(3)
                                            adpay = driver.find_elements_by_css_selector('#PAYPRO_text')
                                            # print(adpay[0].text)
                                            adpay = driver.find_element_by_xpath('//*[@id="PAYPRO_text"]/option[1]')
                                            adpay.click()
                                            time.sleep(3)
                                            # print(adpay.text)

                                            # adpay = adpay.text.split('\n')
                                            # print(adpay)  # 선수금
                                            if adpay.text.__contains__("0%"):
                                                # print("타냐?")
                                                deposit = driver.find_element_by_xpath('//*[@id="DEPPRO_text"]')
                                                # print(deposit.text) # 보증금
                                                deposit = deposit.text.split('\n')
                                                # print(deposit[0])
                                                residual = driver.find_element_by_xpath(
                                                    '//*[@id="REPRT_AMT"]/option[2]')  # 최대잔가 고정 리스트 출력이 안됨.
                                                # print(residual.text)  # 잔존가치
                                                dits = driver.find_element_by_xpath(
                                                    '//*[@id="STIP_DST_CD"]/option[1]')  # 2만키로 고정 리스트 출력이 안됨.
                                                # print(dits.text)
                                                city = driver.find_element_by_xpath('//*[@id="PBDBT_CITY_CD"]')
                                                # print(city.text)
                                                merits = driver.find_element_by_xpath(
                                                    '//*[@id="e2_list"]/tr[1]/td[1]/label')
                                                print(merits.text)
                                                monthly_pay = driver.find_element_by_xpath(
                                                    '//*[@id="e2_list"]/tr[1]/td[2]')
                                                print(monthly_pay.text)
                    elif l == '아반떼 N':
                        print('아반떼 N')

    elif e == '제네시스':
        print("제네시스")

# elm = driver.find_element_by_xpath('//*[@id="create_list"]/li[1]')

# if elm.text == '현대':
#     # 현대
#     elm = driver.find_element_by_xpath('//*[@id="create_list"]/li[1]/a/figure/img')
#     elm.click()
#     time.sleep(3)

driver.close()
