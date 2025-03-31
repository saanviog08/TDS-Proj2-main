import requests
import zipfile
import io
import pandas as pd

url = "https://flask-hello-world-silk-psi-36.vercel.app/"
question = "\n    Sports Analytics for CricketPro\n    CricketPro Insights is a leading sports analytics firm specializing in providing in-depth statistical analysis and insights for cricket teams, coaches, and enthusiasts. Leveraging data from prominent sources like ESPN Cricinfo, CricketPro offers actionable intelligence that helps teams optimize player performance, strategize game plans, and engage with fans through detailed statistics and visualizations.\n\n    In the competitive world of cricket, understanding player performance metrics is crucial for team selection, game strategy, and player development. However, manually extracting and analyzing batting statistics from extensive datasets spread across multiple web pages is time-consuming and prone to errors. To maintain their edge and deliver timely insights, CricketPro needs an efficient, automated solution to aggregate and analyze player performance data from ESPN Cricinfo's ODI (One Day International) batting statistics.\n\n    CricketPro Insights has identified the need to automate the extraction and analysis of ODI batting statistics from ESPN Cricinfo to streamline their data processing workflow. The statistics are available on a paginated website, with each page containing a subset of player data. By automating this process, CricketPro aims to provide up-to-date insights on player performances, such as the number of duck outs (i.e. a score of zero), which are pivotal for team assessments and strategic planning.\n\n    As part of this initiative, you are tasked with developing a solution that allows CricketPro analysts to:\n\n    Navigate Paginated Data: Access specific pages of the ODI batting statistics based on varying requirements.\n    Extract Relevant Data: Use Google Sheets' IMPORTHTML function to pull tabular data from ESPN Cricinfo.\n    Analyze Performance Metrics: Count the number of ducks (where the player was out for 0 runs) each player has, aiding in performance evaluations.\n    Your Task\n    ESPN Cricinfo has ODI batting stats for each batsman. The result is paginated across multiple pages. Count the number of ducks in page number 22.\n\n    Understanding the Data Source: ESPN Cricinfo's ODI batting statistics are spread across multiple pages, each containing a table of player data. Go to page number 22.\n    Setting Up Google Sheets: Utilize Google Sheets' IMPORTHTML function to import table data from the URL for page number 22.\n    Data Extraction and Analysis: Pull the relevant table from the assigned page into Google Sheets. Locate the column that represents the number of ducks for each player. (It is titled \"0\".) Sum the values in the \"0\" column to determine the total number of ducks on that page.\n    Impact\n    By automating the extraction and analysis of cricket batting statistics, CricketPro Insights can:\n\n    Enhance Analytical Efficiency: Reduce the time and effort required to manually gather and process player performance data.\n    Provide Timely Insights: Deliver up-to-date statistical analyses that aid teams and coaches in making informed decisions.\n    Scalability: Easily handle large volumes of data across multiple pages, ensuring comprehensive coverage of player performances.\n    Data-Driven Strategies: Enable the development of data-driven strategies for player selection, training focus areas, and game planning.\n    Client Satisfaction: Improve service offerings by providing accurate and insightful analytics that meet the specific needs of clients in the cricketing world.\n    What is the total number of ducks across players on page number 22 of ESPN Cricinfo's ODI batting stats?\n    "
question = "Let's make sure you know how to use npx and prettier.\n    Download . In the directory where you downloaded it, make sure it is called README.md, and run npx -y prettier@3.4.2 README.md | sha256sum.\n    What is the output of the command?"

files = {'file': open("tests/README.md", 'rb')}
data = {'question': question}
response = requests.post(url,
    files=files,
    data=data)
print(response.text)
