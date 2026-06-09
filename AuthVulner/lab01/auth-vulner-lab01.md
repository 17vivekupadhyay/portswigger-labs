# Lab: Username Enumeration via Different Responses

I completed this lab using Burp Suite Community Edition and the Intruder tool. After sending the login request to Intruder, I tested the provided username list and noticed that one response had a different length than the others: `2896` instead of around `2984`. This difference revealed that the valid username was `arkansas`. I then kept the username fixed and brute-forced the password using the provided password list. The successful attempt returned a `302` redirect, revealing the valid password as `mathew`, which allowed me to log in and complete the lab.

Source: https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses