---
layout: org-report
title: Open Source at CMS Metrics Report for {repo_owner} | REPORT-{date_stamp}
permalink: /{repo_owner}/

org: {repo_owner}
reportID: REPORT-{date_stamp}
date_stampThisWeek: {date_stamp}
date_stampLastWeek: {date_stamp}
---
<div class="summary-table">
  <table class="usa-table usa-table--borderless">
    <h2> Summary Table </h2>
    <thead>
      <tr>
        <th scope="col">Metric</th>
        <th scope="col">Latest</th>
        <th scope="col">Previous</th>
        <th scope="col">Diff</th>
        <th scope="col">% Diff</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th scope="row">Commits</th>
        <td>{latest_commits_count}</td>
        <td>{previous_commits_count}</td>
        <td style="{commits_count_diff_color}" >{commits_count_diff}</td>
        <td style="{commits_count_diff_percent_color}" >{commits_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>{latest_issues_count}</td>
        <td>{previous_issues_count}</td>
        <td style="{issues_count_diff_color}" >{issues_count_diff}</td>
        <td style="{issues_count_diff_percent_color}" >{issues_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>{latest_open_issues_count}</td>
        <td>{previous_open_issues_count}</td>
        <td style="{open_issues_count_diff_color}" >{open_issues_count_diff}</td>
        <td style="{open_issues_count_diff_percent_color}" >{open_issues_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>{latest_closed_issues_count}</td>
        <td>{previous_closed_issues_count}</td>
        <td style="{closed_issues_count_diff_color}" >{closed_issues_count_diff}</td>
        <td style="{closed_issues_count_diff_percent_color}" >{closed_issues_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>{latest_open_pull_requests_count}</td>
        <td>{previous_open_pull_requests_count}</td>
        <td style="{open_pull_requests_count_diff_color}" >{open_pull_requests_count_diff}</td>
        <td style="{open_pull_requests_count_diff_percent_color}" >{open_pull_requests_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>{latest_merged_pull_requests_count}</td>
        <td>{previous_merged_pull_requests_count}</td>
        <td style="{merged_pull_requests_count_diff_color}" >{merged_pull_requests_count_diff}</td>
        <td style="{merged_pull_requests_count_diff_percent_color}" >{merged_pull_requests_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>{latest_closed_pull_requests_count}</td>
        <td>{previous_closed_pull_requests_count}</td>
        <td style="{closed_pull_requests_count_diff_color}" >{closed_pull_requests_count_diff}</td>
        <td style="{closed_pull_requests_count_diff_percent_color}" >{closed_pull_requests_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>{latest_forks_count}</td>
        <td>{previous_forks_count}</td>
        <td style="{forks_count_diff_color}" >{forks_count_diff}</td>
        <td style="{forks_count_diff_percent_color}" >{forks_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>{latest_stargazers_count}</td>
        <td>{previous_stargazers_count}</td>
        <td style="{stargazers_count_diff_color}" >{stargazers_count_diff}</td>
        <td style="{stargazers_count_diff_percent_color}" >{stargazers_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>{latest_watchers_count}</td>
        <td>{previous_watchers_count}</td>
        <td style="{watchers_count_diff_color}" >{watchers_count_diff}</td>
        <td style="{watchers_count_diff_percent_color}" >{watchers_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>{latest_followers_count}</td>
        <td>{previous_followers_count}</td>
        <td style="{followers_count_diff_color}" >{followers_count_diff}</td>
        <td style="{followers_count_diff_percent_color}" >{followers_count_diff_percent}%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <h2 class="graph-section-title">Activity Graphs</h2>
  <div class="all-graphs">
    {% Issues/PRs Status Breakdown Graph %}
    {{% render "graph-section" baseurl: site.baseurl, path: "/{repo_owner}/{repo_owner}_issue_gauge.svg", title: "Issues & PRs Status Breakdown", modal_description: "This graph provides an overview of the statuses of issues and pull requests in the organization. It categorizes them into open issues, open pull requests, and closed and merged pull requests, helping track progress and worklad distribution." %}}
    {% New Issues over Last 6 Months %}
    {{% render "graph-section" baseurl: site.baseurl, path: "/{repo_owner}/{repo_owner}_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months", modal_description: "These graphs illustrate the number of new contributors joining the organization over time. They show data for six-month intervals, providing insights into contributor growth and onboarding rates." %}}
    {% Top Committers Bar Graph %}
    {{% render "graph-section" baseurl: site.baseurl, path: "/{repo_owner}/{repo_owner}_top_committers.svg", title: "Top Committers", modal_description: "This graph highlights the top contributors with the organizations, ranked by the number of commits they have made. It provides insights into the most active members driving developement efforts and their relative contributions to the organization's repositories." %}}
    {% Libyear Timeline Graph %}
    {{% render "graph-section" baseurl: site.baseurl, path: "/{repo_owner}/{repo_owner}_libyear_timeline.svg", title: "Dependency Libyears", modal_description: "This timeline graph visualizes the age of dependencies in the organization in terms of 'libyears.' It highlights how up-to-date the dependencies are and the potential risk of outdated libraries." %}}
  </div>
</div>