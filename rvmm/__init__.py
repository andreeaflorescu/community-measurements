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


rust_vmm_org = init_github().get_organization('rust-vmm')


def get_repos(org=rust_vmm_org):
    return org.get_repos()


def date_from(str_date):
    return datetime.datetime.strptime(str_date, "%Y-%m-%d")


def get_quarter_of(year):
    Q1 = (f"Q1_{year}", date_from(f"{year}-01-01"), date_from(f"{year}-03-31"))
    Q2 = (f"Q2_{year}", date_from(f"{year}-04-01"), date_from(f"{year}-06-30"))
    Q3 = (f"Q3_{year}", date_from(f"{year}-07-01"), date_from(f"{year}-09-20"))
    Q4 = (f"Q4_{year}", date_from(f"{year}-10-01"), date_from(f"{year}-12-31"))
    return [Q1, Q2, Q3, Q4]
