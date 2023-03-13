
# 🚀 eXplorerXSS

This is a Python script that demonstrates a cross-site scripting (XSS) attack on a login page. The script uses the 🐍 requests and 🍲 BeautifulSoup libraries to send HTTP requests to the target website, extract the CSRF token, inject XSS payloads into the login form fields, and collect sensitive information if the attack is successful.

## 🏁 Getting Started

To use this script, you need to have Python 3 and the requests and BeautifulSoup libraries installed on your machine. You can install these libraries using pip:

`pip install requests 📦`
`pip install beautifulsoup4 🎨`

## 🎬 Usage

To use this script, you need to modify the following variables:

-   `url`: The URL of the target website's login page.
    
-   `payloads`: A list of XSS payloads to inject into the login form fields.
    
-   `data`: A dictionary of the login form data, including the CSRF token.
    

After modifying these variables, you can run the script using the following command:

Copy code

`python explorerxss.py 🚀` 

The script will send a GET request to the login page to extract the CSRF token, inject the XSS payloads into the login form fields, and send a POST request with the form data. If the attack is successful, the script will print the collected sensitive information, including cookies 🍪, user agent 🕵️‍♂️, and OS version 🖥️.

## 🚫 Limitations

This script is for educational purposes only and should not be used for malicious purposes. The script only demonstrates a basic XSS attack on a simple login page and may not work on more complex websites with better security measures. In addition, the script assumes that the target website does not have any protection against CSRF attacks.

## 📚 References

-   [requests library documentation](https://docs.python-requests.org/en/latest/)
    
-   [BeautifulSoup library documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    
-   [Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)
