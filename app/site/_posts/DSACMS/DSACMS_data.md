---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-11-10
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-11-10
date_stampThisWeek: 2024-11-10
date_stampLastWeek: 2024-11-10
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
        <td>3788</td>
        <td>3758</td>
        <td style="color: #45c527" >30</td>
        <td style="color: #45c527" >0.8%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>188</td>
        <td>188</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>99</td>
        <td>101</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >2%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>89</td>
        <td>87</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >2.3%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>31</td>
        <td>28</td>
        <td style="" >3</td>
        <td style="" >10%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>846</td>
        <td>835</td>
        <td style="color: #45c527" >11</td>
        <td style="color: #45c527" >1.3%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>148</td>
        <td>145</td>
        <td style="" >3</td>
        <td style="" >2%</td>
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