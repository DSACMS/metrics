---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-09-15
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-09-15
date_stampThisWeek: 2024-09-15
date_stampLastWeek: 2024-09-15
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
        <td>53495</td>
        <td>53455</td>
        <td style="color: #45c527" >40</td>
        <td style="color: #45c527" >0.075%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>932</td>
        <td>929</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.32%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>110</td>
        <td>108</td>
        <td style="" >2</td>
        <td style="" >1.8%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>822</td>
        <td>821</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.12%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>227</td>
        <td>225</td>
        <td style="" >2</td>
        <td style="" >0.88%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19288</td>
        <td>19254</td>
        <td style="color: #45c527" >34</td>
        <td style="color: #45c527" >0.18%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4319</td>
        <td>4309</td>
        <td style="" >10</td>
        <td style="" >0.23%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>566</td>
        <td>566</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1413</td>
        <td>1410</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.21%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1789</td>
        <td>1787</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.11%</td>
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
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_top_committers.svg", title: "Top Committers" %}
  </div>
</div>