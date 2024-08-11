---
layout: repo-report
title: Open Source at CMS Metrics Report for macpro-mako | REPORT-2024-08-11
permalink: /Enterprise-CMCS/macpro-mako/

org: Enterprise-CMCS
repo: macpro-mako
reportID: REPORT-2024-08-11
date_stampThisWeek: 2024-08-11
date_stampLastWeek: 2024-08-11
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
        <td>1472</td>
        <td>1417</td>
        <td style="color: #45c527" >55</td>
        <td style="color: #45c527" >3.8%</td>
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
        <td>7</td>
        <td>8</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >13%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>557</td>
        <td>541</td>
        <td style="color: #45c527" >16</td>
        <td style="color: #45c527" >2.9%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>118</td>
        <td>117</td>
        <td style="" >1</td>
        <td style="" >0.85%</td>
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
        <td>6</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >15%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>4</td>
        <td>5</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >22%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mako/issue_gauge_macpro-mako_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mako/commit_sparklines_macpro-mako_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/macpro-mako/firstResponseForClosedPR_macpro-mako_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mako/total_line_makeup_macpro-mako_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/macpro-mako/new_commit_contributors_by_day_over_last_month_macpro-mako_data.svg, /Enterprise-CMCS/macpro-mako/new_commit_contributors_by_day_over_last_six_months_macpro-mako_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>