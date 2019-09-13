#!/usr/bin/env python
# coding: utf-8
import argparse
from PyCodeChallenge import ParseJSON


def get_spark_commits(date):
    # 2.1: Change the github_api_url so that it queries with the input date
    parse_json_obg = ParseJSON()
    status = parse_json_obg.parse_json(date)
    return "Executed Successfully" if status is True else "No records to update"


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Get the spark commits at a given date")
    parser.add_argument('-d',
                        '--date',
                        type=str,
                        help='The date to be executed in the YYYYMMDD format. (Eg. 20180120)',
                        required=True)

    args = parser.parse_args()
    get_spark_commits(args.date)