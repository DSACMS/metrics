---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-07-21
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-07-21
date_stampThisWeek: 2024-07-21
date_stampLastWeek: 2024-07-21
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
        <td>52983</td>
        <td>52914</td>
        <td style="color: #45c527" >69</td>
        <td style="color: #45c527" >0.13%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>921</td>
        <td>921</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>118</td>
        <td>118</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>803</td>
        <td>803</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>228</td>
        <td>245</td>
        <td style="color: #45c527" >-17</td>
        <td style="color: #45c527" >7.2%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18853</td>
        <td>18793</td>
        <td style="color: #45c527" >60</td>
        <td style="color: #45c527" >0.32%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4204</td>
        <td>4179</td>
        <td style="" >25</td>
        <td style="" >0.6%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>562</td>
        <td>561</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.18%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1379</td>
        <td>1371</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >0.58%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1771</td>
        <td>1767</td>
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
  </div>
</div>