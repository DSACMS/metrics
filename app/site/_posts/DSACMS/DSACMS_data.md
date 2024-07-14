---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-07-14
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-07-14
date_stampThisWeek: 2024-07-14
date_stampLastWeek: 2024-07-14
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
        <td>1772</td>
        <td>1669</td>
        <td style="color: #45c527" >103</td>
        <td style="color: #45c527" >6%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>124</td>
        <td>120</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >3.3%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>85</td>
        <td>83</td>
        <td style="" >2</td>
        <td style="" >2.4%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>39</td>
        <td>37</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >5.3%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>22</td>
        <td>18</td>
        <td style="" >4</td>
        <td style="" >20%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>257</td>
        <td>232</td>
        <td style="color: #45c527" >25</td>
        <td style="color: #45c527" >10%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>32</td>
        <td>28</td>
        <td style="" >4</td>
        <td style="" >13%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>12</td>
        <td>12</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>44</td>
        <td>44</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>28</td>
        <td>27</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >3.6%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>13</td>
        <td>13</td>
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
  </div>
</div>