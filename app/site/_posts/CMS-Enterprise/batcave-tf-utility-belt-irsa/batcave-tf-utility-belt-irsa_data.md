---
layout: repo-report
title: Open Source at CMS Metrics Report for batcave-tf-utility-belt-irsa | REPORT-2024-11-24
permalink: /CMS-Enterprise/batcave-tf-utility-belt-irsa/

org: CMS-Enterprise
repo: batcave-tf-utility-belt-irsa
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
        <td>15</td>
        <td>15</td>
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
        <td>14</td>
        <td>14</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>2</td>
        <td>2</td>
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
        <td>0</td>
        <td>0</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>5</td>
        <td>4</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >22%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/issue_gauge_batcave-tf-utility-belt-irsa_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/commit_sparklines_batcave-tf-utility-belt-irsa_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/firstResponseForClosedPR_batcave-tf-utility-belt-irsa_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/total_line_makeup_batcave-tf-utility-belt-irsa_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMS-Enterprise/batcave-tf-utility-belt-irsa/new_commit_contributors_by_day_over_last_month_batcave-tf-utility-belt-irsa_data.svg, /CMS-Enterprise/batcave-tf-utility-belt-irsa/new_commit_contributors_by_day_over_last_six_months_batcave-tf-utility-belt-irsa_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMS-Enterprise/batcave-tf-utility-belt-irsa/language_summary_batcave-tf-utility-belt-irsa_data.svg, /CMS-Enterprise/batcave-tf-utility-belt-irsa/predominant_langs_batcave-tf-utility-belt-irsa_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/average_issue_resolution_time_batcave-tf-utility-belt-irsa_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/libyear_timeline_batcave-tf-utility-belt-irsa_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/DRYness_batcave-tf-utility-belt-irsa_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/estimated_project_costs_batcave-tf-utility-belt-irsa_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/estimated_project_time_batcave-tf-utility-belt-irsa_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMS-Enterprise/batcave-tf-utility-belt-irsa/estimated_people_contributing_batcave-tf-utility-belt-irsa_data.svg", title: "Estimated Individual Contributors" %}
</div>