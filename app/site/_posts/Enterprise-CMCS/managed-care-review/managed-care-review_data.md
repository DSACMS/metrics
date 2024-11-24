---
layout: repo-report
title: Open Source at CMS Metrics Report for managed-care-review | REPORT-2024-11-24
permalink: /Enterprise-CMCS/managed-care-review/

org: Enterprise-CMCS
repo: managed-care-review
reportID: REPORT-2024-11-24
date_stampThisWeek: 2024-11-24
date_stampLastWeek: 2024-11-24
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
        <td>2205</td>
        <td>2182</td>
        <td style="color: #45c527" >23</td>
        <td style="color: #45c527" >1%</td>
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
        <td>9</td>
        <td style="color: #45c527" >-3</td>
        <td style="color: #45c527" >40%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>2173</td>
        <td>2150</td>
        <td style="color: #45c527" >23</td>
        <td style="color: #45c527" >1.1%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>782</td>
        <td>779</td>
        <td style="" >3</td>
        <td style="" >0.38%</td>
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
        <td>10</td>
        <td>10</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>14</td>
        <td>13</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >7.4%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/issue_gauge_managed-care-review_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/commit_sparklines_managed-care-review_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/managed-care-review/firstResponseForClosedPR_managed-care-review_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/total_line_makeup_managed-care-review_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/managed-care-review/new_commit_contributors_by_day_over_last_month_managed-care-review_data.svg, /Enterprise-CMCS/managed-care-review/new_commit_contributors_by_day_over_last_six_months_managed-care-review_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/Enterprise-CMCS/managed-care-review/language_summary_managed-care-review_data.svg, /Enterprise-CMCS/managed-care-review/predominant_langs_managed-care-review_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/average_issue_resolution_time_managed-care-review_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/libyear_timeline_managed-care-review_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/DRYness_managed-care-review_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/estimated_project_costs_managed-care-review_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/estimated_project_time_managed-care-review_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/managed-care-review/estimated_people_contributing_managed-care-review_data.svg", title: "Estimated Individual Contributors" %}
</div>