---
layout: org-report
title: Open Source at CMS Metrics Report for DSACMS | REPORT-2024-10-02
permalink: /DSACMS/

org: DSACMS
reportID: REPORT-2024-10-02
date_stampThisWeek: 2024-10-02
date_stampLastWeek: 2024-10-02
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
        <td>2282</td>
        <td>2261</td>
        <td style="color: #45c527" >21</td>
        <td style="color: #45c527" >0.92%</td>
      </tr>
      <tr>
        <th scope="row">Issues</th>
        <td>149</td>
        <td>147</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >1.4%</td>
      </tr>
      <tr>
        <th scope="row">Open Issues</th>
        <td>80</td>
        <td>80</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Closed Issues</th>
        <td>69</td>
        <td>67</td>
        <td style="color: #45c527" >2</td>
        <td style="color: #45c527" >2.9%</td>
      </tr>
      <tr>
        <th scope="row">Open Pull Requests</th>
        <td>29</td>
        <td>30</td>
        <td style="color: #45c527" >-1</td>
        <td style="color: #45c527" >3.4%</td>
      </tr>
      <tr>
        <th scope="row">Merged Pull Requests</th>
        <td>366</td>
        <td>357</td>
        <td style="color: #45c527" >9</td>
        <td style="color: #45c527" >2.5%</td>
      </tr>
      <tr>
        <th scope="row">Closed Pull Requests</th>
        <td>88</td>
        <td>82</td>
        <td style="" >6</td>
        <td style="" >7.1%</td>
      </tr>
      <tr>
        <th scope="row">Forks</th>
        <td>15</td>
        <td>15</td>
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
        <td>25</td>
        <td>25</td>
        <td style="" >0</td>
        <td style="" >0%</td>
      </tr>
      <tr>
        <th scope="row">Followers</th>
        <td>20</td>
        <td>19</td>
        <td style="color: #45c527" >1</td>
        <td style="color: #45c527" >5.1%</td>
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