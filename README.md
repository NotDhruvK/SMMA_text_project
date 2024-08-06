# Twilio-based Funnel Project

This project is designed to run continuously on a server, interfacing with the Twilio API to send and receive text messages. It processes contacts from CSV files, categorizes responses, updates CSV files, and sends daily email summaries.

## High-Level Steps

### 1. Project Setup

1. **Set up a virtual environment**.
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```
2. **Install necessary libraries**.
   ```sh
   pip install -r requirements.txt
   ```

### 2. Configuration

#### Setting Up Environment Variables

This project uses environment variables to store sensitive information like API keys and email credentials. Follow these steps to set up your environment variables:

1. Create a copy of the `.env.example` file and name it `.env`:

   ```sh
   cp .env.example .env
   ```

2. Open the `.env` file and replace the placeholder values with your actual credentials:

   ```plaintext
   TWILIO_ACCOUNT_SID=your_actual_account_sid
   TWILIO_AUTH_TOKEN=your_actual_auth_token
   TWILIO_PHONE_NUMBER=your_actual_twilio_phone_number
   EMAIL_HOST=your_actual_email_host
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_actual_email@example.com
   EMAIL_HOST_PASSWORD=your_actual_email_password
   ```

3. Save the `.env` file.

## Server Setup

### 1. Setting up the server

The server is used to keep the flask and the celery apps running while the sent SMS are awaiting a reply.

1. Get an External IP and link it to your domain
2. Create two screens using the command:

```sh
screen -S "name_of_screen"
```

The first screen will house your Flask server.
The sceond screen will house your redis and celery server.

#### Setting up NGINX

1. Use this command first:

```sh
sudo nano /etc/nginx/sites-available/flask_app
```

2. Then add the following configuration to the file:

```sh
server {
    listen 80;
    server_name your_domain.com;  # Replace with your domain or IP address

    location / {
        proxy_pass http://127.0.0.1:5000;  # Flask app running on port 5000
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Save and Exit 3. Create a synbolic link to enable this site

```sh
sudo ln -s /etc/nginx/sites-available/flask_app /etc/nginx/sites-enabled
```

4. Remove the default configuration if it exists

```sh
sudo rm /etc/nginx/sites-enabled/default
```

5. Test the NGINX server

```sh
sudo nginx -t
```

6. Restart the server

```sh
sudo systemctl restart nginx
```

After following these steps, you should be able to access the website via the domain.

#### Pull all of your code onto the server

```sh
git clone "https://github.com/NotDhruvK/SMMA_text_project" text_project
```

This will clone all the files into the folder names text_project

## Running the Server

#### Start Redis server

```sh
redis-server
```

#### Check status of Redis Server

```sh
sudo lsof -i :6379
```

#### Ensuring Redis Server is working

```sh
sudo systemctl start redis
```

#### Run celery worker

```sh
celery -A celery_worker.celery worker --loglevel=info
```

#### Run the Flask server

1. **Change out of the Celery screen using the command:**
   `Ctrl + A + D`
2. **Change in the Flask screen using the command:**

```sh
screen -r {name_of_flask_screen}
```

3. **Running the flask application**

```sh
python3 twilio_client_receiving.py
```

4. **Exit out of Flask screen**
   `Ctrl + A + D`

## Scheduling CRON jobs

1. **Enter the command**

```sh
sudo crontab -e
```

2. **Add these three line to the end of the crontab**

```
*/15 * * * * /usr/bin/python3 /home/dhruvadam/textproject/src/every15mins.py >> /home/dhruvadam/textproject/cron.log 2>&1
0 14-19 * * * /usr/bin/python3 /home/dhruvadam/textproject/src/every_hour.py >> /home/dhruvadam/textproject/cron.log 2>&1
0 7 * * * /usr/bin/python3 /home/dhruvadam/textproject/src/every_day.py >> /home/dhruvadam/textproject/cron.log 2>&1
```

These will execute the files on the basis of the times provided in the first 5 characters on the statements.
