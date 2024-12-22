---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-12-22
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-12-22
date_stampThisWeek: 2024-12-22
date_stampLastWeek: 2024-12-22
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
        <td>4058</td>
        <td>4030</td>
        <td style="color: #45c527" >28</td>
        <td style="color: #45c527" >0.69%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>195</td>
        <td>194</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.51%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>103</td>
        <td>102</td>
        <td style="" >1</td>
        <td style="" >0.98%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>92</td>
        <td>92</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>48</td>
        <td>49</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >2.1%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>921</td>
        <td>912</td>
        <td style="color: #45c527" >9</td>
        <td style="color: #45c527" >0.98%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>175</td>
        <td>170</td>
        <td style="" >5</td>
        <td style="" >2.9%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>24</td>
        <td>24</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>66</td>
        <td>66</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>36</td>
        <td>36</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>25</td>
        <td>24</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >4.1%</td>
      </tr>
    </tbody>
  </table>
</div>
<div class="graph-container">
  <br>
  <h2>Activity Graphs</h2>
  <div class="all-graphs">
    <!--- Issues/PRs Status Breakdown Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_top_committers.svg", title: "Top Committers" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_libyear_timeline.svg", title: "Dependency Libyears" %}
  </div>
</div>