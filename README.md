# cloud firestore ping Test

ping / measuring the time of Firebase Cloud Firestore data retrieval.

create projects with different cloud firestore locations / Regional / multi-Regional ( Data Center Locations ) to compare data retrieval time.

PS : idk if this the correct way to messure it but it is what it is :rage3:

## Requirements
- Python
- pip
- Firebase Admin (Python)
- 
## Instructions

```sh
sudo apt-get install python-pip
```
```sh
pip install firebase-admin
```
if you're having six incompatible issues :
```sh
pip install six==1.13.0
```

## On Firebase Project

- Project Settings - > Service Accounts -- > Select Python --- > Generate New Private Key ---- > Save the file in the same dir of the cfping.py file

EXAMPLE : 
downloads/us-centraltest/

                -cfping.py
                -privatekey.json
- duplicate and compare
