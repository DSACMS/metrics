"""
Definitions of specific metrics for metricsLib
"""
from metricsLib.metrics_data_structures import CustomMetric, parse_commits_by_month
from metricsLib.metrics_data_structures import GraphQLMetric, RangeMetric, SumMetric
from metricsLib.constants import TOKEN

# The general procedure is to execute all metrics against all repos and orgs

SIMPLE_METRICS = []

# Weekly, monthly metrics.
PERIODIC_METRICS = []

# Classification metrics
ADVANCED_METRICS = []

# Metrics gathered by org instead of by repo
ORG_METRICS = []

REPO_GITHUB_GRAPHQL_QUERY = """
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


github_graphql_simple_counts_metric_map = {
  "description": ["data", "repository", "description"],
  "commits_count": ["data", "repository", "defaultBranchRef", "target", "history", "totalCount"],
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
}
SIMPLE_METRICS.append(GraphQLMetric("githubGraphqlSimpleCounts", ["repo", "owner"],
 REPO_GITHUB_GRAPHQL_QUERY, github_graphql_simple_counts_metric_map, token=TOKEN))

PERIODIC_METRICS.append(RangeMetric("newContributorsofCommits", ["repo_id", "period", "begin_date", "end_date"],
  "https://ai.chaoss.io/api/unstable/repos/{repo_id}/pull-requests-merge-contributor-new?period={period}&begin_date={begin_date}&end_date={end_date}",
  {"new_commit_contributor": "count"}))

ORG_GITHUB_GRAPHQL_QUERY = """
query ($org_login: String!) {
  organization(login: $org_login) {
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
ORG_METRICS.append(GraphQLMetric("githubGraphqlOrgSimple", ["org_login"], ORG_GITHUB_GRAPHQL_QUERY,
                                 {"timestampCreatedAt": ["data", "organization", "createdAt"],
                                 "avatar_url": ["data", "organization", "avatarUrl"],
                                  "description": ["data", "organization", "description"],
                                  "email": ["data", "organization", "email"],
                                  "is_verified": ["data", "organization", "isVerified"],
                                  "location": ["data", "organization", "location"],
                                  "twitter_username": ["data", "organization", "twitterUsername"],
                                  "repo_count": ["data", "organization", "repositories", "totalCount"]
                                  }, token=TOKEN))

FOLLOWERS_ENDPOINT = "https://api.github.com/users/{org_login}/followers"
ORG_METRICS.append(
  SumMetric("orgFollowers", ["org_login"], FOLLOWERS_ENDPOINT, "followers_count",token=TOKEN)
)

COMMITS_ENDPOINT = "https://api.github.com/repos/{owner}/{repo}/commits"
SIMPLE_METRICS.append(CustomMetric("getCommitsByMonth", [
                      'owner', 'repo'], COMMITS_ENDPOINT, parse_commits_by_month, token=TOKEN))
