---
layout: repo-report
title: Open Source at CMS Metrics Report for macpro-mdct-mfp | REPORT-2024-10-14
permalink: /Enterprise-CMCS/macpro-mdct-mfp/

org: Enterprise-CMCS
repo: macpro-mdct-mfp
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
        <td>665</td>
        <td>661</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.6%</td>
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
        <td>3</td>
        <td>4</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >29%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>657</td>
        <td>653</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.61%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>125</td>
        <td>125</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>3</td>
        <td>3</td>
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
        <td>11</td>
        <td>10</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >9.5%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-mfp/issue_gauge_macpro-mdct-mfp_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-mfp/commit_sparklines_macpro-mdct-mfp_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/macpro-mdct-mfp/firstResponseForClosedPR_macpro-mdct-mfp_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-mfp/total_line_makeup_macpro-mdct-mfp_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/macpro-mdct-mfp/new_commit_contributors_by_day_over_last_month_macpro-mdct-mfp_data.svg, /Enterprise-CMCS/macpro-mdct-mfp/new_commit_contributors_by_day_over_last_six_months_macpro-mdct-mfp_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>