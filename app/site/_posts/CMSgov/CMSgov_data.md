---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-08-28
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-08-28
date_stampThisWeek: 2024-08-28
date_stampLastWeek: 2024-08-28
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
        <td>53455</td>
        <td>53274</td>
        <td style="color: #45c527" >181</td>
        <td style="color: #45c527" >0.34%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>929</td>
        <td>926</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >0.32%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>108</td>
        <td>109</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >0.92%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>821</td>
        <td>817</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.49%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>225</td>
        <td>230</td>
        <td style="color: #45c527" >-5</td>
        <td style="color: #45c527" >2.2%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19254</td>
        <td>19112</td>
        <td style="color: #45c527" >142</td>
        <td style="color: #45c527" >0.74%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4309</td>
        <td>4279</td>
        <td style="" >30</td>
        <td style="" >0.7%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>566</td>
        <td>564</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.35%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1410</td>
        <td>1396</td>
        <td style="color: #45c527" >14</td>
        <td style="color: #45c527" >1%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1787</td>
        <td>1772</td>
        <td style="color: #45c527" >15</td>
        <td style="color: #45c527" >0.84%</td>
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