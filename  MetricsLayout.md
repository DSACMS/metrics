# Updating Metrics
This page will update the markdown site through github actions that hit various endpoints to gather metrics for each repo and repo group. We shouldn't store metrics data unless it is something fairly simple that can be derived statically on the markdown page. 

The update process will look like this:
    1. Erase old metric data that the markdown was pulling from (Graphs, Markdown for each repo and repo group)
    2. Query all metrics for all repos and repo groups
    3. Store the data in a generated markdown table for the home page, Graphs and Markdown for the other pages

Relevant: https://www.markdownguide.org/extended-syntax/


# Home Page

Lists the repos along with surface metrics. The Contributor and commit sparklines will be shown next to the repo icon with the contributor sparklines hidden if it is a small repo.

Simple endpoints:
    Github graphql !!
    Augur forks and fork count
    Annual Commit Count Ranked Repos (Has net commits in response)
    Issues Active

# Weekly Page

Shows various weekly statistics by group and then by repo when the user scrolls down the page. See below for specifics.

The monthly page can show the same metrics over a month. 

# Conditional Metrics

Some metrics should only be displayed or fetched on a conditional basis.
For example if a repo has more than 5 stars on github then they are 
considered to be actually using github for collaboration and then things
like pull requests, issues, new contributors can have more advanced useful
metrics.