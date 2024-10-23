---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-10-23
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-10-23
date_stampThisWeek: 2024-10-23
date_stampLastWeek: 2024-10-23
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
        <td>2587</td>
        <td>2441</td>
        <td style="color: #45c527" >146</td>
        <td style="color: #45c527" >5.8%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>160</td>
        <td>157</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >1.9%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>82</td>
        <td>82</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>78</td>
        <td>75</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >3.9%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>29</td>
        <td>30</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >3.4%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>401</td>
        <td>396</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>113</td>
        <td>108</td>
        <td style="" >5</td>
        <td style="" >4.5%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>17</td>
        <td>17</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>47</td>
        <td>43</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >8.9%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>24</td>
        <td>24</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>20</td>
        <td>20</td>
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
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_issue_gauge.svg", title: "Issues & PRs Status Breakdown" %}
    <!-- New Issues over Last 6 Months -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_new_issues_by_day_over_last_six_months.svg", title: "New Issues over Last 6 Months" %}
    <!-- Top Committers Bar Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_top_committers.svg", title: "Top Committers" %}
    <!-- Libyear Timeline Graph -->
    {% render "graph-section" baseurl: site.baseurl, path: "/DSACMS/DSACMS_libyear_timeline.svg", title: "Dependency Libyears" %}
  </div>
</div>