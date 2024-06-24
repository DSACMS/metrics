---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-06-24
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-06-24
date_stampThisWeek: 2024-06-24
date_stampLastWeek: 2024-06-24
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
        <td>1586</td>
        <td>1556</td>
        <td style="color: #45c527" >30</td>
        <td style="color: #45c527" >1.9%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>114</td>
        <td>113</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.88%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>80</td>
        <td>80</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>34</td>
        <td>33</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >3%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>13</td>
        <td>15</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >14%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>218</td>
        <td>207</td>
        <td style="color: #45c527" >11</td>
        <td style="color: #45c527" >5.2%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>24</td>
        <td>23</td>
        <td style="" >1</td>
        <td style="" >4.3%</td>
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
        <td>44</td>
        <td>43</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >2.3%</td>
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