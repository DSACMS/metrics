---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-07-28
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-07-28
date_stampThisWeek: 2024-07-28
date_stampLastWeek: 2024-07-28
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
        <td>53077</td>
        <td>52983</td>
        <td style="color: #45c527" >94</td>
        <td style="color: #45c527" >0.18%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>922</td>
        <td>921</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.11%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>107</td>
        <td>118</td>
        <td style="color: #45c527" >-11</td>
        <td style="color: #45c527" >9.8%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>815</td>
        <td>803</td>
        <td style="color: #45c527" >12</td>
        <td style="color: #45c527" >1.5%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>231</td>
        <td>228</td>
        <td style="" >3</td>
        <td style="" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18937</td>
        <td>18853</td>
        <td style="color: #45c527" >84</td>
        <td style="color: #45c527" >0.44%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4225</td>
        <td>4204</td>
        <td style="" >21</td>
        <td style="" >0.5%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>563</td>
        <td>562</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.18%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1384</td>
        <td>1379</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >0.36%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1775</td>
        <td>1771</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.23%</td>
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