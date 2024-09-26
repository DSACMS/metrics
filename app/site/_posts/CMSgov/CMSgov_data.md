---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-09-24
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-09-24
date_stampThisWeek: 2024-09-24
date_stampLastWeek: 2024-09-24
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
        <td>53772</td>
        <td>53754</td>
        <td style="color: #45c527" >18</td>
        <td style="color: #45c527" >0.033%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>937</td>
        <td>936</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.11%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>111</td>
        <td>110</td>
        <td style="" >1</td>
        <td style="" >0.9%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>826</td>
        <td>826</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>219</td>
        <td>225</td>
        <td style="color: #45c527" >-6</td>
        <td style="color: #45c527" >2.7%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19445</td>
        <td>19433</td>
        <td style="color: #45c527" >12</td>
        <td style="color: #45c527" >0.062%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4384</td>
        <td>4371</td>
        <td style="" >13</td>
        <td style="" >0.3%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>572</td>
        <td>572</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1421</td>
        <td>1421</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1794</td>
        <td>1792</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.11%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>30</td>
        <td>30</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_top_committers.svg", title: "Top Committers" %}
  </div>
</div>