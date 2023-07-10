# Web-Scraping-Alert-System
This repository contains a Python script for web scraping local news updates and implementing an automated alert system using Twilio. The script periodically checks a local news website for any incidents or emergencies in the specified area and sends text messages using Twilio API to notify the user. 

Features:
- Web scraping using BeautifulSoup library to extract relevant information from HTML content.
- Integration with Twilio API for sending text messages with the extracted news title.
- Implementation of the Windows Task Scheduler to automate script execution every 10 minutes.
- Console output of the scraped news information for debugging and monitoring purposes.

Dependencies:
- Python 3.x
- requests library
- BeautifulSoup library
- Twilio library

Usage:
1. Install the required dependencies mentioned above.
2. Clone or download this repository to your local machine.
3. Update the URL in the script to the desired local news website.
4. Replace the Twilio account SID, authentication token, and phone numbers in the script with your own.
5. Run the script using a Python interpreter.
6. Confirm successful execution by checking the console output and receiving the text messages.

Contributions:
Contributions to improve the functionality, efficiency, or add new features are welcome. Please fork the repository, make your changes, and submit a pull request.





