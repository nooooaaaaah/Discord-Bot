import threading
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

<<<<<<< HEAD
def scraper(tableID, xpath, key):
    start_time = time.perf_counter()
=======
run_times_file = open("runtime.txt", 'a')

>>>>>>> da0b4a3fcf6ff03b75b571059a7307719fbde32d

def scraper(threads, tableID, xpath, key):
    start_time = time.perf_counter()

# options for how chrome will run
    chrome_options = Options()
    chrome_options.add_argument('--headless') #runs in background

# selenium stuff
    driver = webdriver.Chrome(executable_path=r'C:\Users\Nspie\Documents\GitHub\Discord-Bots\patch-notes-bot\chromedriver\chromedriver.exe', chrome_options= chrome_options) # Starts Chrome webdriver
    driver.get("https://newworldstatus.com/") #Has chrome go to website
    print(f"Looking for element\n")
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath))) # waits to see if table is loaded
    element_found_time = time.perf_counter() - start_time
    print(f"\nElement found in: {element_found_time:0.2f} seconds\n")

# scraping website
    source = BeautifulSoup(driver.page_source, 'html.parser') #ID for table with server wait times # get table
    driver.quit() # quit that selenium goodness
    table_element = source.find("table", {"id" : tableID}) #ID for table with server wait times # get table

    header_list =  table_element.find_all('th') # get headers from table
    tbody = table_element.find('tbody') # gets the body of the table
    tr_list = tbody.find_all('tr') # gets the rows of the table


    header_dic = {}
    header_dic[0] = 'Status'

# creates dictionany of tags from Table headers
    for i in range(len(header_list)):
        header_dic[i+1] = header_list[i].getText()
<<<<<<< HEAD
    multi_skinner(0, tr_list, key, header_dic)
=======
    multi_skinner(threads, tr_list, key, header_dic)

>>>>>>> da0b4a3fcf6ff03b75b571059a7307719fbde32d

    end_time = time.perf_counter()
    run_times_file.write(f"Run Time= {end_time - start_time:0.2f} seconds\nThreads= {threads}\n\n")
    run_times_file.close()
    print(f"\nYo shit ran in: {end_time - start_time:0.2f} seconds\n")
    #driver.quit() #quits all selenium stuff


def multi_skinner(numOfThreads, data, key, header_dic):
    data_array = np.array(data,dtype="object")
    split_data = np.array_split(data_array, 1) # splits data into list of size numOfThreads
    process_list = []
    return_dic = {}
    for i in range(numOfThreads):
        p = threading.Thread(target=parse_row_list, args=(split_data[i], header_dic, key, return_dic))
        p.start()
        process_list.append(p)
    for process in process_list:
        process.join()
    print(return_dic)


def parse_row_list(tr_list, header_dic, table_key, return_dic):
    table_dic = {}
    for k in range(len(tr_list)):
        current_TR = tr_list[k]
        current_TR_TD_list = current_TR.find_all('td')
        world_dic  = {}
        for j in range(len(current_TR_TD_list)):
            current_TD = current_TR_TD_list[j]
            world_dic[header_dic[j]] = current_TD.getText()
        return_dic[world_dic[table_key]] = world_dic
    print("asdas",return_dic)



if __name__ == "__main__":
    scraper(2, 'db76b9e516bd', "/html/body/div[2]/main/div[2]/div/table[2]/tbody/tr[1]/td[2]/strong", 'World')
