---
layout: repo-report
title: Open Source at CMS Metrics Report for hpt-validator | REPORT-2024-08-15
permalink: /CMSgov/hpt-validator/

org: CMSgov
repo: hpt-validator
reportID: REPORT-2024-08-15
date_stampThisWeek: 2024-08-15
date_stampLastWeek: 2024-08-15
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
        <td>157</td>
        <td>156</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.64%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>4</td>
        <td>3</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >29%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>1</td>
        <td>0</td>
        <td style="" >1</td>
        <td style="" >200%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>3</td>
        <td>3</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>2</td>
        <td>3</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >40%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>41</td>
        <td>40</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >2.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>6</td>
        <td>4</td>
        <td style="" >2</td>
        <td style="" >40%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>4</td>
        <td>4</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>3</td>
        <td>3</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>9</td>
        <td>8</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >12%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/hpt-validator/issue_gauge_hpt-validator_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/hpt-validator/commit_sparklines_hpt-validator_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/hpt-validator/firstResponseForClosedPR_hpt-validator_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/hpt-validator/total_line_makeup_hpt-validator_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/hpt-validator/new_commit_contributors_by_day_over_last_month_hpt-validator_data.svg, /CMSgov/hpt-validator/new_commit_contributors_by_day_over_last_six_months_hpt-validator_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>