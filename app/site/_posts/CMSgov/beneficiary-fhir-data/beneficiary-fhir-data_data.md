---
layout: repo-report
title: Open Source at CMS Metrics Report for beneficiary-fhir-data | REPORT-2024-11-24
permalink: /CMSgov/beneficiary-fhir-data/

org: CMSgov
repo: beneficiary-fhir-data
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
        <td>5303</td>
        <td>5300</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.057%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>4</td>
        <td>4</td>
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
        <td>4</td>
        <td>4</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>12</td>
        <td>12</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1969</td>
        <td>1965</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.2%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>482</td>
        <td>480</td>
        <td style="" >2</td>
        <td style="" >0.42%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>33</td>
        <td>33</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>60</td>
        <td>60</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>29</td>
        <td>28</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >3.5%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/issue_gauge_beneficiary-fhir-data_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/commit_sparklines_beneficiary-fhir-data_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/beneficiary-fhir-data/firstResponseForClosedPR_beneficiary-fhir-data_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/total_line_makeup_beneficiary-fhir-data_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/beneficiary-fhir-data/new_commit_contributors_by_day_over_last_month_beneficiary-fhir-data_data.svg, /CMSgov/beneficiary-fhir-data/new_commit_contributors_by_day_over_last_six_months_beneficiary-fhir-data_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/beneficiary-fhir-data/language_summary_beneficiary-fhir-data_data.svg, /CMSgov/beneficiary-fhir-data/predominant_langs_beneficiary-fhir-data_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/average_issue_resolution_time_beneficiary-fhir-data_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/libyear_timeline_beneficiary-fhir-data_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/DRYness_beneficiary-fhir-data_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/estimated_project_costs_beneficiary-fhir-data_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/estimated_project_time_beneficiary-fhir-data_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/beneficiary-fhir-data/estimated_people_contributing_beneficiary-fhir-data_data.svg", title: "Estimated Individual Contributors" %}
</div>