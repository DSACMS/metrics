---
layout: repo-report
title: Open Source at CMS Metrics Report for CMS-GoogleMaps-Socrata-Integration | REPORT-2024-12-22
permalink: /CMSgov/CMS-GoogleMaps-Socrata-Integration/

org: CMSgov
repo: CMS-GoogleMaps-Socrata-Integration
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
        <td>1</td>
        <td>1</td>
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
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>0</td>
        <td>0</td>
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
        <td>8</td>
        <td>8</td>
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
        <td>10</td>
        <td>10</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/issue_gauge_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/commit_sparklines_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/firstResponseForClosedPR_CMS-GoogleMaps-Socrata-Integration_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/total_line_makeup_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/CMS-GoogleMaps-Socrata-Integration/new_commit_contributors_by_day_over_last_month_CMS-GoogleMaps-Socrata-Integration_data.svg, /CMSgov/CMS-GoogleMaps-Socrata-Integration/new_commit_contributors_by_day_over_last_six_months_CMS-GoogleMaps-Socrata-Integration_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/CMS-GoogleMaps-Socrata-Integration/language_summary_CMS-GoogleMaps-Socrata-Integration_data.svg, /CMSgov/CMS-GoogleMaps-Socrata-Integration/predominant_langs_CMS-GoogleMaps-Socrata-Integration_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/average_issue_resolution_time_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/libyear_timeline_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/DRYness_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/estimated_project_costs_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/estimated_project_time_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMS-GoogleMaps-Socrata-Integration/estimated_people_contributing_CMS-GoogleMaps-Socrata-Integration_data.svg", title: "Estimated Individual Contributors" %}
</div>