import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://ya.ru/")

login_button = driver.find_element(By.XPATH, "//a[@data-statlog='headline.enter']").click()

mail = driver.find_element(By.XPATH, "//button[@data-type='login']").click()

login = driver.find_element(By.ID, "passp-field-login").send_keys("Testovii.test.testovich")

login_button2 = driver.find_element(By.ID, "passp:sign-in").click()

password = driver.find_element(By.ID, "passp-field-passwd").send_keys("testovii")

login_button3 = driver.find_element(By.ID, "passp:sign-in").click()

all_services = driver.find_element(By.XPATH, "//a[@title='Все сервисы']").click()

disk = driver.find_element(By.XPATH, "//a[@data-statlog='services_pinned.more_popup.item.disk']").click()

disk_page = driver.window_handles[1]
driver.switch_to.window(disk_page)

create = driver.find_element(By.XPATH, "//button[@class='Button2 Button2_view_raised Button2_size_m Button2_width_max']").click()

folder = driver.find_element(By.XPATH, "//button[@aria-label='Папку']").click()
time.sleep(2)
folder_name = driver.find_element(By.XPATH, "//input[@text='Новая папка']").send_keys("New folder")
time.sleep(2)
save_button = driver.find_element(By.XPATH, "//button[@aria-disabled='false']").click()

new_folder_click = driver.find_element(By.XPATH, "//div[@aria-label='New folder']")
actionChains = ActionChains(driver)
actionChains.double_click(new_folder_click).perform()

time.sleep(2)

create_file = driver.find_element(By.XPATH, "//button[@class='Button2 Button2_view_raised Button2_size_m Button2_width_max']").click()
time.sleep(2)
text_file = driver.find_element(By.XPATH, "//button[@aria-label='Текстовый документ']").click()
time.sleep(2)
new_text_file = driver.find_element(By.XPATH, "//input[@text='Новый документ']").send_keys("New_file")
time.sleep(2)
confirm = driver.find_element(By.XPATH, "//button[@class='Button2 Button2_view_action Button2_size_m confirmation-dialog__button confirmation-dialog__button_submit ']").click()
time.sleep(2)

new_file_page = driver.window_handles[2]
time.sleep(2)
driver.switch_to.window(new_file_page)
driver.close()
time.sleep(2)
driver.switch_to.window(disk_page)
time.sleep(2)

check_new_file = driver.find_elements(By.XPATH, "//div[@aria-label='New_file.docx']")
if len(check_new_file) > 0:
    print("Файл New_file.docx создан успешно")
else:
    print("Файла New_file.docx не существует!")

user_pic = driver.find_element(By.XPATH, "//div[@class='user-pic user-pic_has-plus_ user-account__pic']").click()
log_out = driver.find_element(By.XPATH, "//span[text()='Выйти']").click()

time.sleep(2)
driver.quit()







