---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-04-28
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-04-28
date_stampThisWeek: 2024-04-28
date_stampLastWeek: 2024-04-28
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
        <td>1242</td>
        <td>1233</td>
        <td style="color: #45c527" >9</td>
        <td style="color: #45c527" >0.73%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>83</td>
        <td>80</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >3.7%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>57</td>
        <td>56</td>
        <td style="" >1</td>
        <td style="" >1.8%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>26</td>
        <td>24</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >8%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>11</td>
        <td>12</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >8.7%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>192</td>
        <td>188</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >2.1%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>19</td>
        <td>19</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>7</td>
        <td>7</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>37</td>
        <td>35</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >5.6%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>24</td>
        <td>22</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >8.7%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>12</td>
        <td>12</td>
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