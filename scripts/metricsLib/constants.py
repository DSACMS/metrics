import datetime
import os
from .metrics import SimpleMetric, GraphqlMetric, RangeMetric
from .repos import Repository
from .orgs import GithubOrg
import json

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# Folder Names to send over our projects tracked data
PATH_TO_METRICS_DATA = "_data"
PATH_TO_METADATA = "_metadata"
DATESTAMP = datetime.datetime.now().date().isoformat()
TOKEN = os.getenv("GITHUB_TOKEN")

# The general procedure is to execute all metrics against all repos and orgs

# TODO: Create a read repos-to-include.txt
with open(os.path.join(PATH_TO_METADATA, "projects_tracked.json"), "r") as file:
    tracking_file = json.load(file)


ALL_ORGS = []
for org in tracking_file["orgs"]:
  # Track orgs and all its repos e.g. DSACMS
  ALL_ORGS.append(GithubOrg(org))

repo_urls = []  # Track specific repositories e.g. ['dsacms.github.io']

for _, repo_list in tracking_file["Open Source Projects"].items():
    repo_urls.extend(repo_list)

ALL_REPOS = []
# Create repo objects
for repo_url in repo_urls:
    repo_obj = Repository(repo_url)
    ALL_REPOS.append(repo_obj)


SIMPLE_METRICS = []

# Weekly, monthly metrics.
PERIODIC_METRICS = []

# Classification metrics
ADVANCED_METRICS = []

#Metrics gathered by org instead of by repo
ORG_METRICS = []

repoGithubGraphqlQuery = """
query ($repo: String!, $owner: String!) {
  repository(name: $repo, owner: $owner) {
    description,
    forkCount,
    forkingAllowed,
    stargazerCount,
    
    pullRequests(first: 1)
    {
      totalCount
    },
    mergedPullRequests: pullRequests(first: 1, states: MERGED)
    {
      totalCount
    },
    closedPullRequests: pullRequests(first: 1, states: CLOSED)
    {
      totalCount
    },
    openPullRequests: pullRequests(first: 1, states: OPEN)
    {
      totalCount
    },
    issues(first: 1)
    {
      totalCount
    },
    openIssues: issues(first: 1, states: OPEN)
    {
      totalCount
    },
    closedIssues: issues(first: 1, states: CLOSED)
    {
      totalCount
    },
    watchers(first: 1)
    {
      totalCount
    }
    defaultBranchRef
    {
      name,
      target
      {
        ... on Commit
        {
          history(first: 1)
          {
            totalCount
          }
          
        }
      }
    }
  }
}
"""


SIMPLE_METRICS.append(GraphqlMetric("githubGraphqlSimpleCounts", ["repo", "owner"], repoGithubGraphqlQuery,
                                    {"commits_count": ["data", "repository", "defaultBranchRef", "target", "history", "totalCount"],
                                     "issues_count": ["data", "repository", "issues", "totalCount"],
                                     "open_issues_count": ["data", "repository", "openIssues", "totalCount"],
                                     "closed_issues_count": ["data", "repository", "closedIssues", "totalCount"],
                                     "pull_requests_count": ["data", "repository", "pullRequests", "totalCount"],
                                     "open_pull_requests_count": ["data", "repository", "openPullRequests", "totalCount"],
                                     "merged_pull_requests_count": ["data", "repository", "mergedPullRequests", "totalCount"],
                                     "closed_pull_requests_count": ["data", "repository", "closedPullRequests", "totalCount"],
                                     "forks_count": ["data", "repository", "forkCount"],
                                     "stargazers_count": ["data", "repository", "stargazerCount"],
                                     "watchers_count": ["data", "repository", "watchers", "totalCount"]
                                     }, token=TOKEN))

newContributorsofCommits = "https://ai.chaoss.io/api/unstable/repos/{repo_id}/pull-requests-merge-contributor-new?period={period}&begin_date={begin_date}&end_date={end_date}"
PERIODIC_METRICS.append(RangeMetric("newContributorsofCommits", ["repo_id", "period", "begin_date", "end_date"], newContributorsofCommits,
                                    {"new_commit_contributor": "count"}))

orgGithubGraphqlQuery = """
query {
  organization(login: "DSACMS") {
    createdAt,
    avatarUrl,
    description,
    email,
    isVerified,
    location,
    twitterUsername
    repositories(first: 1)
    {
      totalCount
    }
  }
}
"""
ORG_METRICS.append(GraphqlMetric("githubGraphqlOrgSimple", ["org_login"], orgGithubGraphqlQuery,
                                {"timestampCreatedAt" : ["data", "organization", "createdAt"],
                                 "avatar_url" : ["data", "organization", "avatarUrl"],
                                 "description" : ["data", "organization", "description"],
                                 "email" : ["data", "organization", "email"],
                                 "is_verified" : ["data", "organization", "isVerified"],
                                 "location" : ["data", "organization", "location"],
                                 "twitter_username" : ["data", "organization", "twitterUsername"],
                                 "repo_count" : ["data", "organization", "repositories", "totalCount"]
                                }, token=TOKEN))