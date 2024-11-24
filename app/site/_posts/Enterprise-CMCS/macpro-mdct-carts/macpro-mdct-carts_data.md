---
layout: repo-report
title: Open Source at CMS Metrics Report for macpro-mdct-carts | REPORT-2024-11-24
permalink: /Enterprise-CMCS/macpro-mdct-carts/

org: Enterprise-CMCS
repo: macpro-mdct-carts
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
        <td>4026</td>
        <td>4018</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.2%</td>
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
        <td>4</td>
        <td style="" >2</td>
        <td style="" >40%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1350</td>
        <td>1342</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.59%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>342</td>
        <td>340</td>
        <td style="" >2</td>
        <td style="" >0.59%</td>
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
        <td>4</td>
        <td>4</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>10</td>
        <td>9</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >11%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/issue_gauge_macpro-mdct-carts_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/commit_sparklines_macpro-mdct-carts_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/Enterprise-CMCS/macpro-mdct-carts/firstResponseForClosedPR_macpro-mdct-carts_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/total_line_makeup_macpro-mdct-carts_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/Enterprise-CMCS/macpro-mdct-carts/new_commit_contributors_by_day_over_last_month_macpro-mdct-carts_data.svg, /Enterprise-CMCS/macpro-mdct-carts/new_commit_contributors_by_day_over_last_six_months_macpro-mdct-carts_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/Enterprise-CMCS/macpro-mdct-carts/language_summary_macpro-mdct-carts_data.svg, /Enterprise-CMCS/macpro-mdct-carts/predominant_langs_macpro-mdct-carts_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/average_issue_resolution_time_macpro-mdct-carts_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/libyear_timeline_macpro-mdct-carts_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/DRYness_macpro-mdct-carts_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/estimated_project_costs_macpro-mdct-carts_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/estimated_project_time_macpro-mdct-carts_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/macpro-mdct-carts/estimated_people_contributing_macpro-mdct-carts_data.svg", title: "Estimated Individual Contributors" %}
</div>