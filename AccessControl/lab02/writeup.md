# Lab: Unprotected Admin Functionality with Unpredictable URL

I completed this lab by inspecting the homepage response and looking for any leaked admin functionality. Although the admin panel used an unpredictable `/admin-...` path, the location was exposed inside the page's JavaScript. I parsed the HTML response with BeautifulSoup, extracted the hidden admin path using a regex, and preserved the session cookie from the initial request. Once I had the admin URL, I sent a request to the delete endpoint with `username=carlos`. This demonstrated that hiding an admin URL is not proper access control, because the sensitive functionality was still accessible without authorization.

Source: https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url
