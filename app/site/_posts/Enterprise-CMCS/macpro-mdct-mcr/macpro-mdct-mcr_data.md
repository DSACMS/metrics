---
layout: repo-report
title: Open Source at CMS Metrics Report for macpro-mdct-mcr | REPORT-2024-09-22
permalink: /Enterprise-CMCS/macpro-mdct-mcr/

org: Enterprise-CMCS
repo: macpro-mdct-mcr
reportID: REPORT-2024-09-22
date_stampThisWeek: 2024-09-22
date_stampLastWeek: 2024-09-22
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
        <td>1436</td>
        <td>1429</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >0.49%</td>
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
        <td>3</td>
        <td style="" >2</td>
        <td style="" >50%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1229</td>
        <td>1222</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >0.57%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>243</td>
        <td>241</td>
        <td style="" >2</td>
        <td style="" >0.83%</td>
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
        <td>5</td>
        <td>4</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >22%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>10</td>
        <td>10</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-mcr/issue_gauge_macpro-mdct-mcr_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-mcr/commit_sparklines_macpro-mdct-mcr_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/macpro-mdct-mcr/firstResponseForClosedPR_macpro-mdct-mcr_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-mcr/total_line_makeup_macpro-mdct-mcr_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/macpro-mdct-mcr/new_commit_contributors_by_day_over_last_month_macpro-mdct-mcr_data.svg, /Enterprise-CMCS/macpro-mdct-mcr/new_commit_contributors_by_day_over_last_six_months_macpro-mdct-mcr_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>