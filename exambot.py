from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import os

# Here You Enter Your Modules
listOfModules = ['', '', '', '', '', '']

# Set The Download Folder Here
download_folder = ''
options = webdriver.ChromeOptions()

class ExamBot:

	def __init__(self, username, password):
	
		self.username = username
		self.password = password

		profile = {'plugins.plugins_list': [{'enabled': False,
		'name': 'Chrome PDF Viewer'}],
		'download.default_directory': download_folder,
		'download.extensions_to_open': ''}

		for module in listOfModules:
			os.makedirs(module)

		options.add_experimental_option('prefs', profile)

		# For The Location Of The Chromedriver
		chromedriver = ''
		self.driver = webdriver.Chrome(chromedriver, options = options)


	def downloadPDF(self, xListOfLinks):

		driver = self.driver

		for y in xListOfLinks:
			url = y
			driver.get(url)
			r = requests.get(url, allow_redirects=True)


	def findPDF(self, moduleNumber):

		driver = self.driver

		for module in listOfModules:
			print(module)

			moduleSearchURL = 'https://www-ucc-ie.ucc.idm.oclc.org/cgi-bin/uncgi/examsearch?q=' + module
			driver.get(moduleSearchURL)
			time.sleep(2)

			listOfLinks=[]

			for a in driver.find_elements_by_xpath('.//a'):
				pdfLink = a.get_attribute('href')

				if '.pdf' in pdfLink: 
					if module in pdfLink:
						listOfLinks.append(pdfLink)
			
			print(listOfLinks)

			examScraper.downloadPDF(listOfLinks)


	def login(self):

		driver = self.driver
		driver.get('https://www-ucc-ie.ucc.idm.oclc.org/exampapers/')
		time.sleep(2)

		usernameElement = driver.find_element_by_id('username')
		usernameElement.clear()
		usernameElement.send_keys(self.username)

		passwordElement = driver.find_element_by_id('password')
		passwordElement.clear()
		passwordElement.send_keys(self.password)


		loginButton = driver.find_element_by_css_selector('.form-element.form-button')
		loginButton.click()


# Here You Have To Enter Your Student Email And Password
examScraper = ExamBot('', '')
examScraper.login()
examScraper.findPDF(listOfModules)



