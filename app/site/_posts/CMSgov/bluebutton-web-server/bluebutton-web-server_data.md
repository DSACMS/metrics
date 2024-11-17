---
layout: repo-report
title: Open Source at CMS Metrics Report for bluebutton-web-server | REPORT-2024-11-17
permalink: /CMSgov/bluebutton-web-server/

org: CMSgov
repo: bluebutton-web-server
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
        <td>3522</td>
        <td>3517</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.14%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>26</td>
        <td>26</td>
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
        <td>26</td>
        <td>26</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>5</td>
        <td>7</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >33%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1018</td>
        <td>1013</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.49%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>216</td>
        <td>216</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>24</td>
        <td>24</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>40</td>
        <td>40</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>24</td>
        <td>25</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >4.1%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/issue_gauge_bluebutton-web-server_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/commit_sparklines_bluebutton-web-server_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/bluebutton-web-server/firstResponseForClosedPR_bluebutton-web-server_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/total_line_makeup_bluebutton-web-server_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/bluebutton-web-server/new_commit_contributors_by_day_over_last_month_bluebutton-web-server_data.svg, /CMSgov/bluebutton-web-server/new_commit_contributors_by_day_over_last_six_months_bluebutton-web-server_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/bluebutton-web-server/language_summary_bluebutton-web-server_data.svg, /CMSgov/bluebutton-web-server/predominant_langs_bluebutton-web-server_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/average_issue_resolution_time_bluebutton-web-server_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/libyear_timeline_bluebutton-web-server_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/DRYness_bluebutton-web-server_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/estimated_project_costs_bluebutton-web-server_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/estimated_project_time_bluebutton-web-server_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/bluebutton-web-server/estimated_people_contributing_bluebutton-web-server_data.svg", title: "Estimated Individual Contributors" %}
</div>