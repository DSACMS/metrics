---
layout: repo-report
title: Open Source at CMS Metrics Report for macpro-mdct-qmr | REPORT-2024-11-17
permalink: /Enterprise-CMCS/macpro-mdct-qmr/

org: Enterprise-CMCS
repo: macpro-mdct-qmr
reportID: REPORT-2024-11-17
date_stampThisWeek: 2024-11-17
date_stampLastWeek: 2024-11-17
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
        <td>4563</td>
        <td>4558</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.11%</td>
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
        <td>13</td>
        <td>5</td>
        <td style="" >8</td>
        <td style="" >89%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1537</td>
        <td>1536</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.065%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>246</td>
        <td>245</td>
        <td style="" >1</td>
        <td style="" >0.41%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>2</td>
        <td>2</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/issue_gauge_macpro-mdct-qmr_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/commit_sparklines_macpro-mdct-qmr_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/macpro-mdct-qmr/firstResponseForClosedPR_macpro-mdct-qmr_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/total_line_makeup_macpro-mdct-qmr_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/macpro-mdct-qmr/new_commit_contributors_by_day_over_last_month_macpro-mdct-qmr_data.svg, /Enterprise-CMCS/macpro-mdct-qmr/new_commit_contributors_by_day_over_last_six_months_macpro-mdct-qmr_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/Enterprise-CMCS/macpro-mdct-qmr/language_summary_macpro-mdct-qmr_data.svg, /Enterprise-CMCS/macpro-mdct-qmr/predominant_langs_macpro-mdct-qmr_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/average_issue_resolution_time_macpro-mdct-qmr_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/libyear_timeline_macpro-mdct-qmr_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/DRYness_macpro-mdct-qmr_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/estimated_project_costs_macpro-mdct-qmr_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/estimated_project_time_macpro-mdct-qmr_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-qmr/estimated_people_contributing_macpro-mdct-qmr_data.svg", title: "Estimated Individual Contributors" %}
</div>