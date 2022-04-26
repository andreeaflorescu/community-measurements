import argparse
import datetime

import metrics
from metrics import contributors

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='community-metrics', description='Utility that prints community'
                                                                           'stats using Github')
    parser.add_argument(dest='action',
                        type=str,
                        choices=['commits', 'contributors'],
                        help='Action to take.')

    parser.add_argument('-g', '--github-org', action='store', type=str, dest='github_org', default='rust-vmm')
    parser.add_argument('-s', '--start-year', type=str, dest='start_year', default=datetime.date.today().year,
                        help='Year for which to get the stats. By default the current year is showed.')
    parser.add_argument('-e', '--end-year', type=str, dest='end_year', default=datetime.date.today().year,
                        help='Year until when to get the stats. This will by default be set to the current year.')
    parser.add_argument('-v', '--verbose', help="Print details about the commits/contributors.")

    args = parser.parse_args()
    org = args.github_org
    start_year = args.start_year
    end_year = args.end_year
    action = args.action

    if end_year < start_year:
        raise ValueError("The end year cannot be lower than the start year.")

    for year in range(start_year, end_year + 1):
        quarters = metrics.get_all_quarters_of(year)
        for q in quarters:
            if action == "contributors":
                all_contribs = contributors.get_unique_contributors(since=q[1], until=q[2])
                amzn_contribs = list(filter(lambda c: "amazon" in c, all_contribs))
                print(len(all_contribs), len(amzn_contribs), q[0])
                if args.verbose:
                    print("All Contributors:", all_contribs)
                    print("Amazon Contributors:", amzn_contribs)
            if action == "commits":
                all_commits = contributors.get_commits(q[1], q[2])
                amzn_commits = list(filter(lambda c: "amazon" in c.commit.author.email, all_commits))
                print(len(all_commits), len(amzn_commits), q[0])
                if args.verbose:
                    print("All Commits:", all_commits)
                    print("Amazon Commits:", amzn_commits)
