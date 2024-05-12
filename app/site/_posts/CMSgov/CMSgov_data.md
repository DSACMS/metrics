---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-05-12
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-05-12
date_stampThisWeek: 2024-05-12
date_stampLastWeek: 2024-05-12
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
        <td>52120</td>
        <td>51991</td>
        <td style="color: #45c527" >129</td>
        <td style="color: #45c527" >0.25%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>904</td>
        <td>903</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.11%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>118</td>
        <td>121</td>
        <td style="color: #45c527" >-3</td>
        <td style="color: #45c527" >2.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>786</td>
        <td>782</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.51%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>242</td>
        <td>245</td>
        <td style="color: #45c527" >-3</td>
        <td style="color: #45c527" >1.2%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18275</td>
        <td>18170</td>
        <td style="color: #45c527" >105</td>
        <td style="color: #45c527" >0.58%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4073</td>
        <td>4052</td>
        <td style="" >21</td>
        <td style="" >0.52%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>574</td>
        <td>571</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.52%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1348</td>
        <td>1335</td>
        <td style="color: #45c527" >13</td>
        <td style="color: #45c527" >0.97%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1752</td>
        <td>1745</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >0.4%</td>
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