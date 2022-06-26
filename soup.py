import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36'
}

def GetScore(admission):
    session = requests.Session()
    soup = session.post(
        url='https://rajeduboard.rajasthan.gov.in/RESULT2022/SEV/Roll_Output.asp',
        # headers=headers,
        params={
            "roll_no": admission,
            "B1": "Submit"
        }
    )

    content = BeautifulSoup(soup.content, 'html.parser')

    # name picking
    name = content.table.select("tr")[4].select("td")[1].text[3:]

    # data_number_subject -  list of numbers
    sub_num = []
    for i in range(2,8):
        sub_num.append(content.table.select("table")[1].select("tr")[i].select("td")[5].text)

    # total number picking
    total_number = content.table.select("tr")[7].select("td")[-4].text.split(" ")[4]

    # creating field for inserting into csv file
    field = f"{name}, {admission}, , {sub_num[0]},  {sub_num[1]}, {sub_num[2]}, {sub_num[3]}, {sub_num[4]}, {sub_num[5]}, {total_number}"
    f.write(field)
    f.write('\n')


# creating csv file
filename = "cbse.csv"

# open csv file to write
f = open(filename, 'w')

# creat header in file
header = "NAME, ROLL NO, , HINDI, ENGLISH, SCIENCE, SOCIAL SCIENCE, MATHEMATICS, SANSKRIT, TOTAL NUMBER\n"
f.write(header)

for i in range(1978451, 1978522):
    if(i == 1978461 or i == 1978484 or i == 1978491 or i == 1978517):
        continue
    GetScore(i)

# closing csv file
f.close()