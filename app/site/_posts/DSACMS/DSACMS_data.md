---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-06-30
permalink: /DSACMS/

org: DSACMS
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
        <td>1629</td>
        <td>1586</td>
        <td style="color: #45c527" >43</td>
        <td style="color: #45c527" >2.7%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>115</td>
        <td>114</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.87%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>79</td>
        <td>80</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>36</td>
        <td>34</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >5.7%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>16</td>
        <td>13</td>
        <td style="" >3</td>
        <td style="" >21%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>223</td>
        <td>218</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >2.3%</td>
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
        <td>11</td>
        <td>10</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >9.5%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>44</td>
        <td>44</td>
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
      <tr>
        <th scope="row">Followers</th>
        <td>13</td>
        <td>13</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
  </div>
</div>