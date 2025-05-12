# SentinelSecure Brute Force Demo Setup Guide

This guide will help you set up a safe, legal environment to test the brute force tool against a deliberately vulnerable Flask application.

## Prerequisites:

    Python 3.6+

    Git

    Basic command line knowledge

## Setup Instructions
1. Clone the Repository
```bash
git clone https://github.com/0x5chltz/SentinelSecure.git
cd SentinelSecure/bruteforce
```
2. Set Up the Vulnerable Flask App
Install Flask requirements:
```bash
cd flask-app
pip install -r requirements.txt
```
Start the vulnerable server:
```bash
python app.py
```
The server will run at http://127.0.0.1:5000

3. Prepare the Brute Force Tool
Install dependencies:
```bash
pip install requests beautifulsoup4
```
Download credential files:
```bash
wget https://xcode.co.id/user.txt
wget https://xcode.co.id/wordlist.txt
```
4. Run the Brute Force Attack
```bash
python brute.py
```

## Legal and Safe Testing Environment

This setup creates a completely local and controlled environment where:

    You own both the attacking tool and the target server

    No real systems are being attacked

    All activity stays on your local machine

## Learning Objectives

By running this demo, you can:

    Understand how brute force attacks work

    See how web applications process login attempts

    Learn what makes authentication systems vulnerable

    Develop defenses against such attacks

## Security Recommendations

If you were protecting against this attack:

    Implement account lockouts after 3-5 failed attempts

    Add rate limiting to login endpoints

    Use CAPTCHAs after failed attempts

    Enforce strong password policies

    Implement multi-factor authentication
