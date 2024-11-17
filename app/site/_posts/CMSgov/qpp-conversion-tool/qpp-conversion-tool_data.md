---
layout: repo-report
title: Open Source at CMS Metrics Report for qpp-conversion-tool | REPORT-2024-11-17
permalink: /CMSgov/qpp-conversion-tool/

org: CMSgov
repo: qpp-conversion-tool
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
        <td>7785</td>
        <td>7785</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>46</td>
        <td>45</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >2.2%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>1</td>
        <td>1</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>45</td>
        <td>44</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >2.2%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>3</td>
        <td>1</td>
        <td style="" >2</td>
        <td style="" >100%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>1217</td>
        <td>1216</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.082%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>167</td>
        <td>167</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>62</td>
        <td>62</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>36</td>
        <td>36</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>27</td>
        <td>27</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/issue_gauge_qpp-conversion-tool_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/commit_sparklines_qpp-conversion-tool_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/qpp-conversion-tool/firstResponseForClosedPR_qpp-conversion-tool_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/total_line_makeup_qpp-conversion-tool_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/qpp-conversion-tool/new_commit_contributors_by_day_over_last_month_qpp-conversion-tool_data.svg, /CMSgov/qpp-conversion-tool/new_commit_contributors_by_day_over_last_six_months_qpp-conversion-tool_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/CMSgov/qpp-conversion-tool/language_summary_qpp-conversion-tool_data.svg, /CMSgov/qpp-conversion-tool/predominant_langs_qpp-conversion-tool_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/average_issue_resolution_time_qpp-conversion-tool_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/libyear_timeline_qpp-conversion-tool_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/DRYness_qpp-conversion-tool_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/estimated_project_costs_qpp-conversion-tool_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/estimated_project_time_qpp-conversion-tool_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/qpp-conversion-tool/estimated_people_contributing_qpp-conversion-tool_data.svg", title: "Estimated Individual Contributors" %}
</div>