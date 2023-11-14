---
layout: repo-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-{date_stamp}
permalink: /metrics/repos/{repo_owner}/{repo_name}

org: DSACMS
reportID: REPORT-{date_stamp}
date_stampThisWeek: {date_stamp}
date_stampLastWeek: {date_stamp}
# TODO: Update front matter fields & data above once we have data/graphs for reports.
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
        <td style="color: #45c527" >{commits_count_diff}</td>
        <td style="color: #45c527" >{commits_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>{latest_issues_count}</td>
        <td>{previous_issues_count}</td>
        <td style="color: #45c527" >{issues_count_diff}</td>
        <td style="color: #45c527" >{issues_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>{latest_open_issues_count}</td>
        <td>{previous_open_issues_count}</td>
        <td style="color: #d31c08" >{open_issues_count_diff}</td>
        <td style="color: #d31c08" >{open_issues_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>{latest_closed_issues_count}</td>
        <td>{previous_closed_issues_count}</td>
        <td style="color: #45c527" >{closed_issues_count_diff}</td>
        <td style="color: #45c527" >{closed_issues_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>{latest_open_pull_requests_count}</td>
        <td>{previous_open_pull_requests_count}</td>
        <td style="color: #d31c08" >{open_pull_requests_count_diff}</td>
        <td style="color: #d31c08" >{open_pull_requests_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>{latest_merged_pull_requests_count}</td>
        <td>{previous_merged_pull_requests_count}</td>
        <td style="color: #45c527" >{merged_pull_requests_count_diff}</td>
        <td style="color: #45c527" >{merged_pull_requests_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>{latest_closed_pull_requests_count}</td>
        <td>{previous_closed_pull_requests_count}</td>
        <td style="color: #45c527" >{closed_pull_requests_count_diff}</td>
        <td style="color: #45c527" >{closed_pull_requests_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>{latest_forks_count}</td>
        <td>{previous_forks_count}</td>
        <td style="color: #45c527" >{forks_count_diff}</td>
        <td style="color: #45c527" >{forks_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>{latest_stargazers_count}</td>
        <td>{previous_stargazers_count}</td>
        <td style="color: #45c527" >{stargazers_count_diff}</td>
        <td style="color: #45c527" >{stargazers_count_diff_percent}%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>{latest_watchers_count}</td>
        <td>{previous_watchers_count}</td>
        <td style="color: #45c527" >{watchers_count_diff}</td>
        <td style="color: #45c527" >{watchers_count_diff_percent}%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="row">
    <!--- Issues/PRs Status Breakdown Graph -->
    <figure>
      <embed type="image/svg+xml" src="_graphs/{repo_owner}/{repo_name}/issue_guage_{repo_name}_data.svg" />
    </figure>
    <!--- Contributor Activity Line Graph -->
    <figure>
      <embed type="image/svg+xml" src="_graphs/{repo_owner}/{repo_name}/commit_sparklines_{repo_name}_data.svg" />
    </figure>
  </div>
</div>