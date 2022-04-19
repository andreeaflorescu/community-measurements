import metrics
from metrics import contributors

if __name__ == "__main__":
    year = metrics.get_quarter_of(2019)
    for q in year:
        print(q[0])
        # all_contribs = get_unique_contributors(since=q[1], until=q[2])
        # amzn_contribs = list(filter(lambda c: "amazon" in c, all_contribs))
        # print("all contributors:", len(all))
        # print("amazon contributors:", len(amzn_contribs))
        # print("-------------------------------------------------")
        all_commits = contributors.get_commits(q[1], q[2])
        amzn_commits = list(filter(lambda c: "amazon" in c.commit.author.email, all_commits))
        print(f"{len(all_commits)} {len(amzn_commits)}")