# Showing sql injection and credential issue. 
aws_access_key_id=324153454123423;
aws_secret_access_key=324153454123423;

from django.db import connection

def find_user(username):
    with connection.cursor() as cur:
        cur.execute(f"""select username from USERS where name = '%s'""" % username)
        output = cur.fetchone()
    return output