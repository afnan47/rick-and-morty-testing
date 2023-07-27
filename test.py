from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\aattar\\Downloads\\chromedriver.exe")
driver.get("http://localhost:3000")

def login():
    username = "afnan@mail.com"
    password = "12345678"
    # find username/email field and send the username itself to the input field
    driver.find_element(By.XPATH, '//label[text()="Email"]/../div//input').send_keys(username)
    # find password input field and insert password as well
    driver.find_element(By.XPATH, '//label[text()="Password"]/../div//input').send_keys(password)
    # click login button
    driver.find_element(By.XPATH, '//button[text()="Login"]').click()


def search():
    time.sleep(1)
    driver.find_element(By.XPATH, '//input[@id=":r5:"]').send_keys("Rick")
    time.sleep(2)
    characters = []
    while True:
        sel = driver.find_elements(By.XPATH, '//div[@data-colindex="0"]')
        for i in sel:
            characters.append(i.text)
        driver.execute_script("arguments[0].scrollIntoView();", sel[-1])
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, '//div[@class="MuiDataGrid-row MuiDataGrid-row--lastVisible"]')
            sel = driver.find_elements(By.XPATH, '//div[@data-colindex="0"]')
            for i in sel:
                characters.append(i.text)
            break
        except NoSuchElementException:
            continue
    print(set(characters))

def scroll_to_top():
    action = ActionChains(driver)
    while True:
        first = driver.find_elements(By.XPATH, "//div[@data-rowindex = '1']")
        res = driver.find_elements(By.XPATH, '//div[@data-field="name"]/div[text()]')
        action.scroll_to_element(res[0]).perform()
        if first:
            res = driver.find_element(By.XPATH, '//div[@data-rowindex = "1"]/div[@data-field="name"]/div[text()]')
            break
        time.sleep(3)


def sorting_a():
    sort_list = []
    scroll_to_top()
    sort_button = driver.find_element(By.XPATH, '//div/div[text()="Name"]/../../div/button[@title="Sort" and @type="button"]')
    ActionChains(driver).move_to_element(sort_button).click(sort_button).perform()
    action = ActionChains(driver)

    sort_list = []
    while True:
        sel = driver.find_elements(By.XPATH, '//div[@data-colindex="0"]')
        for i in sel:
            if i.text not in sort_list:
                sort_list.append(i.text)
        driver.execute_script("arguments[0].scrollIntoView();", sel[-1])
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, '//div[@class="MuiDataGrid-row MuiDataGrid-row--lastVisible"]')
            sel = driver.find_elements(By.XPATH, '//div[@data-colindex="0"]')
            for i in sel:
                if i.text not in sort_list:
                    sort_list.append(i.text)
            break
        except NoSuchElementException:
            continue
    
    unsorted = False
    for i in range(len(sort_list)-1):
        if sort_list[i] > sort_list[i+1]:
            unsorted = True
    if not unsorted:
        print("Ascending Sort took place")
    else:
        print("Ascending Sort did not take place")
    time.sleep(3)
    
if __name__ == "__main__":
    login()
    search()
    sorting_a()