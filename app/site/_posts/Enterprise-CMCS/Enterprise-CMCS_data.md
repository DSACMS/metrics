---
layout: org-report
title: Open Source at CMS Metrics Report for Enterprise-CMCS | REPORT-2024-06-30
permalink: /Enterprise-CMCS/

org: Enterprise-CMCS
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
        <td>28799</td>
        <td>28737</td>
        <td style="color: #45c527" >62</td>
        <td style="color: #45c527" >0.22%</td>
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
        <td>146</td>
        <td>142</td>
        <td style="" >4</td>
        <td style="" >2.8%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>12411</td>
        <td>12345</td>
        <td style="color: #45c527" >66</td>
        <td style="color: #45c527" >0.53%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>3220</td>
        <td>3207</td>
        <td style="" >13</td>
        <td style="" >0.4%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>82</td>
        <td>83</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >1.2%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>168</td>
        <td>168</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>202</td>
        <td>201</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.5%</td>
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
  </div>
</div>