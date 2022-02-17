import datetime
import github
import rvmm


def unique(elems):
    unique_list = []
    for x in elems:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list


def flatten(list):
    return [item for sublist in list for item in sublist]


def get_unique_contributors(since=github.GithubObject.NotSet, until=github.GithubObject.NotSet):
    repos = rvmm.get_repos()
    all_contribs = list(map(lambda repo: get_repo_contributors(repo, since, until), repos))
    # all_contribs contains a list of lists, we need to flatten it first
    return unique(flatten(all_contribs))


def get_repo_contributors(repo: github.Repository, since=github.GithubObject.NotSet,
                          until=github.GithubObject.NotSet):
    commits = repo.get_commits(since=since, until=until)
    # Getting the contributors by looking at the author of a commit because in the meantime
    # contributors might have changed jobs, so the email showing up on their github profile
    # might be different than the one used for committing code.
    contribs = unique(list(map(lambda commit: commit.commit.author.email, commits)))
    for (i, contrib) in enumerate(contribs):
        if contrib == "andreea.florescu15@gmail.com":
            contribs[i] = "fandree@amazon.com"
    # filter away contributions from bot
    return list(filter(lambda e: not (is_bot(e)), contribs))


def is_bot(email):
    return "noreply" in email


def get_repo_commits(repo: github.Repository, since=github.GithubObject.NotSet,
                     until=github.GithubObject.NotSet):
    return list(filter(lambda commit: not (is_bot(commit.commit.author.email)),
                       repo.get_commits(since=since, until=until)))


def get_commits(since=github.GithubObject.NotSet,
                until=github.GithubObject.NotSet):
    repos = rvmm.get_repos()
    return flatten(list(map(lambda repo: get_repo_commits(repo, since, until), repos)))


def date_from(str_date):
    return datetime.datetime.strptime(str_date, "%Y-%m-%d")


def get_quarter_of(year):
    Q1 = (f"Q1_{year}", date_from(f"{year}-01-01"), date_from(f"{year}-03-31"))
    Q2 = (f"Q2_{year}", date_from(f"{year}-04-01"), date_from(f"{year}-06-30"))
    Q3 = (f"Q3_{year}", date_from(f"{year}-07-01"), date_from(f"{year}-09-20"))
    Q4 = (f"Q4_{year}", date_from(f"{year}-10-01"), date_from(f"{year}-12-31"))
    return [Q1, Q2, Q3, Q4]


if __name__ == "__main__":
    year = get_quarter_of(2019)
    for q in year:
        print(q[0])
        # all_contribs = get_unique_contributors(since=q[1], until=q[2])
        # amzn_contribs = list(filter(lambda c: "amazon" in c, all_contribs))
        # print("all contributors:", len(all))
        # print("amazon contributors:", len(amzn_contribs))
        # print("-------------------------------------------------")
        all_commits = get_commits(q[1], q[2])
        amzn_commits = list(filter(lambda c: "amazon" in c.commit.author.email, all_commits))
        print(f"{len(all_commits)} {len(amzn_commits)}")
