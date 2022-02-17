import os
from github import Github

ACCESS_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']
github = Github(ACCESS_TOKEN)
rust_vmm_org = github.get_organization('rust-vmm')


def get_repos(org=rust_vmm_org):
    return org.get_repos()
