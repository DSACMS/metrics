---
layout: repo-report
title: Open Source at CMS Metrics Report for redhat-enterprise-linux-8-stig-baseline | REPORT-2024-06-30
permalink: /CMSgov/redhat-enterprise-linux-8-stig-baseline/

org: CMSgov
repo: redhat-enterprise-linux-8-stig-baseline
reportID: REPORT-2024-06-30
date_stampThisWeek: 2024-06-30
date_stampLastWeek: 2024-06-30
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
        <td>66</td>
        <td>66</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>6</td>
        <td>6</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>5</td>
        <td>5</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>1</td>
        <td>1</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>5</td>
        <td>5</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>5</td>
        <td>5</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>7</td>
        <td>7</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>11</td>
        <td>11</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>9</td>
        <td>9</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>15</td>
        <td>15</td>
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
    {% render "graph-section"  baseurl: site.baseurl, path: "/CMSgov/redhat-enterprise-linux-8-stig-baseline/issue_gauge_redhat-enterprise-linux-8-stig-baseline_data.svg", title: "Issues & PRs Status Breakdown" %}
    <!--- Contributor Activity Line Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/redhat-enterprise-linux-8-stig-baseline/commit_sparklines_redhat-enterprise-linux-8-stig-baseline_data.svg", title: "Commits by Month" %}
    <!--- First Response For Closed PR Scatterplot -->
    {% render "graph-section" baseurl: site.baseurl, class: "firstResponsePRCrop", path: "/CMSgov/redhat-enterprise-linux-8-stig-baseline/firstResponseForClosedPR_redhat-enterprise-linux-8-stig-baseline_data.png", title: "First Response For Closed PR" %}
    <!--- Line Complexity Graphs -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/redhat-enterprise-linux-8-stig-baseline/total_line_makeup_redhat-enterprise-linux-8-stig-baseline_data.svg", title: "Line Complexity" %}
    <!--- New Commit Contributors by Day over Last Month and Last 6 Months -->
      {% assign optionsArray = '1 Month, 6 Month' | split: ',' %}
      {% assign graphsArray = '/CMSgov/redhat-enterprise-linux-8-stig-baseline/new_commit_contributors_by_day_over_last_month_redhat-enterprise-linux-8-stig-baseline_data.svg, /CMSgov/redhat-enterprise-linux-8-stig-baseline/new_commit_contributors_by_day_over_last_six_months_redhat-enterprise-linux-8-stig-baseline_data.svg' | split: ',' %}
      {% render "graph-toggle", baseurl: site.baseurl, name: "new-contributors" options: optionsArray, graphs: graphsArray, title: "Number of Contributors Joining per Interval" %}
</div>