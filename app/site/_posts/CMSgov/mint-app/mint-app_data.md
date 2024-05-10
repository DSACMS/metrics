---
layout: repo-report
title: Open Source at CMS Metrics Report for mint-app | REPORT-2024-05-06
permalink: /CMSgov/mint-app/

org: CMSgov
repo: mint-app
reportID: REPORT-2024-05-06
date_stampThisWeek: 2024-05-06
date_stampLastWeek: 2024-05-06
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
        <td>921</td>
        <td>881</td>
        <td style="color: #45c527" >40</td>
        <td style="color: #45c527" >4.4%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>0</td>
        <td>0</td>
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
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>5</td>
        <td>4</td>
        <td style="" >1</td>
        <td style="" >22%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>971</td>
        <td>934</td>
        <td style="color: #45c527" >37</td>
        <td style="color: #45c527" >3.9%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>124</td>
        <td>111</td>
        <td style="" >13</td>
        <td style="" >11%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>2</td>
        <td>2</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>5</td>
        <td>5</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/mint-app/issue_gauge_mint-app_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/mint-app/commit_sparklines_mint-app_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/mint-app/firstResponseForClosedPR_mint-app_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/mint-app/total_line_makeup_mint-app_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/mint-app/new_commit_contributors_by_day_over_last_month_mint-app_data.svg, /CMSgov/mint-app/new_commit_contributors_by_day_over_last_six_months_mint-app_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>