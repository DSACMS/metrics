---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-04-28
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-04-28
date_stampThisWeek: 2024-04-28
date_stampLastWeek: 2024-04-28
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
        <td>51991</td>
        <td>51904</td>
        <td style="color: #45c527" >87</td>
        <td style="color: #45c527" >0.17%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>903</td>
        <td>903</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>121</td>
        <td>121</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>782</td>
        <td>782</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>245</td>
        <td>242</td>
        <td style="" >3</td>
        <td style="" >1.2%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18170</td>
        <td>18117</td>
        <td style="color: #45c527" >53</td>
        <td style="color: #45c527" >0.29%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4052</td>
        <td>4042</td>
        <td style="" >10</td>
        <td style="" >0.25%</td>
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
        <td>1335</td>
        <td>1332</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1745</td>
        <td>1740</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.29%</td>
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