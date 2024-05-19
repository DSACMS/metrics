---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-05-19
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-05-19
date_stampThisWeek: 2024-05-19
date_stampLastWeek: 2024-05-19
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
        <td>52206</td>
        <td>52120</td>
        <td style="color: #45c527" >86</td>
        <td style="color: #45c527" >0.16%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>906</td>
        <td>904</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>120</td>
        <td>118</td>
        <td style="" >2</td>
        <td style="" >1.7%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>786</td>
        <td>786</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>247</td>
        <td>242</td>
        <td style="" >5</td>
        <td style="" >2%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18337</td>
        <td>18275</td>
        <td style="color: #45c527" >62</td>
        <td style="color: #45c527" >0.34%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4086</td>
        <td>4073</td>
        <td style="" >13</td>
        <td style="" >0.32%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>575</td>
        <td>574</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.17%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1354</td>
        <td>1348</td>
        <td style="color: #45c527" >6</td>
        <td style="color: #45c527" >0.44%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1763</td>
        <td>1752</td>
        <td style="color: #45c527" >11</td>
        <td style="color: #45c527" >0.63%</td>
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