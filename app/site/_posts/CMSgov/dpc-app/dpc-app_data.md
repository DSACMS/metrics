---
layout: repo-report
title: Open Source at CMS Metrics Report for dpc-app | REPORT-2024-12-22
permalink: /CMSgov/dpc-app/

org: CMSgov
repo: dpc-app
reportID: REPORT-2024-12-22
date_stampThisWeek: 2024-12-22
date_stampLastWeek: 2024-12-22
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
        <td>1992</td>
        <td>1988</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.2%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>6</td>
        <td>6</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>2</td>
        <td>2</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>4</td>
        <td>4</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>8</td>
        <td>9</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >12%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1771</td>
        <td>1767</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.23%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>574</td>
        <td>571</td>
        <td style="" >3</td>
        <td style="" >0.52%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>17</td>
        <td>17</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>45</td>
        <td>45</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>20</td>
        <td>20</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/dpc-app/issue_gauge_dpc-app_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/dpc-app/commit_sparklines_dpc-app_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/dpc-app/firstResponseForClosedPR_dpc-app_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/dpc-app/total_line_makeup_dpc-app_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/dpc-app/new_commit_contributors_by_day_over_last_month_dpc-app_data.svg, /CMSgov/dpc-app/new_commit_contributors_by_day_over_last_six_months_dpc-app_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/dpc-app/language_summary_dpc-app_data.svg, /CMSgov/dpc-app/predominant_langs_dpc-app_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/dpc-app/average_issue_resolution_time_dpc-app_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/dpc-app/libyear_timeline_dpc-app_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/dpc-app/DRYness_dpc-app_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/dpc-app/estimated_project_costs_dpc-app_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/dpc-app/estimated_project_time_dpc-app_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/dpc-app/estimated_people_contributing_dpc-app_data.svg", title: "Estimated Individual Contributors" %}
</div>