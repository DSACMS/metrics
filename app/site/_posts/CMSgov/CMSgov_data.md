---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-05-26
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-05-26
date_stampThisWeek: 2024-05-26
date_stampLastWeek: 2024-05-26
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
        <td>52272</td>
        <td>52206</td>
        <td style="color: #45c527" >66</td>
        <td style="color: #45c527" >0.13%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>906</td>
        <td>906</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>120</td>
        <td>120</td>
        <td style="" >0</td>
        <td style="" >0%</td>
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
        <td>249</td>
        <td>247</td>
        <td style="" >2</td>
        <td style="" >0.81%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18386</td>
        <td>18337</td>
        <td style="color: #45c527" >49</td>
        <td style="color: #45c527" >0.27%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4094</td>
        <td>4086</td>
        <td style="" >8</td>
        <td style="" >0.2%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>573</td>
        <td>575</td>
        <td style="color: #d31c08" >-2</td>
        <td style="color: #d31c08" >0.35%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1355</td>
        <td>1354</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.074%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1760</td>
        <td>1763</td>
        <td style="color: #d31c08" >-3</td>
        <td style="color: #d31c08" >0.17%</td>
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