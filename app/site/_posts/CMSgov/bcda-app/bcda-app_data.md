---
layout: repo-report
title: Open Source at CMS Metrics Report for bcda-app | REPORT-2024-10-14
permalink: /CMSgov/bcda-app/

org: CMSgov
repo: bcda-app
reportID: REPORT-2024-10-14
date_stampThisWeek: 2024-10-14
date_stampLastWeek: 2024-10-14
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
        <td>905</td>
        <td>897</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.89%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>7</td>
        <td>7</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>2</td>
        <td>2</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>5</td>
        <td>5</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>2</td>
        <td>4</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >67%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>905</td>
        <td>897</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.89%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>82</td>
        <td>82</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>15</td>
        <td>15</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>47</td>
        <td>47</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>26</td>
        <td>26</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/bcda-app/issue_gauge_bcda-app_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-app/commit_sparklines_bcda-app_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/bcda-app/firstResponseForClosedPR_bcda-app_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-app/total_line_makeup_bcda-app_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/bcda-app/new_commit_contributors_by_day_over_last_month_bcda-app_data.svg, /CMSgov/bcda-app/new_commit_contributors_by_day_over_last_six_months_bcda-app_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>