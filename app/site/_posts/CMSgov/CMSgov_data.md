---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-10-20
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-10-20
date_stampThisWeek: 2024-10-20
date_stampLastWeek: 2024-10-20
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
        <td>54044</td>
        <td>53961</td>
        <td style="color: #45c527" >83</td>
        <td style="color: #45c527" >0.15%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>937</td>
        <td>937</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>108</td>
        <td>110</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >1.8%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>829</td>
        <td>827</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.24%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>219</td>
        <td>217</td>
        <td style="" >2</td>
        <td style="" >0.92%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19635</td>
        <td>19592</td>
        <td style="color: #45c527" >43</td>
        <td style="color: #45c527" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4447</td>
        <td>4432</td>
        <td style="" >15</td>
        <td style="" >0.34%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>574</td>
        <td>574</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1441</td>
        <td>1440</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.069%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1799</td>
        <td>1798</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.056%</td>
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