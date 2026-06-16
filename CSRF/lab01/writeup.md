# Lab: CSRF Vulnerability with No Defenses

I completed this lab by identifying that the email change functionality did not use any CSRF protections. The `/my-account/change-email` endpoint accepted a simple POST request containing only the new `email` value, with no CSRF token or additional verification. I created a malicious HTML page with a hidden form that submitted a POST request to the target email change endpoint. The form was placed inside a hidden iframe and automatically submitted using JavaScript, so the victim's browser would send the request while authenticated. This demonstrated a basic CSRF vulnerability because the application trusted the victim's session cookie without confirming that the request was intentionally made by the user.

Source: https://portswigger.net/web-security/csrf/lab-no-defenses
