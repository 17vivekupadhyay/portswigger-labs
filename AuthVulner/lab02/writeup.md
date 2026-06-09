# Lab: 2FA Simple Bypass

I completed this lab by logging in with the provided credentials for `carlos`. After submitting the username and password, the application redirected to the 2FA verification step. However, I discovered that the account page could still be accessed directly by browsing to `/my-account` without completing 2FA. This showed that the application checked the password correctly but failed to enforce 2FA before granting access to protected pages.

source: https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-simple-bypass