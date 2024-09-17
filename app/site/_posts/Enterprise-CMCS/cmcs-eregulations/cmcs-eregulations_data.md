---
layout: repo-report
title: Open Source at CMS Metrics Report for cmcs-eregulations | REPORT-2024-09-17
permalink: /Enterprise-CMCS/cmcs-eregulations/

org: Enterprise-CMCS
repo: cmcs-eregulations
reportID: REPORT-2024-09-17
date_stampThisWeek: 2024-09-17
date_stampLastWeek: 2024-09-17
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
        <td>1141</td>
        <td>1134</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >0.62%</td>
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
        <td>2</td>
        <td>5</td>
        <td style="color: #45c527" >-3</td>
        <td style="color: #45c527" >86%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1145</td>
        <td>1137</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.7%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>252</td>
        <td>251</td>
        <td style="" >1</td>
        <td style="" >0.4%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>10</td>
        <td>10</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>15</td>
        <td>15</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>11</td>
        <td>11</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/cmcs-eregulations/issue_gauge_cmcs-eregulations_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/cmcs-eregulations/commit_sparklines_cmcs-eregulations_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/cmcs-eregulations/firstResponseForClosedPR_cmcs-eregulations_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/cmcs-eregulations/total_line_makeup_cmcs-eregulations_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/cmcs-eregulations/new_commit_contributors_by_day_over_last_month_cmcs-eregulations_data.svg, /Enterprise-CMCS/cmcs-eregulations/new_commit_contributors_by_day_over_last_six_months_cmcs-eregulations_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>