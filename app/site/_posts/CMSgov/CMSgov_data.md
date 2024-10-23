---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-10-23
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-10-23
date_stampThisWeek: 2024-10-23
date_stampLastWeek: 2024-10-23
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
        <td>54107</td>
        <td>54044</td>
        <td style="color: #45c527" >63</td>
        <td style="color: #45c527" >0.12%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>938</td>
        <td>937</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.11%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>108</td>
        <td>108</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>830</td>
        <td>829</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.12%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>201</td>
        <td>219</td>
        <td style="color: #45c527" >-18</td>
        <td style="color: #45c527" >8.6%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19672</td>
        <td>19635</td>
        <td style="color: #45c527" >37</td>
        <td style="color: #45c527" >0.19%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4460</td>
        <td>4447</td>
        <td style="" >13</td>
        <td style="" >0.29%</td>
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
        <td>1441</td>
        <td>1441</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1799</td>
        <td>1799</td>
        <td style="" >0</td>
        <td style="" >0%</td>
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