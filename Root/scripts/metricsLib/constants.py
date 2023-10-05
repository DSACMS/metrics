import datetime, os
from metrics import SimpleMetric, GraphqlMetric

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# Folder Names to send over our projects tracked data
PATH_TO_METRICS_DATA = "_data"
PATH_TO_METADATA = "_metadata"
DATESTAMP = datetime.datetime.now().date().isoformat()
TOKEN = os.getenv("GITHUB_TOKEN")

#The general procedure is to execute all metrics against all repos and orgs

# TODO: Create a read repos-to-include.txt
ALL_ORGS = []  # Track orgs and all its repos e.g. DSACMS
ALL_REPOS = []  # Track specific repositories e.g. ['dsacms.github.io']

ALL_METRICS = []

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
        open_issues: issues(first: 1, states: OPEN)
        {
          totalCount
        },
        closed_issues: issues(first: 1, states: CLOSED)
        {
          totalCount
        },
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


ALL_METRICS.append(GraphqlMetric("githubGraphqlSimpleCounts",githubGraphqlQuery,
            {"datetime": DATESTAMP,
            "commits_count": ["data","repository","defaultBranchRef","target","history","totalCount"],
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