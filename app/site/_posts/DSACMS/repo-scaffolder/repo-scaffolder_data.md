---
layout: repo-report
title: Open Source at CMS Metrics Report for repo-scaffolder | REPORT-2024-10-08
permalink: /DSACMS/repo-scaffolder/

org: DSACMS
repo: repo-scaffolder
reportID: REPORT-2024-10-08
date_stampThisWeek: 2024-10-08
date_stampLastWeek: 2024-10-08
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
        <td>583</td>
        <td>583</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>44</td>
        <td>44</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>26</td>
        <td>26</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>18</td>
        <td>18</td>
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
        <td>110</td>
        <td>110</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>16</td>
        <td>16</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>9</td>
        <td>9</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>20</td>
        <td>21</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >4.9%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>2</td>
        <td>3</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >40%</td>
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
    <!-- Predominant Lanugages Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/predominant_langs_repo-scaffolder_data.svg", title: "Predominant Languages" %}
    <!-- Language Summary Chart -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/repo-scaffolder/language_summary_repo-scaffolder_data.svg", title: "Language Summary" %}
</div>