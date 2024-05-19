# Twilio-based Funnel Project

This project is designed to run continuously on a server, interfacing with the Twilio API to send and receive text messages. It processes contacts from CSV files, categorizes responses, updates CSV files, and sends daily email summaries.

## High-Level Steps

### 1. Project Setup
1. **Initialize a new Python project**.
2. **Set up a virtual environment**.
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```
3. **Install necessary libraries**.
    ```sh
    pip install twilio pandas schedule smtplib
    ```
4. **Create a requirements file**.
    ```sh
    pip freeze > requirements.txt
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

By following these steps, you will ensure that your environment variables are correctly set up and your sensitive information remains secure.

### 3. CSV Handling
1. **Write functions to read from and write to CSV files** (`src/csv_handler.py`).
    ```python
    import pandas as pd

    def read_csv(file_path):
        return pd.read_csv(file_path)

    def write_csv(dataframe, file_path):
        dataframe.to_csv(file_path, index=False)
    ```

### 4. Twilio Integration
1. **Set up the Twilio client** (`src/twilio_client.py`) to send and receive messages.
    ```python
    from twilio.rest import Client
    from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_message(to, body):
        message = client.messages.create(
            body=body,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        return message.sid
    ```

### 5. Message Handling Logic
1. **Define different text sequences and responses**.
2. **Implement a state machine to handle multiple back-and-forth sequences** (`src/message_handler.py`).

### 6. Categorization
1. **Create functions to categorize contacts based on responses**.
2. **Update the CSV files accordingly**.

### 7. Email Notification
1. **Implement logic to send daily email summaries** using an SMTP server (`src/email_notifier.py`).

### 8. Scheduler
1. **Set up a scheduler** (e.g., `schedule` or `APScheduler`) to run the script periodically (`src/scheduler.py`).

### 9. Logging and Error Handling
1. **Implement logging** for debugging and monitoring.
2. **Add error handling** to ensure robustness.

