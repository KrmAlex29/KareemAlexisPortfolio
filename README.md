Cisco Meraki Network Automation Tool

A Python automation tool built on the Cisco Meraki Dashboard API to monitor network health in real time, apply rule updates programmatically, and trigger instant email alerts — cutting manual monitoring out of the incident response loop.

Overview

Built to solve a real operational problem: manually checking device/network status across a distributed environment is slow and easy to miss. This tool polls the Meraki Dashboard API, evaluates device and network health against defined alert rules, and sends automated email notifications the moment something needs attention.

Features


Real-time monitoring of network and equipment status via the Meraki Dashboard API
Automated alert rule execution and modification
Instant email notifications on status changes, removing the need for manual checks
Secure API key handling via environment variables (python-dotenv) — no credentials committed to source control


Impact

Reduced incident response time by 90% by replacing manual status checks with automated, real-time notifications — enabling faster issue resolution across network infrastructure.

Tech Stack


Language: Python
IDE: PyCharm
API: Cisco Meraki Dashboard API
Config/Secrets: python-dotenv, .gitignore


How It Works


Authenticates to the Meraki Dashboard API using an API key loaded from environment variables
Polls network and device status on a defined interval
Evaluates results against configured alert rules
Triggers an email alert when a rule condition is met (e.g., device offline, health threshold breached)
