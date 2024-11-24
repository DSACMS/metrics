---
layout: repo-report
title: Open Source at CMS Metrics Report for batcave-wt-sdl-reporting | REPORT-2024-11-24
permalink: /CMS-Enterprise/batcave-wt-sdl-reporting/

org: CMS-Enterprise
repo: batcave-wt-sdl-reporting
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
        <td>22</td>
        <td>22</td>
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
        <td>7</td>
        <td>7</td>
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
        <td>2</td>
        <td>2</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>7</td>
        <td>6</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >15%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/issue_gauge_batcave-wt-sdl-reporting_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/commit_sparklines_batcave-wt-sdl-reporting_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMS-Enterprise/batcave-wt-sdl-reporting/firstResponseForClosedPR_batcave-wt-sdl-reporting_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/total_line_makeup_batcave-wt-sdl-reporting_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMS-Enterprise/batcave-wt-sdl-reporting/new_commit_contributors_by_day_over_last_month_batcave-wt-sdl-reporting_data.svg, /CMS-Enterprise/batcave-wt-sdl-reporting/new_commit_contributors_by_day_over_last_six_months_batcave-wt-sdl-reporting_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMS-Enterprise/batcave-wt-sdl-reporting/language_summary_batcave-wt-sdl-reporting_data.svg, /CMS-Enterprise/batcave-wt-sdl-reporting/predominant_langs_batcave-wt-sdl-reporting_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/average_issue_resolution_time_batcave-wt-sdl-reporting_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/libyear_timeline_batcave-wt-sdl-reporting_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/DRYness_batcave-wt-sdl-reporting_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/estimated_project_costs_batcave-wt-sdl-reporting_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/estimated_project_time_batcave-wt-sdl-reporting_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-wt-sdl-reporting/estimated_people_contributing_batcave-wt-sdl-reporting_data.svg", title: "Estimated Individual Contributors" %}
</div>