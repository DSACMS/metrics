---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-04-09
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-04-09
date_stampThisWeek: 2024-04-09
date_stampLastWeek: 2024-04-09
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
        <td>1089</td>
        <td>1015</td>
        <td style="" >74</td>
        <td style="" >7%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>73</td>
        <td>73</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>55</td>
        <td>62</td>
        <td style="color: #45c527" >-7</td>
        <td style="color: #45c527" >12%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>18</td>
        <td>11</td>
        <td style="" >7</td>
        <td style="" >48%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>13</td>
        <td>7</td>
        <td style="" >6</td>
        <td style="" >60%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>166</td>
        <td>157</td>
        <td style="" >9</td>
        <td style="" >5.6%</td>
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
        <td>32</td>
        <td>32</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Watchers</th>
        <td>22</td>
        <td>22</td>
        <td style="" >0</td>
        <td style="" >0%</td>
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