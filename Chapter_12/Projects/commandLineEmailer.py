#! python3
#! commandLineEmailer.py - send email from the commandline add email as first arguement and string as second.

#INCOMPLETE
import sys,time
import pyinputplus as pyip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = pyip.inputEmail('username :')
password = pyip.inputPassword('password :')
to = pyip.inputEmail('send to : ')
body = pyip.inputStr('Body : ')

browser = webdriver.Firefox()
browser.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1640183692&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26nlp%3d1%26RpsCsrfState%3de73bee06-a258-78e0-b8cc-ce4a67f4a15b&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
usernameElem = browser.find_element_by_id("i0116")
usernameElem.send_keys(username)
nextElem = browser.find_element_by_id("idSIButton9")
nextElem.click()

time.sleep(2)

passwordElem = browser.find_element_by_id("i0118")
passwordElem.send_keys(password)
nextElem = browser.find_element_by_id("idSIButton9")
nextElem.click()

time.sleep(2)

nextElem = browser.find_element_by_id("idSIButton9")
nextElem.click()

time.sleep(10)

messageElem = browser.find_element_by_id("id__6")
messageElem.click()

time.sleep(5)

toElem = browser.find_element_by_class_name("ms-BasePicker-input.pickerInput_cc9894a7")
toElem.send_keys(to)
time.sleep(1)
clickable = browser.find_element_by_id("sug-item0")
clickable.click()

time.sleep(1)

messageElem = browser.find_element_by_class_name("_16VySYOFix816mo3KsgOhw._1m89yrwkVHJAoAZ_JC8cw3._3VMDfFa1O01ntQj14k1rpD._2h8akM49fdZRv6KHq8jy75._3VQzn9yg47NIR2H1tIIeag")
messageElem.click()
messageElem.send_keys(body)

time.sleep(1)
nextElem = browser.find_element_by_class_name("ms-Button.ms-Button--primary.ms-Button--hasMenu.iconButton.root-242")
nextElem.click()

time.sleep(2)

clickable = browser.find_element_by_id("ok-1")
clickable.click()

