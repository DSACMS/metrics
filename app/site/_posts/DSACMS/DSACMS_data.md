---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-09-22
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-09-22
date_stampThisWeek: 2024-09-22
date_stampLastWeek: 2024-09-22
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
        <td>2187</td>
        <td>2111</td>
        <td style="color: #45c527" >76</td>
        <td style="color: #45c527" >3.5%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>147</td>
        <td>142</td>
        <td style="color: #45c527" >5</td>
        <td style="color: #45c527" >3.5%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>80</td>
        <td>78</td>
        <td style="" >2</td>
        <td style="" >2.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>67</td>
        <td>64</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >4.6%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>27</td>
        <td>20</td>
        <td style="" >7</td>
        <td style="" >30%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>347</td>
        <td>333</td>
        <td style="color: #45c527" >14</td>
        <td style="color: #45c527" >4.1%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>75</td>
        <td>67</td>
        <td style="" >8</td>
        <td style="" >11%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>15</td>
        <td>13</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >14%</td>
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
        <td>24</td>
        <td>23</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >4.3%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>19</td>
        <td>18</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >5.4%</td>
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