---
layout: repo-report
title: Open Source at CMS Metrics Report for batcave-workflow-engine | REPORT-2024-04-28
permalink: /CMS-Enterprise/batcave-workflow-engine/

org: CMS-Enterprise
repo: batcave-workflow-engine
reportID: REPORT-2024-04-28
date_stampThisWeek: 2024-04-28
date_stampLastWeek: 2024-04-28
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
        <td>211</td>
        <td>208</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >1.4%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>1</td>
        <td>1</td>
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
        <td>1</td>
        <td>1</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>1</td>
        <td>1</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>31</td>
        <td>29</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >6.7%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>5</td>
        <td>5</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>1</td>
        <td>0</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >200%</td>
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
        <td>8</td>
        <td>8</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-workflow-engine/issue_gauge_batcave-workflow-engine_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-workflow-engine/commit_sparklines_batcave-workflow-engine_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMS-Enterprise/batcave-workflow-engine/firstResponseForClosedPR_batcave-workflow-engine_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-workflow-engine/total_line_makeup_batcave-workflow-engine_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMS-Enterprise/batcave-workflow-engine/new_commit_contributors_by_day_over_last_month_batcave-workflow-engine_data.svg, /CMS-Enterprise/batcave-workflow-engine/new_commit_contributors_by_day_over_last_six_months_batcave-workflow-engine_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>