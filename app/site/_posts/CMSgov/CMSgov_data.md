---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-05-06
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-05-06
date_stampThisWeek: 2024-05-06
date_stampLastWeek: 2024-05-06
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
        <td>52071</td>
        <td>51814</td>
        <td style="color: #45c527" >257</td>
        <td style="color: #45c527" >0.49%</td>
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
        <td>122</td>
        <td>122</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>782</td>
        <td>781</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.13%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>238</td>
        <td>248</td>
        <td style="color: #45c527" >-10</td>
        <td style="color: #45c527" >4.1%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18235</td>
        <td>18071</td>
        <td style="color: #45c527" >164</td>
        <td style="color: #45c527" >0.9%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4065</td>
        <td>4009</td>
        <td style="" >56</td>
        <td style="" >1.4%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>574</td>
        <td>568</td>
        <td style="color: #45c527" >6</td>
        <td style="color: #45c527" >1.1%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1345</td>
        <td>1332</td>
        <td style="color: #45c527" >13</td>
        <td style="color: #45c527" >0.97%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1746</td>
        <td>1730</td>
        <td style="color: #45c527" >16</td>
        <td style="color: #45c527" >0.92%</td>
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