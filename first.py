#importing all the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import csv
#
print(time.time())

# creating an option variable and making it headless

opt=Options()
opt.add_argument('--headless')

#creating driver and action instance

driver=webdriver.Chrome(options=opt)
action= ActionChains(driver)

#opening a csv file

file=open("info.csv","w")
write_o=csv.writer(file, delimiter=',')

#opening a txt file
question_file=open("details.txt","w")

#starting a loop with alll the main code
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
            question_file.write("QUESTION N0. ")
            question_file.write(questionNumber+"\n")
            question=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div[1]/div[2]/p")
            question_file.write("\n")
            question_file.write(question.text+"\n")
            question_file.write("\n")
            temp = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/ul")
            for j in range(1,7):
                try:
                    list = temp.find_element(By.XPATH,".//li["+str(j)+"]")
                    question_file.write(list.text+"\n")
                except:
                    pass
            element2=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div[1]/div[2]/a[1]")
            action.click(element2)
            action.perform()
            answer=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div/div[1]/div[2]/div[3]/span[1]/span")
            question_file.write("Answer is  " )
            question_file.write(answer.text+"\n")
            question_file.write("\n")
            
        else:
            print("false")
    except NoSuchElementException:
        print("error")
        
file.close()
