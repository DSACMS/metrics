---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-10-14
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-10-14
date_stampThisWeek: 2024-10-14
date_stampLastWeek: 2024-10-14
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
        <td>2428</td>
        <td>2408</td>
        <td style="color: #45c527" >20</td>
        <td style="color: #45c527" >0.83%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>157</td>
        <td>153</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >2.6%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>83</td>
        <td>84</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >1.2%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>74</td>
        <td>69</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >7%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>32</td>
        <td>27</td>
        <td style="" >5</td>
        <td style="" >17%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>388</td>
        <td>379</td>
        <td style="color: #45c527" >9</td>
        <td style="color: #45c527" >2.3%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>107</td>
        <td>94</td>
        <td style="" >13</td>
        <td style="" >13%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>18</td>
        <td>18</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>43</td>
        <td>43</td>
        <td style="" >0</td>
        <td style="" >0%</td>
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
  </div>
</div>