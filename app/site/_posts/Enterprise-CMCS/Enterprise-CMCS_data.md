---
layout: org-report
title: Open Source at CMS Metrics Report for Enterprise-CMCS | REPORT-2024-07-28
permalink: /Enterprise-CMCS/

org: Enterprise-CMCS
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
        <td>29161</td>
        <td>29079</td>
        <td style="color: #45c527" >82</td>
        <td style="color: #45c527" >0.28%</td>
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
        <td>166</td>
        <td>167</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >0.6%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>12812</td>
        <td>12720</td>
        <td style="color: #45c527" >92</td>
        <td style="color: #45c527" >0.72%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>3308</td>
        <td>3287</td>
        <td style="" >21</td>
        <td style="" >0.64%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>85</td>
        <td>85</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>170</td>
        <td>168</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >1.2%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>210</td>
        <td>210</td>
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
  </div>
</div>