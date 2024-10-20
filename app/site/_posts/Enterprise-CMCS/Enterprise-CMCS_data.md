---
layout: org-report
title: Open Source at CMS Metrics Report for Enterprise-CMCS | REPORT-2024-10-20
permalink: /Enterprise-CMCS/

org: Enterprise-CMCS
reportID: REPORT-2024-10-20
date_stampThisWeek: 2024-10-20
date_stampLastWeek: 2024-10-20
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
        <td>29928</td>
        <td>29903</td>
        <td style="color: #45c527" >25</td>
        <td style="color: #45c527" >0.084%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>3206</td>
        <td>3206</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>314</td>
        <td>314</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>2892</td>
        <td>2892</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>155</td>
        <td>149</td>
        <td style="" >6</td>
        <td style="" >3.9%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>13613</td>
        <td>13583</td>
        <td style="color: #45c527" >30</td>
        <td style="color: #45c527" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>3503</td>
        <td>3491</td>
        <td style="" >12</td>
        <td style="" >0.34%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>88</td>
        <td>87</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >1.1%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>175</td>
        <td>175</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>209</td>
        <td>209</td>
        <td style="" >0</td>
        <td style="" >0%</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_top_committers.svg", title: "Top Committers" %}
  </div>
</div>