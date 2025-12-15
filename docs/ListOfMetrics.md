# List of Metrics

## Simple Metrics 

These are metrics that basically just fetch simple counts of things.
    
1. githubGraphqlSimpleCounts - Gets counts of things like commits, issues, pull requests, forks, etc. for a repo. A simple fetch operation
2. totalRepoLines - Counts of the total types of LoC (Lines of Code) present in a repository.
3. totalRepoCommentLines - Counts of the comment types of LoC (Lines of Code) present in a repository.
4. totalRepoBlankLines - Counts of the total blank lines of LoC (Lines of Code) present in a repository.
5. getCommitsByMonth - Gets the total number of commits per repo by month



## Periodic metrics

These are metrics that show data relative to a specific timeboxed period.

1. newContributorsofCommitsWeekly - Fetches a weekly timeseries metric of new contributors to this repo grouped by date.
2. newContributorsofCommitsMonthly - Fetchs a monthly timeseries metric of new contributors to this repo grouped by date.
3. issuesNewWeekly - Fetchs a weekly timeseries of new issues filed on this repo grouped by date.
4. issuesNewMonthly - Fetches a monthly timeseries of new issues filed on this repo grouped by date.

## Advanced Metrics:

These metrics measure something complicated. Like project labeling.

1. getNadiaBadgeURL - Fetches the nadia label for this metric from Augur and calculates a color for the badge too

## Org Metrics

These metrics are specific to an organization.

1. topCommitters - Fetches the top commiters for a GitHub organization. Stores their number of commits along with their email
2. githubGraphqlOrgSimple - Fetches some misc. info for orgs such as avatar_url, location, and email
3. orgFollowers - Gets the count of followers for this org
4. issueNewWeekly - Fetchs a weekly timeseries of new issues filed on this roup grouped by date
5. issueNewMonthly - Fetchs a monthly timeseries of new issues filed on this roup grouped by date

## Resource Metric

These metrics download a resource from the internet.

1. firstResponseForClosedPR - Fetches a scatterplot from augur and downloads it as an image.