---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-11-17
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-11-17
date_stampThisWeek: 2024-11-17
date_stampLastWeek: 2024-11-17
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
        <td>3855</td>
        <td>3788</td>
        <td style="color: #45c527" >67</td>
        <td style="color: #45c527" >1.8%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>190</td>
        <td>188</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >1.1%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>98</td>
        <td>99</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >1%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>92</td>
        <td>89</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >3.3%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>38</td>
        <td>31</td>
        <td style="" >7</td>
        <td style="" >20%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>862</td>
        <td>846</td>
        <td style="color: #45c527" >16</td>
        <td style="color: #45c527" >1.9%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>150</td>
        <td>148</td>
        <td style="" >2</td>
        <td style="" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>23</td>
        <td>23</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>65</td>
        <td>65</td>
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
        <td>24</td>
        <td>24</td>
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