---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-11-17
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-11-17
date_stampThisWeek: 2024-11-17
date_stampLastWeek: 2024-11-17
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
        <td>54320</td>
        <td>54280</td>
        <td style="color: #45c527" >40</td>
        <td style="color: #45c527" >0.074%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>982</td>
        <td>980</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.2%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>110</td>
        <td>109</td>
        <td style="" >1</td>
        <td style="" >0.91%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>872</td>
        <td>871</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.11%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>198</td>
        <td>194</td>
        <td style="" >4</td>
        <td style="" >2%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19863</td>
        <td>19816</td>
        <td style="color: #45c527" >47</td>
        <td style="color: #45c527" >0.24%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4511</td>
        <td>4499</td>
        <td style="" >12</td>
        <td style="" >0.27%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>583</td>
        <td>581</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.34%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1448</td>
        <td>1446</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.14%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1789</td>
        <td>1806</td>
        <td style="color: #d31c08" >-17</td>
        <td style="color: #d31c08" >0.95%</td>
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
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/CMSgov/CMSgov_libyear_timeline.svg", title: "Dependency Libyears" %}
  </div>
</div>