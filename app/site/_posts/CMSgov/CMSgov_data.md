---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-08-12
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-08-12
date_stampThisWeek: 2024-08-12
date_stampLastWeek: 2024-08-12
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
        <td>53274</td>
        <td>53212</td>
        <td style="color: #45c527" >62</td>
        <td style="color: #45c527" >0.12%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>926</td>
        <td>924</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.22%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>109</td>
        <td>107</td>
        <td style="" >2</td>
        <td style="" >1.9%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>817</td>
        <td>817</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>230</td>
        <td>224</td>
        <td style="" >6</td>
        <td style="" >2.6%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>19112</td>
        <td>19060</td>
        <td style="color: #45c527" >52</td>
        <td style="color: #45c527" >0.27%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4279</td>
        <td>4264</td>
        <td style="" >15</td>
        <td style="" >0.35%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>564</td>
        <td>563</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.18%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1396</td>
        <td>1389</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >0.5%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1772</td>
        <td>1770</td>
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