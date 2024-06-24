---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-06-24
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-06-24
date_stampThisWeek: 2024-06-24
date_stampLastWeek: 2024-06-24
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
        <td>52721</td>
        <td>52533</td>
        <td style="color: #45c527" >188</td>
        <td style="color: #45c527" >0.36%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>915</td>
        <td>911</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.44%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>121</td>
        <td>125</td>
        <td style="color: #45c527" >-4</td>
        <td style="color: #45c527" >3.3%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>794</td>
        <td>786</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >1%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>238</td>
        <td>282</td>
        <td style="color: #45c527" >-44</td>
        <td style="color: #45c527" >17%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18686</td>
        <td>18575</td>
        <td style="color: #45c527" >111</td>
        <td style="color: #45c527" >0.6%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4161</td>
        <td>4140</td>
        <td style="" >21</td>
        <td style="" >0.51%</td>
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
        <td>1386</td>
        <td>1367</td>
        <td style="color: #45c527" >19</td>
        <td style="color: #45c527" >1.4%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1779</td>
        <td>1780</td>
        <td style="color: #d31c08" >-1</td>
        <td style="color: #d31c08" >0.056%</td>
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