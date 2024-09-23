---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-09-23
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-09-23
date_stampThisWeek: 2024-09-23
date_stampLastWeek: 2024-09-23
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
        <td>53754</td>
        <td>53700</td>
        <td style="color: #45c527" >54</td>
        <td style="color: #45c527" >0.1%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>936</td>
        <td>936</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>110</td>
        <td>110</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>826</td>
        <td>826</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>225</td>
        <td>224</td>
        <td style="" >1</td>
        <td style="" >0.45%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19433</td>
        <td>19385</td>
        <td style="color: #45c527" >48</td>
        <td style="color: #45c527" >0.25%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4371</td>
        <td>4355</td>
        <td style="" >16</td>
        <td style="" >0.37%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>572</td>
        <td>571</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.17%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1421</td>
        <td>1416</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.35%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1792</td>
        <td>1803</td>
        <td style="color: #d31c08" >-11</td>
        <td style="color: #d31c08" >0.61%</td>
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