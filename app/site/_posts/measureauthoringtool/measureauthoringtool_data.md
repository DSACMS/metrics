---
layout: org-report
title: Open Source at CMS Metrics Report for measureauthoringtool | REPORT-2024-11-24
permalink: /measureauthoringtool/

org: measureauthoringtool
reportID: REPORT-2024-11-24
date_stampThisWeek: 2024-11-24
date_stampLastWeek: 2024-11-24
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
        <td>43585</td>
        <td>43422</td>
        <td style="color: #45c527" >163</td>
        <td style="color: #45c527" >0.37%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>145</td>
        <td>145</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>26</td>
        <td>26</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>119</td>
        <td>119</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>610</td>
        <td>605</td>
        <td style="" >5</td>
        <td style="" >0.82%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>9826</td>
        <td>9765</td>
        <td style="color: #45c527" >61</td>
        <td style="color: #45c527" >0.62%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4019</td>
        <td>4015</td>
        <td style="" >4</td>
        <td style="" >0.1%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>197</td>
        <td>197</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>185</td>
        <td>185</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>530</td>
        <td>530</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>17</td>
        <td>17</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/measureauthoringtool_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/measureauthoringtool_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/measureauthoringtool_top_committers.svg", title: "Top Committers" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/measureauthoringtool/measureauthoringtool_libyear_timeline.svg", title: "Dependency Libyears" %}
  </div>
</div>