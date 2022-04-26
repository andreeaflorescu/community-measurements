import os
import datetime
from github import Github


def init_github():
    try:
        ACCESS_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']
    except KeyError:
        print("The `GITHUB_ACCESS_TOKEN` environment variable is missing."
              "To get a GitHub Access Token you can use the following runbook:")
        print("https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token")
        raise

    github = Github(ACCESS_TOKEN)
    return github


def get_org(name='rust-vmm'):
    return init_github().get_organization(name)


def get_repos(org='rust-vmm'):
    return get_org(org).get_repos()


def date_from(str_date):
    return datetime.datetime.strptime(str_date, "%Y-%m-%d")


def get_all_quarters_of(year):
    return [q1(year), q2(year), q3(year), q4(year)]


def q1(year):
    return f"Q1_{year}", date_from(f"{year}-01-01"), date_from(f"{year}-03-31")


def q2(year):
    return f"Q2_{year}", date_from(f"{year}-04-01"), date_from(f"{year}-06-30")


def q3(year):
    return f"Q3_{year}", date_from(f"{year}-07-01"), date_from(f"{year}-09-20")


def q4(year):
    return f"Q4_{year}", date_from(f"{year}-10-01"), date_from(f"{year}-12-31")


def quarter_year_as_date_interval(quarter, year):
    """
    Get the quarter of the year.
    :param quarter: One of Q1, Q2, Q3, Q4.
    :param year: The year of the date.
    :return: Returns a tuple representing the quarter start and end date.
    """
    if quarter == "Q1":
        return q1(year)
    elif quarter == "Q2":
        return q2(year)
    elif quarter == "Q3":
        return q3(year)
    elif quarter == "Q4":
        return q4(year)
    else:
        raise ValueError("Invalid quarter specified. Valid options are: Q1, Q2, Q3, and Q4")
