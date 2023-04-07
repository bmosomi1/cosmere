import logging
import time
import requests
import mysql.connector


logging.basicConfig(filename="error.log", level=logging.DEBUG)


host = "localhost"
user = "root"
host_password = "root"
host_database = "rsms"


def send_stat(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sms_outgoingnew WHERE usage_status = 0 LIMIT 1000")
    messages = mycursor.fetchall()
    url = "https://sms.procom.co.ke/sms/v1/company/credit/usage"
    company_id = 1

    if len(messages) > 0:
        for message in messages:
            message_cost = calculate_message_cost(message[4])
            body = {
                'company_id': company_id,
                'credits': message_cost,
                'sender_name': message[2]
            }
            response = requests.post(url=url, data=body)
            logging.info(" " + response.text)

            mycursor.execute(f"UPDATE sms_outgoingnew SET usage_status = 1 WHERE id={message[0]}")
            mydb.commit()
    else:
        logging.info('No messages to process')


def calculate_message_cost(message):
    '''
    Method to calculate text message cost
    Sample Usage:
        message = "Hello Simon"
        message_cost = calculate_message_cost(message)
        print(message_cost)

        output:
            1
    '''
    message_length = len(message)
    cost = 0

    if message_length >= 160:
        cost += 1
        new_length = message_length - 160
        if new_length >= 144:
            cost += 1
            new_length = new_length - 144
            if new_length >= 151:
                while new_length >= 151:
                    new_length = new_length - 151
                    cost += 1
                else:
                    cost += 1
            else:
                cost += 1
        else:
            cost += 1
    else:
        cost = 1
    return cost


if __name__ == '__main__':
    while True:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=host_password,
            database=host_database
        )
        try:
            send_stat(mydb)
        except Exception as e:
            print(e)
            logging.debug(f"Send Usage Stat {e}")
        finally:
            mydb.close()
        time.sleep(1)