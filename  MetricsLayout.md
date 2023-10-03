# Updating Metrics
This page will update the markdown site through github actions that hit various endpoints to gather metrics for each repo and repo group. We shouldn't store metrics data unless it is something fairly simple that can be derived statically on the markdown page. 

The update process will look like this:
    1. Erase old metric data that the markdown was pulling from (Graphs, Markdown for each repo and repo group)
    2. Query all metrics for all repos and repo groups
    3. Store the data in a generated markdown table for the home page, Graphs and Markdown for the other pages

Relevant: https://www.markdownguide.org/extended-syntax/


# Home Page

Lists the repos along with surface metrics. The Contributor and commit sparklines will be shown next to the repo icon with the contributor sparklines hidden if it is a small repo.

# Weekly Page

Shows various weekly statistics by group and then by repo when the user scrolls down the page. See below for specifics.

The monthly page can show the same metrics over a month. 

# Good Augur endpoints to use in the future for metrics and reports.

Weekly Diff endpoints:
    1. https://oss-augur.readthedocs.io/en/dev/rest-api/api.html#operation/New%20Contributors%20of%20Commits%20(Repo)
    2. https://oss-augur.readthedocs.io/en/dev/rest-api/api.html#operation/Issues%20New%20(Repo)
    3. pull_request_average_commit_counts
    4. pull_request_average_time_to_responses_and_close 
    5. https://oss-augur.readthedocs.io/en/dev/rest-api/api.html#operation/New%20Contributors%20(Repo%20Group)
    6. https://oss-augur.readthedocs.io/en/dev/rest-api/api.html#operation/New%20Contributor%20Counts%20Bar%20Chart

:. Note: It Seems that there is no diff endpoint for pull requests created in Augur at the moment.

We should probably calculate highlights on our end since it should be specialized to our use case.
