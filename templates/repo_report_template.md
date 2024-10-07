---
layout: repo-report
title: Open Source at CMS Metrics Report for {repo_name} | REPORT-{date_stamp}
permalink: /{repo_owner}/{repo_name}/

org: {repo_owner}
repo: {repo_name}
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
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {{% render "graph-section"  baseurl: site.baseurl, path: "/{repo_owner}/{repo_name}/issue_gauge_{repo_name}_data.svg", title: "Issues & PRs Status Breakdown" %}}
    <!--- Contributor Activity Line Graph -->
    {{% render "graph-section" baseurl: site.baseurl, path: "/{repo_owner}/{repo_name}/commit_sparklines_{repo_name}_data.svg", title: "Commits by Month" %}}
    <!--- First Response For Closed PR Scatterplot -->
    {{% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/{repo_owner}/{repo_name}/firstResponseForClosedPR_{repo_name}_data.png", title: "First Response For Closed PR" %}}
    <!--- Line Complexity Graphs -->
    {{% render "graph-section" baseurl: site.baseurl, path: "/{repo_owner}/{repo_name}/total_line_makeup_{repo_name}_data.svg", title: "Line Complexity" %}}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {{% assign optionsArray = '1 Month, 6 Month' | split: ',' %}}
      {{% assign graphsArray = '/{repo_owner}/{repo_name}/new_commit_contributors_by_day_over_last_month_{repo_name}_data.svg, /{repo_owner}/{repo_name}/new_commit_contributors_by_day_over_last_six_months_{repo_name}_data.svg' | split: ',' %}}
      {{% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}}
    <!-- Predominant Lanugages Graph -->
    {{% render "graph-section" baseurl: site.baseurl, path: "/{repo_owner}/{repo_name}/predominant_langs_{repo_name}_data.svg", title: "Predominant Languages" %}}
    <!-- Language Summary Chart -->
    {{% render "graph-section" baseurl: site.baseurl, path: "/{repo_owner}/{repo_name}/language_summary_{repo_name}_data.svg", title: "Language Summary" %}}
</div>