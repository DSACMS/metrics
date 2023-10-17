## List of Metrics

# Github metrics

Simple metrics:
    1. githubGraphqlSimpleCounts - Gets counts of things like commits, issues, pull requests, forks, etc. for a repo. A simple fetch operation

# Augur metrics

Weekly Diff endpoints:
    1. https://oss-augur.readthedocs.io/en/dev/rest-api/api.html#operation/New%20Contributors%20of%20Commits%20(Repo)
    2. https://oss-augur.readthedocs.io/en/dev/rest-api/api.html#operation/Issues%20New%20(Repo)
    3. pull_request_average_commit_counts
    4. pull_request_average_time_to_responses_and_close 
    5. https://oss-augur.readthedocs.io/en/dev/rest-api/api.html#operation/New%20Contributors%20(Repo%20Group)
    6. https://oss-augur.readthedocs.io/en/dev/rest-api/api.html#operation/New%20Contributor%20Counts%20Bar%20Chart
    7. Code Changes from week to week - https://oss-augur.readthedocs.io/en/main/rest-api/api.html#operation/Code%20Changes%20(Repo)

Activity Metrics:
    1. Top Committers (Both Repo and Repo group) - https://oss-augur.readthedocs.io/en/main/rest-api/api.html#operation/Top%20Committers%20(Repo%20Group)

    2. Predominant languages and License info

    3. File Complexity

    2. New Contributors of Commits - Only if there are a number of new contributers - https://oss-augur.readthedocs.io/en/main/rest-api/api.html#operation/New%20Contributors%20of%20Commits%20(Repo%20Group)

    3. Contributors - Only if stars > 5 : https://oss-augur.readthedocs.io/en/main/rest-api/api.html#operation/Contributors%20(Repo)

    4. Average Issue Resolution Time - Only if stars > 5

    5. Pull Request acceptance rate - Only if stars > 5

    6. Mean Response Times for Closed Pull Requests - Stars > 5


:. Note: It Seems that there is no diff endpoint for pull requests created in Augur at the moment.

We should probably calculate highlights on our end since it should be specialized to our use case.

Project Category Metrics: https://project-types.github.io/

    This is a single metric that categorizes each repo into a type based on user growth and contributor growth. Time period should be around a
    year. Maybe six months.

    Measure of user growth - This should be done through page views and star count (need push access): https://docs.github.com/en/rest/metrics/traffic?apiVersion=2022-11-28

    Measure of contributor growth - https://oss-augur.readthedocs.io/en/main/rest-api/api.html#operation/New%20Contributors%20(Repo)

    The final badge will be calculated based on thresholding these measures into quadrants.

    High contributor growth is defined as > ~5 over six months?

    High user growth is defined as > ~5 over six months?
