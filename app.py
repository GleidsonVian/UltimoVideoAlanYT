from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as ptg

#abre o chrome
navegador = opcoesSelenium.Chrome()
#abre o formulario do chrome
navegador.get('https://www.youtube.com/@LivesAlanzoka')

ptg.sleep(3)

videos = navegador.find_element(By.XPATH, '//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[2]/div[1]').click()

ptg.sleep(3)

video = navegador.find_elements(By.XPATH, '//*[@id="thumbnail"]/yt-image/img')[0].click()

