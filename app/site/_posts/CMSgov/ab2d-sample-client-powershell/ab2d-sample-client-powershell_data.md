---
layout: repo-report
title: Open Source at CMS Metrics Report for ab2d-sample-client-powershell | REPORT-2024-12-22
permalink: /CMSgov/ab2d-sample-client-powershell/

org: CMSgov
repo: ab2d-sample-client-powershell
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
        <td>36</td>
        <td>36</td>
        <td style="" >0</td>
        <td style="" >0%</td>
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
        <td>1</td>
        <td>1</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>13</td>
        <td>13</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
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
        <td>3</td>
        <td>3</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>18</td>
        <td>18</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/issue_gauge_ab2d-sample-client-powershell_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/commit_sparklines_ab2d-sample-client-powershell_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/ab2d-sample-client-powershell/firstResponseForClosedPR_ab2d-sample-client-powershell_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/total_line_makeup_ab2d-sample-client-powershell_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/ab2d-sample-client-powershell/new_commit_contributors_by_day_over_last_month_ab2d-sample-client-powershell_data.svg, /CMSgov/ab2d-sample-client-powershell/new_commit_contributors_by_day_over_last_six_months_ab2d-sample-client-powershell_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/ab2d-sample-client-powershell/language_summary_ab2d-sample-client-powershell_data.svg, /CMSgov/ab2d-sample-client-powershell/predominant_langs_ab2d-sample-client-powershell_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/average_issue_resolution_time_ab2d-sample-client-powershell_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/libyear_timeline_ab2d-sample-client-powershell_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/DRYness_ab2d-sample-client-powershell_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/estimated_project_costs_ab2d-sample-client-powershell_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/estimated_project_time_ab2d-sample-client-powershell_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/ab2d-sample-client-powershell/estimated_people_contributing_ab2d-sample-client-powershell_data.svg", title: "Estimated Individual Contributors" %}
</div>