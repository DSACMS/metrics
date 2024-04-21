---
layout: org-report
title: Open Source at CMS Metrics Report for CMSgov | REPORT-2024-04-21
permalink: /CMSgov/

org: CMSgov
reportID: REPORT-2024-04-21
date_stampThisWeek: 2024-04-21
date_stampLastWeek: 2024-04-21
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
        <td>51904</td>
        <td>51814</td>
        <td style="color: #45c527" >90</td>
        <td style="color: #45c527" >0.17%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>903</td>
        <td>903</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>121</td>
        <td>122</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >0.82%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>782</td>
        <td>781</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.13%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>242</td>
        <td>248</td>
        <td style="color: #45c527" >-6</td>
        <td style="color: #45c527" >2.4%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>18117</td>
        <td>18071</td>
        <td style="color: #45c527" >46</td>
        <td style="color: #45c527" >0.25%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>4042</td>
        <td>4009</td>
        <td style="" >33</td>
        <td style="" >0.82%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>570</td>
        <td>568</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >0.35%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>1332</td>
        <td>1332</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>1740</td>
        <td>1730</td>
        <td style="color: #45c527" >10</td>
        <td style="color: #45c527" >0.58%</td>
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