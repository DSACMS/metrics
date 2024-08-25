---
layout: repo-report
title: Open Source at CMS Metrics Report for mac-fc-github-actions-runner-aws | REPORT-2024-08-25
permalink: /Enterprise-CMCS/mac-fc-github-actions-runner-aws/

org: Enterprise-CMCS
repo: mac-fc-github-actions-runner-aws
reportID: REPORT-2024-08-25
date_stampThisWeek: 2024-08-25
date_stampLastWeek: 2024-08-25
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
        <td>340</td>
        <td>339</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.29%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>10</td>
        <td>10</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>10</td>
        <td>10</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>9</td>
        <td>8</td>
        <td style="" >1</td>
        <td style="" >12%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>145</td>
        <td>144</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.69%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>50</td>
        <td>50</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>11</td>
        <td>11</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>16</td>
        <td>15</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >6.5%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>9</td>
        <td>9</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/mac-fc-github-actions-runner-aws/issue_gauge_mac-fc-github-actions-runner-aws_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/mac-fc-github-actions-runner-aws/commit_sparklines_mac-fc-github-actions-runner-aws_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/mac-fc-github-actions-runner-aws/firstResponseForClosedPR_mac-fc-github-actions-runner-aws_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/mac-fc-github-actions-runner-aws/total_line_makeup_mac-fc-github-actions-runner-aws_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/mac-fc-github-actions-runner-aws/new_commit_contributors_by_day_over_last_month_mac-fc-github-actions-runner-aws_data.svg, /Enterprise-CMCS/mac-fc-github-actions-runner-aws/new_commit_contributors_by_day_over_last_six_months_mac-fc-github-actions-runner-aws_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>