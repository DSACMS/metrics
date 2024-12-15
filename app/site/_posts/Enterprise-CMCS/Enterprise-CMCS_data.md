---
layout: org-report
title: Open Source at CMS Metrics Report for Enterprise-CMCS | REPORT-2024-12-15
permalink: /Enterprise-CMCS/

org: Enterprise-CMCS
reportID: REPORT-2024-12-15
date_stampThisWeek: 2024-12-15
date_stampLastWeek: 2024-12-15
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
        <td>30599</td>
        <td>30373</td>
        <td style="color: #45c527" >226</td>
        <td style="color: #45c527" >0.74%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>3206</td>
        <td>3206</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>314</td>
        <td>314</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>2892</td>
        <td>2892</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>215</td>
        <td>237</td>
        <td style="color: #45c527" >-22</td>
        <td style="color: #45c527" >9.7%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>14088</td>
        <td>13984</td>
        <td style="color: #45c527" >104</td>
        <td style="color: #45c527" >0.74%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>3676</td>
        <td>3620</td>
        <td style="" >56</td>
        <td style="" >1.5%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>90</td>
        <td>89</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >1.1%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>179</td>
        <td>178</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.56%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>237</td>
        <td>237</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_top_committers.svg", title: "Top Committers" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/Enterprise-CMCS/Enterprise-CMCS_libyear_timeline.svg", title: "Dependency Libyears" %}
  </div>
</div>