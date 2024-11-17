---
layout: repo-report
title: Open Source at CMS Metrics Report for metrics | REPORT-2024-11-17
permalink: /DSACMS/metrics/

org: DSACMS
repo: metrics
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
        <td>1460</td>
        <td>1435</td>
        <td style="color: #45c527" >25</td>
        <td style="color: #45c527" >1.7%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>46</td>
        <td>45</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >2.2%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>16</td>
        <td>15</td>
        <td style="" >1</td>
        <td style="" >6.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>30</td>
        <td>30</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>15</td>
        <td>11</td>
        <td style="" >4</td>
        <td style="" >31%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>176</td>
        <td>174</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >1.1%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>49</td>
        <td>48</td>
        <td style="" >1</td>
        <td style="" >2.1%</td>
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
        <td>7</td>
        <td>7</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/DSACMS/metrics/issue_gauge_metrics_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/metrics/commit_sparklines_metrics_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/DSACMS/metrics/firstResponseForClosedPR_metrics_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/metrics/total_line_makeup_metrics_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/DSACMS/metrics/new_commit_contributors_by_day_over_last_month_metrics_data.svg, /DSACMS/metrics/new_commit_contributors_by_day_over_last_six_months_metrics_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/DSACMS/metrics/language_summary_metrics_data.svg, /DSACMS/metrics/predominant_langs_metrics_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/metrics/average_issue_resolution_time_metrics_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/metrics/libyear_timeline_metrics_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/metrics/DRYness_metrics_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/metrics/estimated_project_costs_metrics_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/metrics/estimated_project_time_metrics_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/metrics/estimated_people_contributing_metrics_data.svg", title: "Estimated Individual Contributors" %}
</div>