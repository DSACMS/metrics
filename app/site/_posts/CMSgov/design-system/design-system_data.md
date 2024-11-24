---
layout: repo-report
title: Open Source at CMS Metrics Report for design-system | REPORT-2024-11-24
permalink: /CMSgov/design-system/

org: CMSgov
repo: design-system
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
        <td>2363</td>
        <td>2355</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.34%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>242</td>
        <td>242</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>6</td>
        <td>6</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>236</td>
        <td>236</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>6</td>
        <td>10</td>
        <td style="color: #45c527" >-4</td>
        <td style="color: #45c527" >50%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>2248</td>
        <td>2240</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.36%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>726</td>
        <td>719</td>
        <td style="" >7</td>
        <td style="" >0.97%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>87</td>
        <td>87</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>318</td>
        <td>318</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>58</td>
        <td>57</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >1.7%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/design-system/issue_gauge_design-system_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/commit_sparklines_design-system_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/design-system/firstResponseForClosedPR_design-system_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/total_line_makeup_design-system_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/design-system/new_commit_contributors_by_day_over_last_month_design-system_data.svg, /CMSgov/design-system/new_commit_contributors_by_day_over_last_six_months_design-system_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/design-system/language_summary_design-system_data.svg, /CMSgov/design-system/predominant_langs_design-system_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/average_issue_resolution_time_design-system_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/libyear_timeline_design-system_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/DRYness_design-system_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/estimated_project_costs_design-system_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/estimated_project_time_design-system_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/design-system/estimated_people_contributing_design-system_data.svg", title: "Estimated Individual Contributors" %}
</div>