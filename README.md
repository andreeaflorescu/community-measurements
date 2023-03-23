# Community Measurements

This is a best effort to gathering information about the rust-vmm community
code contributors (gathering information about reviews, issues and other
important contributions is not trivial, and is thus not included for now).

For now the script supports 2 things: printing contributors & printing commits
per year. It is very much not extensible :( but maybe will evolve in the future.

## Running

```bash
# Before you start you need a GitHub access token.
# This will print the number of contributors in 2023 per quarter.
# The output is:
# <total number of contributors> <number of contributors from Amazon> <quarter>
GITHUB_ACCESS_TOKEN=${TOKEN} python3 __main__.py -s 2023 contributors
# This will print the number of commits in 2023 per quarter.
GITHUB_ACCESS_TOKEN=${TOKEN} python3 __main__.py -s 2023 commits
```