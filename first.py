from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import csv
time.time()

# creating an option variable and making it headless
opt=Options()
opt.add_argument('--headless')
#
driver=webdriver.Chrome(options=opt)
action= ActionChains(driver)
#
file=open("info.csv","w")
write_o=csv.writer(file, delimiter=',')
for i in [97934,97935,90837]:
    try:
        x="https://www.examtopics.com/discussions/amazon/view/"+str(i)+"-exam-aws-certified-solutions-architect-professional-sap-c02/"
        driver.get("https://www.examtopics.com/discussions/amazon/view/"+str(i)+"-exam-aws-certified-solutions-architect-professional-sap-c02/")
        element=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/div/h1")
        topic=element.text

        if "Exam AWS Certified Solutions Architect - Professional SAP-C02 topic".upper() in topic:
            questionNumber=topic.split()[-2]
            print("True",questionNumber)
            write_o.writerow([x,questionNumber])
            temp = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul")
            
            
            
            list = temp.find_element(By.XPATH,".//li[2]")
            print(list.text)

        else:
            print("false")
    except NoSuchElementException:
        print("error")
        
file.close()
