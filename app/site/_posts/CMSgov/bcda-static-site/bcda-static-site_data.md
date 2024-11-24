---
layout: repo-report
title: Open Source at CMS Metrics Report for bcda-static-site | REPORT-2024-11-24
permalink: /CMSgov/bcda-static-site/

org: CMSgov
repo: bcda-static-site
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
        <td>222</td>
        <td>220</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.9%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>1</td>
        <td>1</td>
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
        <td>1</td>
        <td>1</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>1</td>
        <td>3</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >100%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>191</td>
        <td>189</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >1.1%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>25</td>
        <td>25</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>1</td>
        <td>1</td>
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
        <td>19</td>
        <td>18</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >5.4%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/issue_gauge_bcda-static-site_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/commit_sparklines_bcda-static-site_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/bcda-static-site/firstResponseForClosedPR_bcda-static-site_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/total_line_makeup_bcda-static-site_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/bcda-static-site/new_commit_contributors_by_day_over_last_month_bcda-static-site_data.svg, /CMSgov/bcda-static-site/new_commit_contributors_by_day_over_last_six_months_bcda-static-site_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/bcda-static-site/language_summary_bcda-static-site_data.svg, /CMSgov/bcda-static-site/predominant_langs_bcda-static-site_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/average_issue_resolution_time_bcda-static-site_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/libyear_timeline_bcda-static-site_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/DRYness_bcda-static-site_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/estimated_project_costs_bcda-static-site_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/estimated_project_time_bcda-static-site_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bcda-static-site/estimated_people_contributing_bcda-static-site_data.svg", title: "Estimated Individual Contributors" %}
</div>