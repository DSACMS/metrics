---
layout: repo-report
title: Open Source at CMS Metrics Report for repo-scaffolder | REPORT-2024-11-24
permalink: /DSACMS/repo-scaffolder/

org: DSACMS
repo: repo-scaffolder
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
        <td>654</td>
        <td>622</td>
        <td style="color: #45c527" >32</td>
        <td style="color: #45c527" >5%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>54</td>
        <td>53</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >1.9%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>29</td>
        <td>28</td>
        <td style="" >1</td>
        <td style="" >3.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>25</td>
        <td>25</td>
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
        <td>131</td>
        <td>127</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >3.1%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>25</td>
        <td>24</td>
        <td style="" >1</td>
        <td style="" >4.1%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>10</td>
        <td>10</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>26</td>
        <td>25</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >3.9%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>2</td>
        <td>2</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/issue_gauge_repo-scaffolder_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/commit_sparklines_repo-scaffolder_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/DSACMS/repo-scaffolder/firstResponseForClosedPR_repo-scaffolder_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/total_line_makeup_repo-scaffolder_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/DSACMS/repo-scaffolder/new_commit_contributors_by_day_over_last_month_repo-scaffolder_data.svg, /DSACMS/repo-scaffolder/new_commit_contributors_by_day_over_last_six_months_repo-scaffolder_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
    <!-- Languages Graphs - Summary + Predominant -->
    {% assign optionsArray = 'Summary, Predominant' | split: ',' %}
    {% assign graphsArray = "/DSACMS/repo-scaffolder/language_summary_repo-scaffolder_data.svg, /DSACMS/repo-scaffolder/predominant_langs_repo-scaffolder_data.svg" | split: ',' %}
    {% render "graph-toggle" baseurl: site.baseurl, name:"language-information" options: optionsArray, graphs: graphsArray, title: "Language Information" %}
    <!-- Average Issue Resolution Time -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/average_issue_resolution_time_repo-scaffolder_data.svg", title: "Average Issue Resolution Time" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/libyear_timeline_repo-scaffolder_data.svg", title: "Dependency Libyears" %}
    <!-- DRYness Percentages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/DRYness_repo-scaffolder_data.svg", title: "DRYness Percentage Graph" %}
    <!-- Cost Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/estimated_project_costs_repo-scaffolder_data.svg", title: "Estimated Costs" %}
     <!-- Time Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/estimated_project_time_repo-scaffolder_data.svg", title: "Estimated Time" %}
    <!-- Contributor Estimate Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/estimated_people_contributing_repo-scaffolder_data.svg", title: "Estimated Individual Contributors" %}
</div>