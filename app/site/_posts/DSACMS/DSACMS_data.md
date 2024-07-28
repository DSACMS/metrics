---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-07-28
permalink: /DSACMS/

org: DSACMS
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
        <td>1894</td>
        <td>1785</td>
        <td style="color: #45c527" >109</td>
        <td style="color: #45c527" >5.9%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>129</td>
        <td>124</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >4%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>82</td>
        <td>84</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >2.4%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>47</td>
        <td>40</td>
        <td style="color: #45c527" >7</td>
        <td style="color: #45c527" >16%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>16</td>
        <td>33</td>
        <td style="color: #45c527" >-17</td>
        <td style="color: #45c527" >69%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>285</td>
        <td>265</td>
        <td style="color: #45c527" >20</td>
        <td style="color: #45c527" >7.3%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>36</td>
        <td>32</td>
        <td style="" >4</td>
        <td style="" >12%</td>
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
        <td>30</td>
        <td>30</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>14</td>
        <td>13</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >7.4%</td>
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