import datetime, os
from .metrics import SimpleMetric, GraphqlMetric
import json

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# Folder Names to send over our projects tracked data
PATH_TO_METRICS_DATA = "_data"
PATH_TO_METADATA = "_metadata"
DATESTAMP = datetime.datetime.now().date().isoformat()
TOKEN = os.getenv("GITHUB_TOKEN")

#The general procedure is to execute all metrics against all repos and orgs

# TODO: Create a read repos-to-include.txt
with open(os.path.join(PATH_TO_METADATA, "projects_tracked.json"), "r") as file:
    tracking_file = json.load(file)


ALL_ORGS = tracking_file["orgs"]  # Track orgs and all its repos e.g. DSACMS

ALL_REPOS = [] # Track specific repositories e.g. ['dsacms.github.io']

for _, repo_list in tracking_file["Open Source Projects"].items():
    ALL_REPOS.extend(repo_list)

SIMPLE_METRICS = []

githubGraphqlQuery = """
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


SIMPLE_METRICS.append(GraphqlMetric("githubGraphqlSimpleCounts",["repo","owner"],githubGraphqlQuery,
            {"commits_count": ["data","repository","defaultBranchRef","target","history","totalCount"],
            "issues_count": ["data","repository","issues","totalCount"],
            "open_issues_count": ["data","repository","openIssues","totalCount"],
            "closed_issues_count": ["data","repository","closedIssues","totalCount"],
            "pull_requests_count": ["data","repository","pullRequests","totalCount"],
            "open_pull_requests_count": ["data","repository","openPullRequests","totalCount"],
            "merged_pull_requests_count": ["data","repository","mergedPullRequests","totalCount"],
            "closed_pull_requests_count": ["data","repository","closedPullRequests","totalCount"],
            "forks_count": ["data","repository","forkCount"],
            "stargazers_count": ["data","repository","stargazerCount"],
            "watchers_count": ["data","repository","watchers","totalCount"]
            },token=TOKEN))