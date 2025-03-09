from selenium import webdriver
from selenium.webdriver.common.by import By
import sys

def test_scores_service(app_url):
    driver = webdriver.Chrome()
    driver.get(app_url)
    score_element = driver.find_element(By.ID, "score")
    score = score_element.text
    driver.quit()
    try:
        score_num = int(score)
        return 1 <= score_num <= 1000
    except:
        return False

def main_function():
    result = test_scores_service("http://localhost:8777")
    sys.exit(0 if result else -1)

if __name__ == "__main__":
    main_function()