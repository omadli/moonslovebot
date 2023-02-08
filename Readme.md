# Simple moonslove bot
Teegram bot: Love test according to the phases of the moon according to the date of birth

Based on the `aiogram` library
## Requirements
**Python 3.8** or higher

## Installation

### Create virtualenvironment:

If not exist virtualenv library

##### Windows: 
```shell
$ pip install virtualenv
```

##### Debian[Ubuntu, Kali, ...]:
```shell
$ sudo apt install python3 python3-venv
$ sudo apt install virtualenv python3-virtualenv
```

Create virtualenv:
##### Windows: 
```shell
$ python -m venv venv
```

##### Debian[Ubuntu, Kali, ...]:
```shell
$ python3 -m venv venv
```

Activate virtualenv:
##### Windows: 
```shell
$ .\venv\Scripts\activate
```

##### Debian[Ubuntu, Kali, ...]:
```shell
$ source ./venv/bin/activate
```

### Install requirements
To install the necessary python libraries:
```shell
$ pip install -r requirements.txt
```

### Environment variables
To configure the ENV values
#### Copy `.env.dist` file
```shell
$ cp .env.dist .env
```

#### Open and edit `.env` file:
With vscode
```shell
$ code .env
```

With nano:
```shell
$ nano .env
```
Or other...

!!! warning keep the bot token or other secret values private

### Run bot 
To run the bot
```shell
$ python bot.py
```

### Deploy to linux server

#### Copy `.service` file to `/etc/systemd/system` directory
```shell
$ sudo cp moonslove.service /etc/systemd/system/moonslove.service
```
!!! note Edit the service file depending on your server.

Start bot service
```shell
$ sudo systemctl daemon-reload
$ sudo systemctl enable moonslove
$ sudo systemctl start moonslove
```

### The end


&copy; [Murodillo](https://t.me/murodillo17)😎🫡

