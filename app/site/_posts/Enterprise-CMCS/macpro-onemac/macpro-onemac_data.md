---
layout: repo-report
title: Open Source at CMS Metrics Report for macpro-onemac | REPORT-2024-08-28
permalink: /Enterprise-CMCS/macpro-onemac/

org: Enterprise-CMCS
repo: macpro-onemac
reportID: REPORT-2024-08-28
date_stampThisWeek: 2024-08-28
date_stampLastWeek: 2024-08-28
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
        <td>1911</td>
        <td>1906</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.26%</td>
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
        <td>28</td>
        <td>26</td>
        <td style="" >2</td>
        <td style="" >7.4%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1122</td>
        <td>1118</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.36%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>348</td>
        <td>347</td>
        <td style="" >1</td>
        <td style="" >0.29%</td>
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
        <td>4</td>
        <td>4</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>12</td>
        <td>12</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-onemac/issue_gauge_macpro-onemac_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-onemac/commit_sparklines_macpro-onemac_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/macpro-onemac/firstResponseForClosedPR_macpro-onemac_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-onemac/total_line_makeup_macpro-onemac_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/macpro-onemac/new_commit_contributors_by_day_over_last_month_macpro-onemac_data.svg, /Enterprise-CMCS/macpro-onemac/new_commit_contributors_by_day_over_last_six_months_macpro-onemac_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>