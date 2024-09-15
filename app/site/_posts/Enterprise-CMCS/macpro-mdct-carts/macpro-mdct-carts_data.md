---
layout: repo-report
title: Open Source at CMS Metrics Report for macpro-mdct-carts | REPORT-2024-09-15
permalink: /Enterprise-CMCS/macpro-mdct-carts/

org: Enterprise-CMCS
repo: macpro-mdct-carts
reportID: REPORT-2024-09-15
date_stampThisWeek: 2024-09-15
date_stampLastWeek: 2024-09-15
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
        <td>3982</td>
        <td>3980</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.05%</td>
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
        <td>6</td>
        <td>7</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >15%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1294</td>
        <td>1291</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.23%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>319</td>
        <td>319</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>1</td>
        <td>1</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>4</td>
        <td>4</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/issue_gauge_macpro-mdct-carts_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/commit_sparklines_macpro-mdct-carts_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/macpro-mdct-carts/firstResponseForClosedPR_macpro-mdct-carts_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/total_line_makeup_macpro-mdct-carts_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/macpro-mdct-carts/new_commit_contributors_by_day_over_last_month_macpro-mdct-carts_data.svg, /Enterprise-CMCS/macpro-mdct-carts/new_commit_contributors_by_day_over_last_six_months_macpro-mdct-carts_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>