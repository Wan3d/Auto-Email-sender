## Description
This Python script is a simple way to bother your friend. It will send to your friend random information about one specific country such as the timezone and the meaning of a generated word.
Your friend is going to be confused when he gets an email message with the information the script has generated.
You can schedule this script to send this information whenever you want, from the email account you choose and select your email receiver.

## Requisites
- Google password for applications
- Selenium library
» pip install selenium
- BeautifulSoup library
» pip install beautifulsoup4
- WebDriver library
» pip install webdriver_manager
- Virtual Environment (Optional)

## Get Google password for applications
First of all we have to go to Security settings and make sure two-steps verification is already working. Then, go to the next link: https://myaccount.google.com/apppasswords.
We have to give a name for our app and create a password. Make sure you copy the password, will not appear anymore.

## Virtual Environment
The relevance of having a venv in this kind of projects is that it secures a little bit more your information such as your email and password. That is the reason why I choose to use it, I have my credentials in a file
stored in my venv and no one can acces but me. You can use it as I do, or you just can put your information on the credentials.py file. It is really not a big deal, it is just a basic script.

## How it works?
This code basically extracts specific information from the HTML of a webpage. First, it navigates to a site that generates a new random word each time you refresh. 
Then, it locates the element containing the word and retrieves the text that the script stores in a variable.
Next, searchs the same word in the RAE webpage and gets the element containing the first definition.
It does the same thing for country and timezone, it only will change the element from it is getting the information.
There is a function that works for sending the emails, this function will receive as parameter the information captured and send it as subject to the email receiver.

## How to use it?
This is a specific script—it can be modified or used as a base, but for this particular use case, you only need three basic things (after completing the requirements):
- Your email sender
- The password for that email
- The email recipient

Make sure to open the credentials.py file and replace the placeholder values with your own information.

If you're using a virtual environment, store your credentials as variables in a .env file, and access them using os.getenv(<variable>). That’s how I did it, and you’ll find an example in the credentials file.

If you’re not using a virtual environment, just replace the os.getenv(<variable>) lines with your actual data directly in the file.
For example, if my email is joan@gmail.com and my password is 123, I would write:

gmailUser = "joan@gmail.com"

gmailPassword = "123"

## License

MIT License – do whatever you want with it, just don't blame me if your friend blocks you 😄

