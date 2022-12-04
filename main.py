from selenium import webdriver
from selenium.webdriver.common.by import By
from eth_account import Account
import time,os,sqlite3,requests



def creat_db():
    pwd = os.getcwd()
    db_pwd = pwd + "/zelta.db"
    print(db_pwd)
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('''CREATE TABLE zelta (
                id INTEGER,
                address VARCHAR(256),
                private_key VARCHAR,
                phrases VARCHAR(256),
                Gmail VARCHAR,
                status VARCHAR

                );''')
    conn.commit()
    conn.close()
    print("created successfully")
def creat_wallet(number):
    pwd = os.getcwd()
    db_pwd = pwd + "/zelta.db"
    print(db_pwd)
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    for i in range(number):
        c.execute("SELECT COUNT(*) FROM zelta;")
        count = c.fetchall()[0][0]
        print(count)
        Account.enable_unaudited_hdwallet_features()
        account,mnemonic=Account.create_with_mnemonic()
        address=account.address
        private_key= account.key.hex()
        phrases=mnemonic
        print("current count:"+str(count))
        print("address: "+address)
        print("hex: "+private_key)
        print("mnemonic: "+phrases)
        c.execute("INSERT INTO zelta (id,address,private_key,phrases)VALUES('%s','%s','%s','%s')"%(count,address, private_key, phrases))
        conn.commit()
    conn.close()

def regist_selenium ():
    pwd = os.getcwd()
    db_pwd = pwd + "/zelta.db"
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('SELECT * from zelta where Gmail LIKE "%@%"')
    rows = c.fetchall()
    count=1
    WEB_DRIVER_PATH = pwd + "/tool/chromedriver"
    opt = webdriver.ChromeOptions()
    opt.page_load_strategy = "none"
    driver = webdriver.Chrome(executable_path=WEB_DRIVER_PATH, options=opt)
    driver.get("https://zelta.io/")
    time.sleep(1)
    for i in rows:
        google_email=i[4]
        secret_key = i[3].split(" ")
        address=i[1]
        print("当前循环数量 "+str(count))
        print("当前钱包地址："+str(address))
        print("当前钱包助记词："+str(secret_key))
        print("当前email："+str(google_email))
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/main/div[1]/div[1]/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="chakra-modal--body-2"]/form/input[2]').clear()
        driver.find_element(By.XPATH, '//*[@id="chakra-modal--body-2"]/form/input[3]').clear()
        email = driver.find_element(By.XPATH, '//*[@id="chakra-modal--body-2"]/form/input[2]')
        email.send_keys(google_email)
        polygon_address = driver.find_element(By.XPATH, '//*[@id="chakra-modal--body-2"]/form/input[3]')
        polygon_address.send_keys(address)
        driver.find_element(By.XPATH, '//*[@id="chakra-modal--body-2"]/form/button').click()


        try:
            driver.find_element(By.XPATH, '//div[contains(@style,"visibility: visible")]')
            print("verification required skip")
            driver.refresh()
        except:

            try:
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="chakra-modal--header-2"]/button').click()
                c.execute("update zelta set status ='User signed up successfully' where address='%s';" % (address))
                conn.commit()
                print("User signed up successfully")
            except:
                c.execute("update zelta set status ='ALREADY_EXISTS' where address='%s';" % (address))
                conn.commit()
                print("aALREADY_EXISTS")


        count=count+1
        print("&&&&&&&&&&&&&")
        time.sleep(2)

def regist_post ():
    websiteURL_post = "https://asia-south1-pbnative-403e0.cloudfunctions.net/register"
    db_pwd = "./zelta.db"
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('SELECT * from zelta where Gmail LIKE "%@%"')
    rows = c.fetchall()
    count=1
    time.sleep(1)
    for i in rows:
        google_email=i[4]
        address=i[1]
        print("当前循环数量 "+str(count))
        print("当前钱包地址："+str(address))
        print("当前email："+str(google_email))
        data = {"data":{"email":google_email,"address": address}}
        r = requests.post(websiteURL_post, json=data)
        if "ALREADY_EXISTS" in r.text:
            c.execute("update zelta set status ='ALREADY_EXISTS' where address='%s';" % (address))
            conn.commit()
            print("ALREADY_EXISTS")
        elif "User signed up successfully" in r.text:
            c.execute("update zelta set status ='User signed up successfully' where address='%s';" % (address))
            conn.commit()
            print ("User signed up successfully")
        count=count+1
        print("&&&&&&&&&&&&&")
        time.sleep(2)

if __name__ == '__main__':
    #creat_db()
    #creat_wallet(20)
    #regist_selenium()
    regist_post()
