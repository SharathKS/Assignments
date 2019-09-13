from PyCodeChallenge import ClosePGConnection, BuildReqRes, GetPGConnection
import json


class ParseJSON:

    def __init__(self):
        print("Parsing Initialised")

    def parse_json(self,arg):
        # 2.1: Change the github_api_url so that it queries with the input date
        """get the spark commits for the date"""

        get_pg_connection = GetPGConnection()
        close_pg_connection = ClosePGConnection()
        build_req_res = BuildReqRes()

        api_url = build_req_res.get_api_url(arg)
        resp = build_req_res.get_response(api_url)

        json_data = json.loads(resp.content)
        print(f"The response contains {len(json_data)} properties\n")
        connection = get_pg_connection.get_pg_connection()
        for key in json_data:
            cursor = connection.cursor()
            sha = str(key.get('sha'))
            url = str(key.get('url'))
            message = str(key.get('commit').get('message'))
            commit_date = str(key.get('commit').get('author').get('date'))
            login_name = str(key.get('author').get('login'))
            email = str(key.get('commit').get('author').get('email'))
            email_company_split = str(key.get('commit').get('author').get('email'))
            email_company = email_company_split.split('@')[1]
            postgresql_select_query = "SELECT login_name FROM f_spark_authors WHERE login_name=%s"
            cursor.execute(postgresql_select_query, (login_name,))
            connection.commit()
            count = cursor.rowcount
            if count == 0:
                spark_authors_query = """ INSERT INTO f_spark_authors (login_name,email,email_company,creation_date) VALUES (%s,%s,%s,NOW()) """
                cursor.execute(spark_authors_query, (login_name, email, email_company,))
                print("Data Inserted In f_spark_authors Table")
                postgres_check_query = """ Select id from f_spark_authors where login_name in (%s) """
                cursor.execute(postgres_check_query, (login_name,))
                rows = cursor.fetchone()[0]
                print(rows)
                postgresql_commit_check = "SELECT author_id,sha FROM f_spark_commits WHERE author_id=%s AND sha=%s"
                cursor.execute(postgresql_commit_check, (rows, sha,))
                connection.commit()
                count = cursor.rowcount
                if count == 0:
                    spark_commits_query = """ INSERT INTO f_spark_commits (sha,url,message,commit_date,author_id,creation_date) VALUES (%s,%s,%s,%s,%s,NOW()) """
                    cursor.execute(spark_commits_query, (sha, url, message, commit_date, rows,))
                    connection.commit()
        close_pg_connection.close_pg(connection)
        return True
