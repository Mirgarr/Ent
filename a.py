from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def login(driverL, user_email, user_password, msgaenvoyer, objet, destinataire):
    driverL.get("https://ent.ecollege78.fr/auth/login#/")
    time.sleep(2)

    driverL.execute_script("document.cookie = 'cookie_accept=true';")

    username2 = driverL.find_element(By.NAME, "email")
    password2 = driverL.find_element(By.NAME, "password")

    username2.send_keys(user_email)
    password2.send_keys(user_password)
    password2.send_keys(Keys.RETURN)
    time.sleep(2)

    driverL.get(f"https://ent.ecollege78.fr/conversation/conversation#/inbox")
    time.sleep(2)
    try:
        wait = WebDriverWait(driver, 10)
        new_message_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cell-ellipsis")))
        new_message_button.click()
        time.sleep(1)

# DESTINATAIREEEE
        recipient_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@ng-model='search.text']")))
        recipient_input.send_keys(destinataire)
        time.sleep(1)

        recipient_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@ng-model='search.text']")))
        recipient_input.send_keys(destinataire)
        time.sleep(1)

        recipient_list = wait.until(EC.visibility_of_element_located((By.XPATH, "//drop-down[@list-id='dd-id-for-aria-2']")))
        options = recipient_list.find_elements(By.XPATH, ".//div[contains(@class, 'twelve flex-row align-center')]")


        for option in options:
            if destinataire.lower() in option.text.lower():
                option.click()
                break

        time.sleep(1)
# FIN DESTINATAIREEEEEE
        
        time.sleep(1)

        objet_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@ng-model='state.newItem.subject']")))
        objet_input.send_keys(objet)
        time.sleep(2)
        
        message_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@contenteditable='true']")))
        message_input.send_keys(msgaenvoyer)
        time.sleep(2)
    except Exception as e:
            print(f"erreur {e}")



def main():
    user_email = input("ent email \n")
    user_password = input("ent mdp \n")
    msgaenvoyer = input("quel message faut-il envoyer? \n")
    objet = input("quel est l'objet du message? \n")
    destinataire = input("à qui envoyer le message?")

    global driver
    driver = webdriver.Chrome()
    try:
        login(driver, user_email, user_password, msgaenvoyer, objet, destinataire)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
