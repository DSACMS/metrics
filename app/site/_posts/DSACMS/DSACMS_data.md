---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-10-27
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-10-27
date_stampThisWeek: 2024-10-27
date_stampLastWeek: 2024-10-27
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
        <td>2604</td>
        <td>2587</td>
        <td style="color: #45c527" >17</td>
        <td style="color: #45c527" >0.65%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>161</td>
        <td>160</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >0.62%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>80</td>
        <td>82</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >2.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>81</td>
        <td>78</td>
        <td style="color: #45c527" >3</td>
        <td style="color: #45c527" >3.8%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>27</td>
        <td>29</td>
        <td style="color: #45c527" >-2</td>
        <td style="color: #45c527" >7.1%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>405</td>
        <td>401</td>
        <td style="color: #45c527" >4</td>
        <td style="color: #45c527" >0.99%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>115</td>
        <td>113</td>
        <td style="" >2</td>
        <td style="" >1.8%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>18</td>
        <td>17</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >5.7%</td>
      </tr>
      <tr>
        <th scope="row">Stars</th>
        <td>47</td>
        <td>47</td>
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
        <td>22</td>
        <td>20</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >9.5%</td>
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