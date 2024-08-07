---
layout: repo-report
title: Open Source at CMS Metrics Report for beneficiary-fhir-data | REPORT-2024-08-05
permalink: /CMSgov/beneficiary-fhir-data/

org: CMSgov
repo: beneficiary-fhir-data
reportID: REPORT-2024-08-05
date_stampThisWeek: 2024-08-05
date_stampLastWeek: 2024-08-05
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
        <td>5178</td>
        <td>5166</td>
        <td style="color: #45c527" >12</td>
        <td style="color: #45c527" >0.23%</td>
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
        <td>18</td>
        <td>17</td>
        <td style="" >1</td>
        <td style="" >5.7%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1886</td>
        <td>1878</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.43%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>456</td>
        <td>452</td>
        <td style="" >4</td>
        <td style="" >0.88%</td>
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
        <td>57</td>
        <td>56</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >1.8%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>30</td>
        <td>31</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >3.3%</td>
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
</div>