---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-06-10
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-06-10
date_stampThisWeek: 2024-06-10
date_stampLastWeek: 2024-06-10
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
        <td>1539</td>
        <td>1532</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >0.46%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>110</td>
        <td>98</td>
        <td style="color: #45c527" >12</td>
        <td style="color: #45c527" >12%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>77</td>
        <td>66</td>
        <td style="" >11</td>
        <td style="" >15%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>33</td>
        <td>32</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >3.1%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>15</td>
        <td>14</td>
        <td style="" >1</td>
        <td style="" >6.9%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>204</td>
        <td>204</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>22</td>
        <td>22</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>9</td>
        <td>8</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >12%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>41</td>
        <td>41</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>23</td>
        <td>23</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>13</td>
        <td>12</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >8%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
  </div>
</div>