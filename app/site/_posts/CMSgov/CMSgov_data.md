---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-06-10
permalink: /CMSgov/

org: CMSgov
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
        <td>52424</td>
        <td>52341</td>
        <td style="color: #45c527" >83</td>
        <td style="color: #45c527" >0.16%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>910</td>
        <td>908</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>123</td>
        <td>122</td>
        <td style="" >1</td>
        <td style="" >0.82%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>787</td>
        <td>786</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.13%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>262</td>
        <td>263</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >0.38%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18487</td>
        <td>18437</td>
        <td style="color: #45c527" >50</td>
        <td style="color: #45c527" >0.27%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4112</td>
        <td>4106</td>
        <td style="" >6</td>
        <td style="" >0.15%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>570</td>
        <td>570</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1366</td>
        <td>1363</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1766</td>
        <td>1760</td>
        <td style="color: #45c527" >6</td>
        <td style="color: #45c527" >0.34%</td>
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