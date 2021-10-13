# import time
import time
from datetime import timedelta, date

# db
import psycopg2

# selenium
from selenium import webdriver  # import selenium
from selenium.webdriver.common.keys import Keys  # keys import
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

PATH = 'D:\projects\pepcoding web\pep mentor assignment\selenium\chromedriver.exe'


options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(PATH, options=options)

# connect to the db
con = psycopg2.connect(
    host="localhost",
    database="pepcoding_assignment",
    user="postgres",
    password="root"
)


# cursor
cur = con.cursor()


while True:
    # Code executed here
    # execute query
    # TODO: get all the pincodes from the table availability and put them in a list
    try:
        cur.execute("delete from availabilities")
        con.commit()
        cur.execute("select distinct pincode from logins")
        rows = cur.fetchall()
        print(rows)
        for pincode in rows:
            driver.find_element_by_tag_name(
                'body').send_keys(Keys.CONTROL + 'n')
            driver.get("https://www.cowin.gov.in/")
            elementClick = driver.find_elements_by_css_selector(
                ".mat-ripple.mat-tab-label.mat-focus-indicator.ng-star-inserted.mat-tab-label-active")
            elementClick[0].click()
            search = driver.find_element_by_id('mat-input-0')
            search.send_keys(pincode)
            # click a search button
            search.send_keys(Keys.ENTER)
            # wait for the element to load
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'div.row.ng-star-inserted'))
                )
                table = driver.find_elements_by_css_selector(
                    'div.row.ng-star-inserted')
                for row in table:
                    hospitalName = row.find_element_by_css_selector('p').text
                    slots = row.find_elements_by_css_selector('li')

                    for i in range(len(slots)):
                        if slots[i].text != 'NA' and i != 0:
                            details = slots[i].text.split("\n")
                            print(details)
                            if len(details) > 4:
                                print(details)
                                vaccine = details[0]
                                dose1 = details[2]
                                dose2 = details[5]
                                total = details[3]
                                Date_req = date.today() + timedelta(days=i)
                                print(pincode)
                                print(hospitalName)
                                print(details)
                                print(vaccine)
                                print(dose1)
                                print(dose2)
                                print(total)
                                cur.execute("INSERT INTO availabilities(pincode, date_of_availibility, type_of_vaccine, dose1, dose2, slots, hospital_name) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                                    pincode, Date_req, vaccine,  dose1, dose2, total, hospitalName))
                                con.commit()

            except TimeoutException:
                print("Loading took too much time!")

        time.sleep(60*5)
    except Exception as e:
        raise e


# commit the transcation
con.commit()

# close the cursor
cur.close()

# close the connection
con.close()
