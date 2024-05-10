---
layout: repo-report
title: Open Source at CMS Metrics Report for dedupliFHIR | REPORT-2024-05-06
permalink: /DSACMS/dedupliFHIR/

org: DSACMS
repo: dedupliFHIR
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
        <td>226</td>
        <td>196</td>
        <td style="color: #45c527" >30</td>
        <td style="color: #45c527" >14%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>13</td>
        <td>7</td>
        <td style="color: #45c527" >6</td>
        <td style="color: #45c527" >60%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>6</td>
        <td>4</td>
        <td style="" >2</td>
        <td style="" >40%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>7</td>
        <td>3</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >80%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>40</td>
        <td>33</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >19%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>2</td>
        <td>1</td>
        <td style="" >1</td>
        <td style="" >67%</td>
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
        <td>7</td>
        <td>4</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >55%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>5</td>
        <td>3</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >50%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/issue_gauge_dedupliFHIR_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/commit_sparklines_dedupliFHIR_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/DSACMS/dedupliFHIR/firstResponseForClosedPR_dedupliFHIR_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/total_line_makeup_dedupliFHIR_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/DSACMS/dedupliFHIR/new_commit_contributors_by_day_over_last_month_dedupliFHIR_data.svg, /DSACMS/dedupliFHIR/new_commit_contributors_by_day_over_last_six_months_dedupliFHIR_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>