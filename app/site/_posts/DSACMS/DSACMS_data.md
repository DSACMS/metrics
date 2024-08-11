---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-08-11
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-08-11
date_stampThisWeek: 2024-08-11
date_stampLastWeek: 2024-08-11
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
        <td>1948</td>
        <td>1894</td>
        <td style="color: #45c527" >54</td>
        <td style="color: #45c527" >2.8%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>137</td>
        <td>129</td>
        <td style="color: #45c527" >8</td>
        <td style="color: #45c527" >6%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>81</td>
        <td>82</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >1.2%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>56</td>
        <td>47</td>
        <td style="color: #45c527" >9</td>
        <td style="color: #45c527" >17%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>20</td>
        <td>16</td>
        <td style="" >4</td>
        <td style="" >22%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>301</td>
        <td>285</td>
        <td style="color: #45c527" >16</td>
        <td style="color: #45c527" >5.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>43</td>
        <td>36</td>
        <td style="" >7</td>
        <td style="" >18%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>13</td>
        <td>12</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >8%</td>
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
        <td>30</td>
        <td style="color: #d31c08" >-2</td>
        <td style="color: #d31c08" >6.9%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>14</td>
        <td>14</td>
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