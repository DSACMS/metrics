---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-06-23
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-06-23
date_stampThisWeek: 2024-06-23
date_stampLastWeek: 2024-06-23
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
        <td>52533</td>
        <td>52424</td>
        <td style="color: #45c527" >109</td>
        <td style="color: #45c527" >0.21%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>911</td>
        <td>910</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.11%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>125</td>
        <td>123</td>
        <td style="" >2</td>
        <td style="" >1.6%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>786</td>
        <td>787</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >0.13%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>282</td>
        <td>262</td>
        <td style="" >20</td>
        <td style="" >7.4%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18575</td>
        <td>18487</td>
        <td style="color: #45c527" >88</td>
        <td style="color: #45c527" >0.47%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4140</td>
        <td>4112</td>
        <td style="" >28</td>
        <td style="" >0.68%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>571</td>
        <td>570</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.18%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1367</td>
        <td>1366</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.073%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1780</td>
        <td>1766</td>
        <td style="color: #45c527" >14</td>
        <td style="color: #45c527" >0.79%</td>
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
  </div>
</div>