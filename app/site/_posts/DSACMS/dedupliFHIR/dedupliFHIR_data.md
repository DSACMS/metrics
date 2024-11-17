---
layout: repo-report
title: Open Source at CMS Metrics Report for dedupliFHIR | REPORT-2024-11-17
permalink: /DSACMS/dedupliFHIR/

org: DSACMS
repo: dedupliFHIR
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
        <td>505</td>
        <td>489</td>
        <td style="color: #45c527" >16</td>
        <td style="color: #45c527" >3.2%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>21</td>
        <td>21</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>9</td>
        <td>9</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>12</td>
        <td>12</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>5</td>
        <td>10</td>
        <td style="color: #45c527" >-5</td>
        <td style="color: #45c527" >67%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>117</td>
        <td>111</td>
        <td style="color: #45c527" >6</td>
        <td style="color: #45c527" >5.3%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>52</td>
        <td>51</td>
        <td style="" >1</td>
        <td style="" >1.9%</td>
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
        <td>8</td>
        <td>8</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>4</td>
        <td>4</td>
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
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/DSACMS/dedupliFHIR/language_summary_dedupliFHIR_data.svg, /DSACMS/dedupliFHIR/predominant_langs_dedupliFHIR_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/average_issue_resolution_time_dedupliFHIR_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/libyear_timeline_dedupliFHIR_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/DRYness_dedupliFHIR_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/estimated_project_costs_dedupliFHIR_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/estimated_project_time_dedupliFHIR_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/dedupliFHIR/estimated_people_contributing_dedupliFHIR_data.svg", title: "Estimated Individual Contributors" %}
</div>